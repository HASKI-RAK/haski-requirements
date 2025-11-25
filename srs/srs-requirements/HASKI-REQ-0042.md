---
id: HASKI-REQ-0042
title: Lernaktivitäts-Besuche für Analytics erfassen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-007
links:
  parents: ["SyRS-FUNC-007"]
  stories: ["HASKI-RAK/HASKI-Frontend#136"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_topic_visit"
---

## Beschreibung

Das System **shall** jede Topic- und Learning-Element-Nutzung eines Studierenden über dedizierte REST-Endpunkte erfassen, damit Learning-Analytics-Dashboards verlässliche Verlaufsdaten besitzen. Ein Besuch **shall** mindestens den Startzeitpunkt `visit_start`, die referenzierte Moodle-Identität (`student_id`, `moodle_user_id`, `topic_id` bzw. `learning_element_id`) sowie automatisch gesetzte Endzeitpunkte speichern. Ungültige oder unvollständige Nutzlasten **shall** mit einer validierenden Fehlermeldung beantwortet werden, ohne persistente Einträge zu erzeugen.

## Akzeptanzkriterien

- [ ] `POST /lms/student/<student_id>/<moodle_user_id>/topic/<topic_id>` legt einen Besuchseintrag mit `visit_start` und optionalem `visit_end` an; Antwort enthält `id`, `student_id`, `topic_id`, `visit_start`, `visit_end`.
- [ ] `POST /lms/student/<student_id>/<moodle_user_id>/learningElement/<learning_element_id>` verhält sich analog und speichert `learning_element_id` statt `topic_id`.
- [ ] Fehlende Pflichtfelder oder falsche Datentypen führen zu HTTP 400 mit einer klaren Fehlerstruktur (`{"error": ..., "message": ...}`), ohne Seiteneffekte.
- [ ] Falsche Datumformate (z.B. `01.01.2023`) werden abgelehnt und begründet.
- [ ] Jeder persistierte Besuch ist eindeutig dem Studierenden und dem referenzierten Topic bzw. Learning Element zuordenbar, damit spätere Aggregationen (z.B. Frontend-Issue GH-136) darauf zugreifen können.

## Rationale

Frontend-Issue [GH-136](https://github.com/HASKI-RAK/HASKI-Frontend/issues/136) fordert die Bereitstellung von Learning-Analytics-Daten direkt im HASKI-Dashboard. Damit Nutzungsstatistiken serverseitig berechnet werden können, müssen Topic- und Learning-Element-Besuche transaktional erfasst und validiert werden. Die hier spezifizierten Endpunkte liefern die Rohdaten für spätere Aggregationen (Verweildauer, zuletzt besuchte Inhalte etc.) und stellen sicher, dass jeder Trackable Event korrekt mit Moodle-Identitäten verknüpft ist.

## Hinweise

- Die Speicherung erfolgt in den Tabellen `student_topic_visit` bzw. `student_learning_element_visit`; beide Tabellen benötigen Foreign-Key-Constraints auf `student`, `topic` bzw. `learning_element`.
- `visit_end` kann serverseitig nachgetragen werden (z.B. durch Abschlussjobs), wenn nur der Startzeitpunkt gesendet wurde.
- Die Endpunkte teilen sich Validierungslogik mit bestehenden Moodle-LMS-Bridges; daher sollen Fehlermeldungen konsistent mit anderen `/lms/*`-Routen sein.
- Zugriff erfolgt ausschließlich über authentifizierte LMS-Bridges, damit Studierende nicht direkt auf die Rohendpunkte zugreifen müssen.
