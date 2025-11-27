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
---

## Beschreibung

Das Backend **shall** einen dedizierten GET-Endpunkt `GET /user/<user_id>/<lms_user_id>/settings` bereitstellen, der die mandantenbezogenen Benutzereinstellungen (z. B. Farbschema `theme` und Passwort-Placeholder `pswd`) anhand der Kombination aus lokaler User-ID und verknüpfter Moodle-ID zurückliefert. Nur Nutzer:innen mit gültiger Session und Berechtigung **shall** ihre eigenen Settings oder delegierte Profile abrufen dürfen. Fehlende, inkonsistente oder nicht autorisierte ID-Kombinationen **shall** deterministisch mit einer Fehlantwort (`{"error": "...", "message": "..."}`) quittiert werden, ohne weitere Profildaten preiszugeben.

## Akzeptanzkriterien

- [x] Erfolgreiche Requests liefern HTTP 200, enthalten mindestens die Felder `theme` und `pswd` und spiegeln die zuletzt persistierten Einstellungen wider.
- [x] Nicht existierende oder nicht verknüpfte Nutzer:innen resultieren in HTTP 404 mit der beschriebenen Fehlstruktur.
- [x] Der Endpunkt prüft, dass `user_id` und `lms_user_id` zusammenpassen, bevor Einstellungen gelesen werden, und gibt keine Daten bei Inkonsistenzen preis.
- [x] Antwortschema bleibt OAS-konform (Basic Setup 2.0), sodass Frontend-Komponenten ohne zusätzliche Mapper auf Nutzerpräferenzen zugreifen können.
- [x] Security-Tests stellen sicher, dass weder Passworthashes noch sensible Stammdaten außerhalb des Settings-Blocks ausgeliefert werden.

## Rationale

Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) definiert das Basic-Setup-OAS und verlangt dedizierte Endpunkte für Nutzerprofile. Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) stellt sicher, dass bei der ersten Anmeldung jede:r Nutzer:in automatisch eine Settings-Zeile erhält. Der hier beschriebene Endpunkt macht diese Daten für UI-Komponenten abrufbar, sodass z. B. Theme-Umschaltungen oder Passwortwechsel synchronisiert bleiben und der LTI-Flow (SyRS-INT-003) konsistente Mandantenlogik sicherstellt.

## Hinweise

- Rückgaben enthalten ausschließlich konfigurierbare Präferenzfelder; Stammdaten sind über `HASKI-REQ-0069` abrufbar und werden hier bewusst ausgespart.
- Fehlermeldungen sollen klar zwischen "User not found" und Autorisierungsproblemen unterscheiden, damit Betriebsteams Supporttickets schneller schließen können.
- E2E-Verifikation: `backend/tests/e2e/test_api.py::TestApi::test_get_user_settings_by_id`.
