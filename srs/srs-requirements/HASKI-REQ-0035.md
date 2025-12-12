---
id: HASKI-REQ-0035
title: Automatische Kursanlage, Enrollment und Kurs-Seite
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-008
merged_from: ["HASKI-REQ-0053", "HASKI-REQ-0038", "HASKI-REQ-0078", "HASKI-REQ-0082", "HASKI-REQ-0068"]
links:
  parents:
    - "SyRS-INT-003"
    - "SyRS-INT-005"
    - "SyRS-FUNC-008"
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Frontend#47"
    - "HASKI-RAK/HASKI-Frontend#48"
    - "HASKI-RAK/HASKI-Frontend#19"
    - "HASKI-RAK/HASKI-Frontend#339"
    - "HASKI-RAK/HASKI-Backend#30"
    - "HASKI-RAK/HASKI-Backend#131"
    - "GH-131"
    - "GH-123"
  tests:
    - "backend/tests/e2e/test_api.py::TestApi::test_api_create_course_from_moodle_without_start_date"
    - "backend/tests/e2e/test_api.py::TestApi::test_api_create_course_from_moodle"
    - "backend/tests/unit/test_service.py::test_get_courses_from_moodle"
    - "backend/tests/e2e/test_api.py::TestApi::test_update_course_from_moodle"
    - "backend/tests/e2e/test_api.py::TestApi::test_update_course_from_moodle_with_start_date"
    - path: "frontend/src/components/CreateCourse/Modal/CreateCourseModal.test.tsx"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_course"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_course_by_id"
      - path: "backend/tests/unit/test_service.py"
        name: "test_update_course_without_start_date"
      - path: "backend/tests/unit/test_service.py"
        name: "test_update_course_with_start_date"
      - path: "backend/tests/unit/test_service.py"
        name: "test_delete_course"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_course_topic"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_course_topic_by_course"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_course_topic_by_topic"
      - path: "backend/tests/unit/test_service.py"
        name: "test_delete_course_topic_by_course"
      - path: "backend/tests/unit/test_service.py"
        name: "test_delete_course_topic_by_topic"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_topics_by_student_and_course_id"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_les_for_course_id"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_les_for_course_and_topic_id"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_sub_topics"
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
    - path: "backend/tests/unit/test_service.py"
      name: "test_add_student_to_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_add_teacher_to_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_course_creator_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_courses_by_uni"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_courses_by_student_id"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_teacher_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_student_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_student_to_course_duplicate"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_add_all_students_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_add_all_students_to_topics"
    - path: "frontend/src/services/Topic/postAddAllStudentsToTopics.test.ts"
      name: "postAddAllStudentsToTopics has expected behaviour"
    - path: "frontend/src/services/Course/postAddAllStudentsToCourse.test.ts"
      name: "postAddAllStudentsToCourse has expected behaviour"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_delete_course_from_moodle"
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
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_remote_course_content"
    - path: "HASKI-Frontend/src/services/RemoteTopics/fetchRemoteTopics.test.tsx"
      name: "fetchRemoteTopics has expected behaviour"
    - path: "HASKI-Frontend/src/store/Slices/RemoteTopicSlice.test.tsx"
      name: "RemoteTopicSlice"
---

## Beschreibung

Das System **shall** Kurse automatisch basierend auf Daten aus dem Learning Management System (Moodle) anlegen und aktualisieren. Dabei **shall** die Kursstruktur, Metadaten (wie Name, ID, Startdatum) und die Zuordnung zur Hochschule übernommen werden.

Das System **shall** eine Kurs-Seite bereitstellen, die eine Übersicht aller Themen (Topics) des Kurses anzeigt. Die Seite **shall** die Navigation zu den einzelnen Themen ermöglichen. Für Lehrende (Course Creator) **shall** zusätzlich ein Button zum Erstellen neuer Themen angezeigt werden.

