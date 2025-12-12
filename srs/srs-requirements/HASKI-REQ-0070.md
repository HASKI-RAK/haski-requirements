---
id: HASKI-REQ-0070
title: Benutzereinstellungen mandantenfähig abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#81", "HASKI-RAK/HASKI-Backend#30"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_user_settings_by_id"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_user_settings_by_id"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_user_settings"
    - path: "frontend/src/components/ThemeMenu/Modal/ThemeModal.test.tsx"
      name: "ThemeModal tests"
    - path: "frontend/src/services/Theme/postUserSettings.test.tsx"
      name: "postUserSettings has expected behaviour"
---

## Beschreibung

Das Backend **shall** einen dedizierten GET-Endpunkt `GET /user/<user_id>/<lms_user_id>/settings` bereitstellen, der die mandantenbezogenen Benutzereinstellungen (z. B. Farbschema `theme` und Passwort-Placeholder `pswd`) anhand der Kombination aus lokaler User-ID und verknüpfter Moodle-ID zurückliefert. Nur Nutzer:innen mit gültiger Session und Berechtigung **shall** ihre eigenen Settings oder delegierte Profile abrufen dürfen. Fehlende, inkonsistente oder nicht autorisierte ID-Kombinationen **shall** deterministisch mit einer Fehlantwort (`{"error": "...", "message": "..."}`) quittiert werden, ohne weitere Profildaten preiszugeben.

Ergänzend **shall** das Backend einen abgesicherten PUT-Endpunkt `PUT /user/<user_id>/<lms_user_id>/settings` bereitstellen, über den authentifizierte Nutzer:innen ihre mandantenbezogenen Einstellungen (z. B. `theme`, optionale Passwort-Placeholder `pswd`) aktualisieren können, sowie einen komplementären `DELETE /user/<user_id>/<lms_user_id>/settings`-Endpunkt, der die gespeicherten Settings auf ihre Standardwerte zurücksetzt.

## Akzeptanzkriterien

### Lesen von Benutzereinstellungen

- [x] Erfolgreiche Requests liefern HTTP 200, enthalten mindestens die Felder `theme` und `pswd` und spiegeln die zuletzt persistierten Einstellungen wider.
- [x] Nicht existierende oder nicht verknüpfte Nutzer:innen resultieren in HTTP 404 mit der beschriebenen Fehlstruktur.
- [x] Der Endpunkt prüft, dass `user_id` und `lms_user_id` zusammenpassen, bevor Einstellungen gelesen werden, und gibt keine Daten bei Inkonsistenzen preis.
- [x] Antwortschema bleibt OAS-konform (Basic Setup 2.0), sodass Frontend-Komponenten ohne zusätzliche Mapper auf Nutzerpräferenzen zugreifen können.
- [x] Security-Tests stellen sicher, dass weder Passworthashes noch sensible Stammdaten außerhalb des Settings-Blocks ausgeliefert werden.

### Aktualisieren und Zurücksetzen von Benutzereinstellungen

- [x] Valide Requests mit `theme` (und optional `pswd`) an `PUT /user/<user_id>/<lms_user_id>/settings` liefern HTTP 201 und geben die aktualisierten Felder (`theme`, `pswd`) im Response-Body zurück.
- [x] Nicht existierende oder nicht zusammenpassende `user_id`/`lms_user_id`-Kombinationen führen zu HTTP 404 mit der standardisierten Fehlerantwort.
- [x] Fehlende Pflichtfelder oder ungültige Werte (z. B. falsche Struktur für `theme`) resultieren in HTTP 400 und persistieren keine Änderungen.
- [x] Die transaktionale Aktualisierung verwendet `update_settings_for_user`, sodass `settings`-Datensätze konsistent gespeichert und für nachfolgende GET-Aufrufe verfügbar sind.
- [x] Ein `DELETE /user/<user_id>/<lms_user_id>/settings`-Aufruf mit gültiger Kombination liefert HTTP 200 samt Defaultfeldern (`theme`, `pswd`) und verweigert unbekannte User:innen mit HTTP 404, ohne neue Daten anzulegen.

## Rationale

Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) definiert das Basic-Setup-OAS und verlangt dedizierte Endpunkte für Nutzerprofile. Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) stellt sicher, dass bei der ersten Anmeldung jede:r Nutzer:in automatisch eine Settings-Zeile erhält. Der hier beschriebene Endpunkt macht diese Daten für UI-Komponenten abrufbar, sodass z. B. Theme-Umschaltungen oder Passwortwechsel synchronisiert bleiben und der LTI-Flow (SyRS-INT-003) konsistente Mandantenlogik sicherstellt.

## Hinweise

- Rückgaben enthalten ausschließlich konfigurierbare Präferenzfelder; Stammdaten sind über `HASKI-REQ-0069` abrufbar und werden hier bewusst ausgespart.
- Fehlermeldungen sollen klar zwischen "User not found" und Autorisierungsproblemen unterscheiden, damit Betriebsteams Supporttickets schneller schließen können.
- E2E-Verifikation: `backend/tests/e2e/test_api.py::TestApi::test_get_user_settings_by_id`.
