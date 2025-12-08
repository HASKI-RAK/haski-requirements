---
id: HASKI-REQ-0094
title: Course Enrollment and Visibility
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  stories: ["GH-131", "GH-123"]
  tests:
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
  parents: []
---

## Beschreibung

The system **shall** allow users (Students, Teachers, Course Creators) to be enrolled in courses.
The system **shall** ensure that students only see courses they are enrolled in (participating in).
The system **shall** support different roles within a course (Student, Teacher).
