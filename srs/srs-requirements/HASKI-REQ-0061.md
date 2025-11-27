---
id: HASKI-REQ-0061
title: Subtopics eines belegten Kurses abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#76", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_sub_topics_for_topic"
---

## Beschreibung

Das System **shall** für eingeschriebene Studierende über `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic/<topic_id>/subtopic` sämtliche Subtopics (Unterabschnitte) eines Topics zurückliefern. Die Antwort **shall** den Schlüssel `topics` enthalten, dessen Elemente mindestens `id`, `lms_id`, `name`, `is_topic`, `contains_le`, `university`, `parent_id` sowie den Kontext `student_topic` bereitstellen, damit Lernräume, Lernpfade und Analytics dieselben Metadaten nutzen. Zugriffe auf fremde Kurse oder Topics **shall** deterministisch mit 404 bzw. 403 beantwortet werden.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten `topics` inkl. der genannten Felder pro Subtopic.
- [x] Ungültige Studierenden-, Kurs- oder Topic-IDs führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Die Route akzeptiert Moodle-IDs und wiederverwendet dieselbe Mapping-Logik wie `GET .../topic` (HASKI-REQ-0055).
- [x] Die API antwortet deterministisch, auch wenn keine Subtopics existieren (leeres Array statt Fehler).

## Rationale

GitHub Issue [#76](https://github.com/HASKI-RAK/HASKI-Backend/issues/76) beschreibt die Kurs-Topic-Relationen, auf deren Basis Lernräume und Lernpfade zusammengesetzt werden. Subtopics bilden die nächste Aggregationsebene (z. B. Wochenabschnitte) und müssen für Dashboards und Pfadberechnung abrufbar sein. OAS-Spezifikation GH-30 legt die Felder und ID-Mappings fest. Mit dem Endpoint können Frontends und Automationen konsistent dieselben Datenquellen wie die Kursübersicht nutzen.

## Hinweise

- Autorisierung erfolgt über dieselben Decorators wie bei `GET .../topic`.
- Für Topics ohne Subtopics wird `topics: []` zurückgegeben.
- Strukturierte Fehlermeldungen folgen dem globalen Fehlerformat.
