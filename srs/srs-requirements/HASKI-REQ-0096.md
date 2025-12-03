---
id: HASKI-REQ-0096
title: Default Learning Paths
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
links:
  stories: ["GH-84"]
  tests:
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_default_learning_path"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_default_learning_path_by_university"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_default_learning_path_by_uni"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_get_learning_path_default"
  parents: []
---

## Beschreibung

The system **shall** allow the creation and management of default learning paths for topics.
These default paths serve as a fallback or template when adaptive generation is not applicable or desired.
The system **shall** allow defining default paths per university/institution if needed.
