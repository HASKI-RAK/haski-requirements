---
id: HASKI-REQ-0035
title: Automatische Kursanlage, -synchronisation und Kurs-Seite
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents:
    - "SyRS-INT-003"
    - "SyRS-INT-005"
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Frontend#47"
    - "HASKI-RAK/HASKI-Frontend#48"
    - "HASKI-RAK/HASKI-Frontend#19"
    - "HASKI-RAK/HASKI-Frontend#339"
    - "HASKI-RAK/HASKI-Backend#30"
  tests:
    - "backend/tests/e2e/test_api.py::TestApi::test_api_create_course_from_moodle_without_start_date"
    - "backend/tests/e2e/test_api.py::TestApi::test_api_create_course_from_moodle"
    - "backend/tests/unit/test_service.py::test_get_courses_from_moodle"
    - "backend/tests/e2e/test_api.py::TestApi::test_update_course_from_moodle"
    - "backend/tests/e2e/test_api.py::TestApi::test_update_course_from_moodle_with_start_date"
    - path: "frontend/src/components/CreateCourse/Modal/CreateCourseModal.test.tsx"
      name: "CreateCourseModal"
    - path: "frontend/src/components/CreateCourse/Table/CreateCourseTable.test.tsx"
      name: "CreateCourseTable"
    - path: "frontend/src/components/CreateCourse/Table/CreateCourseDetailsTable.test.tsx"
      name: "CreateCourseDetailsTable"
    - path: "frontend/src/components/CourseCard/CourseCard.test.tsx"
      name: "CourseCard Component"
    - path: "frontend/src/components/CourseCard/CreateCourseCard.test.tsx"
      name: "CreateCourseCard Component"
    - path: "frontend/src/components/DeleteEntityModal/DeleteEntityModal.test.tsx"
      name: "DeleteEntityModal Component"
    - path: "frontend/src/pages/Course/Course.test.tsx"
      name: "Course Page"
    - path: "frontend/src/pages/Home/Home.test.tsx"
      name: "Home Page"
    - path: "frontend/src/services/Course/postCourse.test.tsx"
      name: "postCourse has expected behaviour"
    - path: "frontend/src/services/CourseTopics/CourseTopics.test.tsx"
      name: "useCourseTopics"
    - path: "frontend/src/services/RemoteCourses/fetchRemoteCourses.test.tsx"
      name: "fetchRemoteCourses has expected behaviour"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_remote_courses"
---

## Beschreibung

Das System **shall** Kurse automatisch basierend auf Daten aus dem Learning Management System (Moodle) anlegen und aktualisieren. Dabei **shall** die Kursstruktur, Metadaten (wie Name, ID, Startdatum) und die Zuordnung zur Hochschule übernommen werden.

Das System **shall** eine Kurs-Seite bereitstellen, die eine Übersicht aller Themen (Topics) des Kurses anzeigt. Die Seite **shall** die Navigation zu den einzelnen Themen ermöglichen. Für Lehrende (Course Creator) **shall** zusätzlich ein Button zum Erstellen neuer Themen angezeigt werden.

## Akzeptanzkriterien

### Backend / Synchronisation

- [ ] Das System stellt einen Endpunkt zur Erstellung von Kursen bereit
- [ ] Kurse werden mit korrekter Moodle-ID (LMS-ID) angelegt
- [ ] Metadaten wie Name, Erstellungsdatum und Startdatum werden korrekt übernommen
- [ ] Das System verhindert das Anlegen von Duplikaten (basierend auf LMS-ID)
- [ ] Fehlende optionale Parameter (z.B. Startdatum) werden robust behandelt
- [ ] Ungültige Eingabedaten führen zu entsprechenden Fehlermeldungen

### Frontend / Kurs-Seite

- [x] Die Seite zeigt eine Liste aller Themen des Kurses an.
- [x] Ein Klick auf ein Thema navigiert zur entsprechenden Themen-Seite.
- [x] Lehrende sehen einen Button "Thema erstellen".
- [x] Studierende sehen den Button "Thema erstellen" nicht.

## Rationale

Die Synchronisation der Kursdaten ist essenziell, um die Lernumgebung in HASKI mit dem führenden System (Moodle) konsistent zu halten. Dies wurde initial im Rahmen der Basic Backend Structure (Issue #21) umgesetzt. Die Kurs-Seite ist der zentrale Einstiegspunkt für Studierende und Lehrende, um auf die Lerninhalte zuzugreifen und diese zu verwalten.
