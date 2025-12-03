---
id: HASKI-REQ-0053
title: Studierendenkurse über REST abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#131", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_student_courses"
    - path: "frontend/src/pages/Home/Home.test.tsx"
      name: "Test the Home page-1; Test the Home page-2"
    - path: "frontend/src/services/Courses/fetchCourses.test.tsx"
      name: "fetchCourses has expected behaviour"
---

## Beschreibung

Das System **shall** eine gefilterte Kursübersicht für jeden Studierenden bereitstellen, sodass nur die tatsächlich belegten Veranstaltungen angezeigt werden. Die Schnittstelle muss die eindeutigen Zuordnungen aus dem angebundenen LMS berücksichtigen und die relevanten Kursmetadaten in konsistenter Form bereitstellen.

## Akzeptanzkriterien

- [x] Die ausgelieferte Kursliste enthält ausschließlich Veranstaltungen, für die eine gültige Einschreibung des angefragten Studierenden besteht.
- [x] Pro Kurs stehen die wesentlichen Metadaten (z. B. interne ID, LMS-Referenz, Name, Hochschule) zur Verfügung, sodass Lernräume diese Informationen direkt anzeigen können.
- [x] Änderungen an Einschreibungen oder Kursdaten werden ohne zusätzliche Synchronisation in der Kursübersicht sichtbar.

## Rationale

SyRS-FUNC-008 fordert konfigurierbare Lernräume. Eine kompakte Kursübersicht bildet dafür die Grundlage, weil sie festlegt, zwischen welchen Kontexten Studierende wechseln dürfen und welche Inhalte anschließend geladen werden.

## Hinweise

- Autorisierungslogik und Datensicht sollen mit den Kursdetail- und Topic-Routen abgestimmt sein.
- Das OAS-Dokument beschreibt die nutzbaren Felder; Anpassungen sind gemeinsam mit Frontend und Analytics zu planen.
