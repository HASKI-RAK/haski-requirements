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
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_student_course"
    - path: "frontend/src/pages/Home/Home.test.tsx"
      name: "Test the Home page-1; Test the Home page-2"
    - path: "frontend/src/services/Courses/fetchCourses.test.tsx"
      name: "fetchCourses has expected behaviour"
    - path: "HASKI-Frontend/src/store/Slices/CoursesSlice.test.ts"
      name: "CoursesSlice caching"
    - path: "HASKI-Frontend/src/store/Slices/CourseSlice.test.ts"
      name: "CourseSlice setCourse"
  merged_from: ["HASKI-REQ-0054"]
---

## Beschreibung

Das System **shall** Kursdaten für Studierende über REST bereitstellen, sowohl als gefilterte Übersicht aller belegten Veranstaltungen als auch für einzelne Kurse. Die Schnittstelle muss die eindeutigen Zuordnungen aus dem angebundenen LMS berücksichtigen und die relevanten Kursmetadaten in konsistenter Form bereitstellen.

### Kursübersicht

Listet alle Kurse, für die eine gültige Einschreibung des Studierenden besteht.

### Einzelkurs-Details

Liefert die Detaildaten eines belegten Kurses, sobald eine Anwendung diese für einen berechtigten Studierenden benötigt. Die gelieferten Informationen umfassen sämtliche Kurseigenschaften, die für Dashboards, Lernräume oder Reporting relevant sind.

## Akzeptanzkriterien

### Kursübersicht

- [x] Die ausgelieferte Kursliste enthält ausschließlich Veranstaltungen, für die eine gültige Einschreibung des angefragten Studierenden besteht.
- [x] Pro Kurs stehen die wesentlichen Metadaten (z. B. interne ID, LMS-Referenz, Name, Hochschule) zur Verfügung, sodass Lernräume diese Informationen direkt anzeigen können.
- [x] Änderungen an Einschreibungen oder Kursdaten werden ohne zusätzliche Synchronisation in der Kursübersicht sichtbar.

### Einzelkurs-Details

- [x] Für gültige Kurs-/Studierendenkombinationen stehen vollständige Metadaten (z. B. interne Kennung, LMS-Referenz, Bezeichnung, Hochschule) zur Verfügung.
- [x] Anfragen außerhalb der zulässigen Einschreibungen werden konsequent abgewiesen und geben keine Details zu fremden Kursen preis.
- [x] Aktualisierte Kursattribute sind unmittelbar nach Pflege im System sichtbar, sodass gekoppelte Oberflächen immer auf aktuelle Daten zugreifen.

## Rationale

SyRS-FUNC-008 fordert konfigurierbare Lernräume. Eine kompakte Kursübersicht bildet dafür die Grundlage, weil sie festlegt, zwischen welchen Kontexten Studierende wechseln dürfen und welche Inhalte anschließend geladen werden. Konfigurierbare Lernräume benötigen auch Detailinformationen pro Kurs, etwa für Breadcrumbs, Kursbanner oder die Auswahl von Lernpfaden.

## Hinweise

- Autorisierungslogik und Datensicht sollen mit den Kursdetail- und Topic-Routen abgestimmt sein.
- Das OAS-Dokument beschreibt die nutzbaren Felder; Anpassungen sind gemeinsam mit Frontend und Analytics zu planen.
- Relevante Felder sind im OAS-Schema dokumentiert und sollten versioniert angepasst werden.
