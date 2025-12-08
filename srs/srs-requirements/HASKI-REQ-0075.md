---
id: HASKI-REQ-0075
title: Nutzerstammdaten aus Moodle aktualisieren
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#81"]
  parents: ["SyRS-INT-003"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_user_from_moodle"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_user"
---

## Beschreibung

Das Backend **shall** einen OAS-konformen Endpunkt `PUT /lms/user/<user_id>/<lms_user_id>` bereitstellen, über den Moodle das Stammdatenprofil eines bereits angelegten HASKI-Nutzers aktualisieren kann (z. B. Namensänderung, neue Hochschulzuordnung). Die Route **shall** die Kombination aus interner `user_id` und verknüpfter `lms_user_id` prüfen, bevor Änderungen an den Tabellen `haski_user` und `settings` vorgenommen werden, damit nur existierende Profile angepasst werden. Erfolgreiche Updates **shall** die aktuellen Einstellungen (Theme, Sprache, Passwort-Hash) unverändert zurückgeben, sodass Frontends sofort dieselbe Sicht erhalten.

## Akzeptanzkriterien

- [x] Ein vollständiger Request mit `name` und `university` liefert HTTP 201 sowie ein JSON mit `id`, `name`, `university`, `lms_user_id`, `role` und `settings`.
- [x] Fehlende Pflichtfelder oder falsche Datentypen führen zu HTTP 400 mit der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) und verursachen keine Datenänderung.
- [x] Nicht existente Kombinationen aus `user_id` und `lms_user_id` werden mit HTTP 404 beantwortet und offenbaren keine internen Details.
- [x] Bereits gespeicherte Rollenzuordnungen und Settings bleiben bei einem Update unverändert erhalten, damit Berechtigungen und UI-Präferenzen konsistent bleiben.

## Rationale

GitHub issue GH-30 (Basic Setup 2.0) fordert vollständige CRUD-Unterstützung für alle im OAS beschriebenen LMS-Nutzerendpunkte. GH-81 automatisiert zwar die Erstanlage der Nutzer und Settings, dennoch müssen spätere Änderungen aus Moodle synchronisiert werden, um Dubletten zu vermeiden und personenbezogene Daten gemäß SyRS-INT-003 aktuell zu halten.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Fehlerhafte Requests sollen auditierbar geloggt werden, weil sie auf fehlerhafte Moodle-Integrationen oder Stammdatenimporte hinweisen.
