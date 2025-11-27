---
id: HASKI-REQ-0073
title: Benutzereinstellungen aktualisieren
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003"]
  stories:
    - "HASKI-RAK/HASKI-Backend#81"
    - "HASKI-RAK/HASKI-Backend#30"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_user_settings_by_id"
---

## Beschreibung

Das Backend **shall** einen abgesicherten PUT-Endpunkt `PUT /user/<user_id>/<lms_user_id>/settings` bereitstellen, über den authentifizierte Nutzer:innen ihre mandantenbezogenen Einstellungen (z. B. `theme`, optionale Passwort-Placeholder `pswd`) aktualisieren können. Der Endpunkt **shall** die Kombination aus lokaler HASKI-User-ID und verknüpfter Moodle-ID validieren, bevor Änderungen gespeichert werden. Nur berechtigte Nutzer:innen dürfen ihre eigenen bzw. delegierten Settings ändern; fehlerhafte ID-Kombinationen oder unvollständige Payloads **shall** deterministisch mit der bekannten Fehlerstruktur (`{"error": ..., "message": ...}`) beantwortet werden. Erfolgreiche Updates **shall** die persistierten Settings sofort zurückgeben, sodass Frontends Änderungen ohne weiteren GET-Aufruf anzeigen können.

## Akzeptanzkriterien

- [x] Valide Requests mit `theme` (und optional `pswd`) liefern HTTP 201 und geben die aktualisierten Felder (`theme`, `pswd`) im Response-Body zurück.
- [x] Nicht existierende oder nicht zusammenpassende `user_id`/`lms_user_id`-Kombinationen führen zu HTTP 404 mit der standardisierten Fehlerantwort.
- [x] Fehlende Pflichtfelder oder ungültige Werte (z. B. falsche Struktur für `theme`) resultieren in HTTP 400 und persistieren keine Änderungen.
- [x] Die transaktionale Aktualisierung verwendet `update_settings_for_user`, sodass `settings`-Datensätze konsistent gespeichert und für nachfolgende GET-Aufrufe verfügbar sind.

## Rationale

GitHub Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) stellt sicher, dass für jede:n Nutzer:in initial ein Settings-Datensatz angelegt wird. Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) definiert im Basic-Setup-OAS die Nutzerverwaltungs-Endpoints, einschließlich Änderungsoperationen. Dieses Requirement macht die Aktualisierung der Settings explizit, sodass UI-Komponenten Theme-Umschaltungen oder Passwortänderungen serverseitig widerspiegeln können. Der E2E-Test `backend/tests/e2e/test_api.py::TestApi::test_update_user_settings_by_id` validiert sowohl Erfolgs- als auch Fehlerfälle.

## Hinweise

- Die Implementierung stützt sich auf `services.update_settings_for_user`, welches `UA.Settings`-Objekte erzeugt und über das Repository persistiert.
- Erweiterungen (z. B. zusätzliche Präferenzfelder) sind zulässig, solange Schema und Sicherheitsprüfungen erhalten bleiben.
- Bei Bedarf kann `reset_settings` verwendet werden, um Defaultwerte wiederherzustellen; dies ändert nichts an der hier beschriebenen Update-Schnittstelle.
