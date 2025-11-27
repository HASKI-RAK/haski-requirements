---
id: HASKI-REQ-0055
title: Kursinhalte (Topics) pro Studierendenkurs abrufen
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
      name: "TestApi::test_get_student_course_topics"
---

## Beschreibung

Das System **shall** über `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic` alle Topics (inklusive Subtopics) eines Kurses ausliefern, sofern der Studierende für diesen Kurs eingeschrieben ist. Die Antwort **shall** die Topic-Metadaten (`id`, `lms_id`, `name`, `is_topic`, `contains_le`, `university`, `parent_id`) sowie den individuellen Lernfortschrittskontext (`student_topic`) enthalten, damit Lernräume und Lernpfad-Berechnungen (GH-76) auf denselben Datenbestand zugreifen können. Ungültige IDs oder fehlende Berechtigungen **shall** deterministisch abgelehnt werden.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten den Schlüssel `topics`, dessen Elemente mindestens die genannten Topic-Metadaten und `student_topic` enthalten.
- [x] Ungültige Studierenden-, Kurs- oder Topiczuweisungen resultieren in HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Topics spiegeln die in GH-76 genutzten Kurs-Topic-Relationen wider, sodass Lernpfad-Berechnungen und Frontends konsistent bleiben.
- [x] Der Endpoint folgt dem in GH-30 dokumentierten OAS-Schema und akzeptiert Moodle-IDs zur Identifikation.

## Rationale

SyRS-FUNC-008 fordert konfigurierbare Lernräume. Dafür muss jeder Studierende die zugehörigen Topics eines belegten Kurses inklusive persönlicher Lernfortschrittsinformationen abrufen können. GitHub issue GH-76 beschreibt die zugrunde liegende Datenhaltung für Kurs-Topic-Relationen, während GH-30 die formale API-Struktur festlegt.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/76
- Supporting issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Die gleiche Pfadstruktur besitzt Unterrouten für Subtopics und Learning Elements; wiederverwendbare Autorisierungsprüfungen werden empfohlen.
