---
id: HASKI-REQ-0093
title: Kurs- und Themenverwaltung
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#131"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_course_by_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topic_by_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_topic_learning_element"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topic_learning_element_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topic_learning_element_by_le"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_topic_learning_element_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_topic_learning_element_by_le"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_learning_element"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_les_for_course_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_les_for_course_and_topic_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_sub_topics"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topics_by_student_and_course_id"
    - path: "frontend/src/services/Course/postCourse.test.tsx"
      name: "postCourse has expected behaviour"
    - path: "frontend/src/services/LearningElement/postLearningElement.test.tsx"
      name: "postLearningElement has expected behaviour"
---

## Beschreibung

Das System **shall** Funktionen zur Verwaltung von Kursen, Themen (Topics) und Lernelementen bereitstellen. Dies umfasst das Erstellen, Aktualisieren und Abrufen dieser Entitäten sowie deren Verknüpfungen (z.B. Kurs-Thema, Thema-Lernelement, Student-Kurs). Diese Funktionen bilden die Grundlage für die Abbildung der Lehrstruktur aus dem LMS in HASKI.

## Akzeptanzkriterien

- [ ] Kurse können mit und ohne Startdatum erstellt und aktualisiert werden.
- [ ] Themen (Topics) können erstellt, aktualisiert und hierarchisch (Sub-Topics) verwaltet werden.
- [ ] Lernelemente können erstellt, aktualisiert und Themen zugeordnet werden.
- [ ] Studierende und Lehrende können Kursen zugeordnet werden.
- [ ] Verknüpfungen zwischen Kursen, Themen und Lernelementen können verwaltet und abgefragt werden.
- [ ] Abfragen nach Hochschule, Kurs-ID oder Topic-ID liefern die korrekten Entitäten zurück.

## Rationale

Die Verwaltung der Kursstruktur ist essenziell für die Funktion des adaptiven Lernsystems. Die Daten werden primär aus dem LMS synchronisiert (siehe HASKI-REQ-0078), müssen aber im HASKI-Backend persistiert und verwaltbar sein. Die Tests in `backend/tests/unit/test_service.py` verifizieren die korrekte Funktion der Service-Layer-Methoden für diese CRUD-Operationen.