Das System **shall** Benutzer (Studierende, Lehrende, Course Creator) in Kursen einschreiben können. Studierende **shall** nur die Kurse sehen, in denen sie eingeschrieben sind. Das System **shall** verschiedene Rollen innerhalb eines Kurses unterstützen (Student, Teacher) und über abgesicherte Endpunkte sowohl Einzelzuordnungen (Lehrkraft/Studierender zu Kurs) als auch Bulk-Synchronisationen aller in Moodle eingeschriebenen Studierenden pro Kurs vornehmen. Die Synchronisation **shall** Moodle-Einschreibungen prüfen, fehlende `student_course`-Relationen anlegen, Duplikate verhindern und auf Wunsch alle betroffenen Topics eines Kurses mit denselben Studierenden-Zuordnungen versehen, damit Lernpfade und Empfehlungen unmittelbar auf Kurs- und Topic-Ebene starten können.

Ergänzend **shall** das System eine REST-Schnittstelle bereitstellen, über die Studierende ihre Kurse abrufen können – sowohl als gefilterte Übersicht aller belegten Veranstaltungen als auch für einzelne Kurse. Die Kursübersicht **shall** ausschließlich Veranstaltungen liefern, für die eine gültige Einschreibung des Studierenden besteht, und pro Kurs die wesentlichen Metadaten (interne ID, LMS-Referenz, Name, Hochschule) in konsistenter Form bereitstellen. Einzelkurs-Detailabfragen **shall** dieselben Metadaten für einen konkret adressierten Kurs zurückgeben und Anfragen außerhalb der zulässigen Einschreibungen konsequent abweisen.

Über die Synchronisation hinaus **shall** das Backend vollständige CRUD-Funktionen für Kurse, Kurs-Topic-Zuordnungen und kursbezogene Abfragen bereitstellen. Dazu gehört, dass Kurse mit und ohne Startdatum gepflegt werden können, Topic-Zuordnungen konsistent bleiben und Service-Layer-Abfragen nach Hochschule, Kurs-ID oder Topic-ID stets die korrekten Datensichten liefern.

Zusätzlich **shall** das Backend einen separaten Endpunkt `GET /lms/remote/course/<course_id>/content` bereitstellen, der die aus dem Moodle-LMS gelieferten Kurssektionen inklusive aller Module (Learning Elements) strukturerhaltend und weitgehend unverändert an HASKI-Clients zurückgibt. Vor dem Abruf **shall** die Kurs-ID validiert und die Moodle-Webservice-Anfrage ausgeführt werden; fehlerhafte Antworten (HTTP-Fehler, invalide JSON-Strukturen) **shall** deterministisch behandelt werden. Jedes Topic-Objekt **shall** mindestens `topic_lms_id`, `topic_lms_name` und eine Liste `lms_learning_elements` enthalten, deren Einträge wiederum mindestens `lms_id`, `lms_learning_element_name` und `lms_activity_type` bereitstellen, damit Import- und Scaffolding-Funktionen vollständige Metadaten besitzen.

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

### Enrollment und Sichtbarkeit

- [x] Benutzer können in Kursen eingeschrieben werden (Studierende, Lehrende, Course Creator) – sowohl einzeln über dedizierte Endpunkte als auch bulkweise auf Basis der in Moodle vorhandenen Einschreibungen.
- [x] Studierende sehen nur die Kurse, in denen sie (via Moodle) eingeschrieben sind; doppelte Zuordnungen werden erkannt und verhindert.
- [x] Das System unterstützt verschiedene Rollen innerhalb eines Kurses und spiegelt Rollenänderungen aus Moodle konsistent wider.

### Bulk-Synchronisation von Moodle-Einschreibungen

