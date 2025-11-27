---
id: HASKI-REQ-0056
title: Lernelemente eines Kurses pro Studierenden abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#21", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_les_in_course_for_student"
---

## Beschreibung

Das System **shall** über `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/learningElement` alle Lernelemente eines belegten Kurses zurückliefern. Die Route **shall** pro Eintrag die Metadaten (`id`, `lms_id`, `activity_type`, `classification`, `name`, `university`) sowie den studentenspezifischen Status (`student_learning_element`) ausgeben, damit Frontends Lernräume und Fortschrittsanzeigen aufbauen können. Ungültige Kurs- oder Studenten-IDs **shall** deterministisch abgefangen werden, damit keine fremden Inhalte offengelegt werden.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten den Schlüssel `learning_elements` mit vollständigen Metadaten sowie `student_learning_element` für jeden Eintrag.
- [x] Ungültige Studierenden- oder Kurskombinationen führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Die Route übernimmt ihre Daten aus den in GH-21 eingeführten Kurs-/Lernelement-CRUD-Strukturen und folgt der OAS-Spezifikation aus GH-30.
- [x] Die Antwort reflektiert Aktualisierungen (z. B. neue H5P-Elemente) ohne zusätzliche Synchronisation, sodass Lernräume stets aktuelle Inhalte anzeigen.

## Rationale

SyRS-FUNC-008 verlangt konfigurierbare Lernräume inklusive konkreter Lernelemente. GitHub issue GH-21 etablierte die grundlegenden CRUD-Operationen für Kurse, Topics und Learning Elements; GH-30 beschreibt die zugehörigen REST-Schnittstellen. Die Anforderung stellt sicher, dass Studierende nur die Learning Elements ihrer eigenen Kurse sehen.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/21
- Supporting issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Der Endpoint teilt sich Autorisierung und Filterlogik mit den Topic- und Kursendpunkten; gemeinsame Middleware reduziert Inkonsistenzen.
