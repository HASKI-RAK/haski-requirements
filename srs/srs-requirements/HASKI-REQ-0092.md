---
id: HASKI-REQ-0092
title: Automatische Benutzer-Provisionierung
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-001
links:
  stories: ["HASKI-RAK/HASKI-Backend#81"]
  parents: ["SyRS-FUNC-001"]
  tests:
    tests:
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_admin"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_course_creator"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_settings"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_student"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_empty_user_by_lms_id"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_user_by_lms_id"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_teacher"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_user"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_learning_characteristics"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_learning_style"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_learning_strategy"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_knowledge"
      - path: "backend/tests/unit/test_service.py"
        name: "test_create_learning_analytics"
      - path: "backend/tests/unit/test_service.py"
        name: "test_get_learning_characteristics"
---

    - path: "backend/tests/unit/test_service.py"
      name: "test_get_user_by_admin"

---

## Beschreibung

Das System **shall** Benutzerkonten und zugehörige Profil-Tabellen automatisch anlegen, wenn sich ein Benutzer zum ersten Mal über LTI authentifiziert und noch kein Konto existiert. Dieser Provisionierungsprozess **shall** sicherstellen, dass alle für den adaptiven Lernprozess notwendigen Datenstrukturen initialisiert sind, bevor der Benutzer auf das System zugreift.

Der Prozess umfasst die Initialisierung folgender Entitäten:

- `User` (Basis-Benutzerdaten aus LTI-Launch)
- `Settings` (Benutzerspezifische Einstellungen)
- `Student` (Rollenspezifische Daten, falls Rolle Student)
- `LearningCharacteristics` (Lernmerkmale)
- `LearningStyle` (Lernstil-Präferenzen, initialisiert mit Standardwerten)
- `Knowledge` (Wissensstand)
- `LearningAnalytics` (Lernfortschrittsdaten)
- `LearningStrategy` (Lernstrategien)
- `StudentCourse` (Verknüpfung zum Kurs)

## Akzeptanzkriterien

- [ ] `create_user` legt einen neuen Benutzer an, wenn dieser noch nicht existiert.
- [ ] `create_student` initialisiert die Studenten-Rolle und verknüpft sie mit dem Benutzer.
- [ ] Alle abhängigen Tabellen (`LearningCharacteristics`, `LearningStyle`, `Knowledge`, `LearningAnalytics`, `LearningStrategy`) werden mit validen Standardwerten initialisiert.
- [ ] Die Integrität der Verknüpfungen (Foreign Keys) ist gewährleistet.
- [ ] Der Vorgang ist idempotent oder prüft auf Existenz, um Duplikate zu vermeiden.

## Rationale

GitHub Issue #81 fordert: "User and according Tables get created automatically, when user logs in without an existing account in HASKI". Dies ist essenziell für ein nahtloses Onboarding ohne manuellen Administrationsaufwand. Die Tests in `backend/tests/unit/test_service.py` verifizieren die korrekte Erstellung und Initialisierung dieser Entitäten.