- [x] Ein REST-Endpunkt `POST /course/<course_id>/allStudents` synchronisiert alle in Moodle eingeschriebenen Studierenden in die HASKI-Relation `student_course` und liefert bei Erfolg HTTP 201 mit `CREATED`, `course_id` und der Anzahl neu verknüpfter Studierender.
- [x] Ein ergänzender Endpunkt `POST /course/<course_id>/topics/allStudents` stellt sicher, dass alle Topics des Kurses dieselben Studierenden-Zuordnungen erhalten; die Implementierung ist idempotent und erzeugt keine doppelten Relationen.
- [x] Inkonsistente oder fehlende Einschreibungen (z. B. Studierende ohne passende Hochschul- oder Kurszuordnung) erzeugen keine Relationen, werden aber nachvollziehbar geloggt.
- [x] Wiederholte Aufrufe ohne neue LMS-Einschreibungen erzeugen keine zusätzlichen Zuordnungen und kennzeichnen dies in der Antwort (`CREATED: false`).

### Kursübersicht-API (Studierendenkurse über REST)

- [x] Die bereitgestellte Kursliste für einen Studierenden enthält ausschließlich Veranstaltungen, für die eine gültige Einschreibung des angefragten Studierenden besteht.
- [x] Pro Kurs stehen die wesentlichen Metadaten (z. B. interne ID, LMS-Referenz, Name, Hochschule) zur Verfügung, sodass Lernräume und Dashboards diese Informationen direkt anzeigen können.
- [x] Änderungen an Einschreibungen oder Kursdaten werden ohne zusätzliche Synchronisation in der Kursübersicht sichtbar.

### Einzelkurs-Details-API

- [x] Für gültige Kurs-/Studierendenkombinationen stehen vollständige Metadaten (z. B. interne Kennung, LMS-Referenz, Bezeichnung, Hochschule) über REST zur Verfügung.
- [x] Anfragen außerhalb der zulässigen Einschreibungen werden konsequent abgewiesen und geben keine Details zu fremden Kursen preis.
- [x] Aktualisierte Kursattribute sind unmittelbar nach Pflege im System in den Einzelkurs-Detailaufrufen sichtbar, sodass gekoppelte Oberflächen immer auf aktuelle Daten zugreifen.

### Verwaltung & Abfragen

- [x] Kurse können per API erstellt, aktualisiert und gelöscht werden – optionales Startdatum ist kein Pflichtfeld.
- [x] Kurs-Topic-Zuordnungen können erzeugt, abgefragt und gelöscht werden, ohne referenzielle Integrität zu verletzen.
- [x] Service-Methoden liefern Kurse nach Hochschule, Kurs-ID sowie studentischer Zugehörigkeit konsistent zurück.
- [x] Das System stellt Kurs- und Topic-Inhalte pro Kurs-ID bereit, inklusive zugehöriger Learning Elements für Kurs- und Topic-Detailansichten.

### Remote-LMS-Kursinhalte

- [x] Erfolgreiche Aufrufe von `GET /lms/remote/course/<course_id>/content` liefern HTTP 200 und eine Liste von Topic-Objekten mit den oben genannten Pflichtfeldern.
- [x] Jedes Topic enthält eine nicht-leere Liste `lms_learning_elements`, deren Einträge mindestens `lms_id`, `lms_learning_element_name` und `lms_activity_type` umfassen und beliebige Zusatzfelder aus Moodle beibehalten.
- [x] Ungültige oder nicht erreichbare Moodle-Kurse führen zu einer strukturierten Fehlermeldung (HTTP 404/502), ohne interne Stacktraces preiszugeben.
- [x] Der Endpunkt kapselt Netz-/Authentifizierungsfehler von Moodle und schreibt Fehlversuche in die Betriebslogs.

## Rationale

Die Synchronisation der Kursdaten ist essenziell, um die Lernumgebung in HASKI mit dem führenden System (Moodle) konsistent zu halten. Dies wurde initial im Rahmen der Basic Backend Structure (Issue #21) umgesetzt. Die Kurs-Seite ist der zentrale Einstiegspunkt für Studierende und Lehrende, um auf die Lerninhalte zuzugreifen und diese zu verwalten. Die Remote-Kursinhalts-API (Issue #30) ergänzt diese Synchronisation, indem sie die vollständige Kursstruktur aus Moodle für Import- und Verwaltungsfunktionen bereitstellt.
