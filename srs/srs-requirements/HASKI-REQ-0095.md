---
id: HASKI-REQ-0095
title: Adaptive Learning Path Generation
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  stories: ["GH-1", "GH-2", "GH-6", "GH-8", "GH-22", "GH-23", "GH-24", "GH-76"]
  tests:
    - path: "backend/tests/unit/test_service.py"
      name: "test_student_learning_element_visit"
    - path: "backend/tests/unit/test_service.py"
      name: "test_student_topic_visit"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_path"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_learning_paths_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_knowledge_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_analytics_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_path"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_knowledge_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_learning_analytics_by_student_id"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_aco"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_distance"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_get_coordinates"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_tyche"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_nestor"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_training_nestor"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_with_out_of_range_learning_style_for_ga"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_learning_style_check"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_calculate_variable_score_graf"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_ga_2"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_ga"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_ga_for_all"
  parents: []
---

## Beschreibung

The system **shall** generate adaptive learning paths for students based on selected algorithms (e.g., ACO, Graph-based).
The system **shall** store the generated learning paths.
The system **shall** allow retrieving the generated learning path for a student in a specific course/topic.
The system **shall** allow deleting learning paths for a student (e.g., for regeneration).
