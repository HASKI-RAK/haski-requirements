---
id: HASKI-REQ-0080
title: Kontaktmeldungen löschen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-011
links:
  parents: ["SyRS-FUNC-011"]
  stories:
    - "HASKI-RAK/HASKI-Backend#39"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_delete_contact_form"
---

## Beschreibung

Das Backend **shall** zusätzlich zum Absenden von Supportmeldungen einen authentifizierten Endpunkt `DELETE /user/<user_id>/<lms_user_id>/contactform` bereitstellen, über den Studierende oder Supportrollen einen zuvor gespeicherten Eintrag entfernen können, sobald der Vorgang abgeschlossen ist. Die Route **shall** dieselbe Nutzer- und Moodle-ID-Kombination validieren wie der `POST`-Endpunkt und ausschließlich vorhandene Meldungen löschen; nach erfolgreicher Ausführung **shall** eine bestätigende Antwort (HTTP 201 mit `{"message": ...}`) zurückgegeben werden.

## Akzeptanzkriterien

- [x] Gültige Kombinationen aus `user_id` und `lms_user_id` führen zu einem erfolgreichen Löschvorgang mit HTTP 201 und einer Bestätigungsnachricht.
- [x] Nicht existierende Nutzer:innen oder fehlende Kontaktmeldungen werden mit HTTP 404 und der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) beantwortet.
- [x] Der Endpunkt erfordert dieselben Authentifizierungsmechanismen wie das Erstellen des Kontaktformulars, sodass nur berechtigte Personen eigene Meldungen entfernen können.
- [x] Der Löschvorgang hinterlässt keine verwaisten Relationen; anschließend abrufbare Listen enthalten den entfernten Datensatz nicht mehr.

## Rationale

GitHub Issue [#39](https://github.com/HASKI-RAK/HASKI-Backend/issues/39) führte die Kontaktformular-Funktion ein und umfasst den kompletten Lebenszyklus einer Meldung. Dieses Requirement stellt sicher, dass nachbearbeitete Tickets wieder gelöscht werden können, damit Supportteams ihre Backlogs sauber halten. Der E2E-Test `backend/tests/e2e/test_api.py::TestApi::test_delete_contact_form` prüft die End-to-End-Löschoperation.

## Hinweise

- Löschvorgänge sollen revisionssicher geloggt werden, damit Supportfälle rückverfolgbar bleiben.
- Eine spätere Erweiterung kann Administrator:innen erlauben, fremde Meldungen zu löschen; das Verhalten bleibt kompatibel, solange die Autorisierung gewahrt bleibt.
