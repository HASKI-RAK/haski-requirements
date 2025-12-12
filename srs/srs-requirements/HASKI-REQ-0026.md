---
id: HASKI-REQ-0026
title: Erstellung und Konfiguration von Standard-Lernpfaden mit Scaffolding-Elementen
type: Functional
status: Implemented
source_id: SyRS-FUNC-008
stakeholder_priority: Medium
verification_method: Test
links:
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#353",
      "HASKI-RAK/HASKI-Backend#84",
      "HASKI-RAK/HASKI-Frontend#309",
      "HASKI-RAK/HASKI-Frontend#308",
      "HASKI-RAK/HASKI-Backend#93",
      "HASKI-RAK/HASKI-Frontend#306",
      "HASKI-RAK/HASKI-Frontend#269",
    ]
  parents: ["SyRS-FUNC-008"]
  tests:
    # Frontend tests
    - path: "frontend/src/components/CreateDefaultLearningPath/Modal/CreateDefaultLearningPathModal.test.tsx"
      name: "CreateDefaultLearningPathModal"
    - path: "frontend/src/components/CreateDefaultLearningPath/OpenCreateDefaultLearningPath/OpenCreateDefaultLearningPath.test.tsx"
      name: "OpenCreateDefaultLearningPath"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/CreateDefaultLearningPathTable.test.tsx"
      name: "CreateDefaultLearningPathTable"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/CreateDefaultLearningPathTable.hooks.test.tsx"
      name: "useCreateDefaultLearningPathTable"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/DraggableItem.test.tsx"
      name: "DraggableItem Component"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/DroppableItem.test.tsx"
      name: "Droppable Component"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/SortableItem.test.tsx"
      name: "SortableItem Component"
    - path: "frontend/src/services/DefaultLearningPath/fetchDefaultLearningPath.test.tsx"
      name: "fetchDefaultLearningPath has expected behaviour"
    - path: "frontend/src/store/Slices/DefaultLearningPathSlice.test.ts"
      name: "DefaultLearningPathSlice caching"
    - path: "frontend/src/services/DefaultLearningPath/fetchDisabledClassifications.test.tsx"
      name: "fetchDisabledClassifications has expected behaviour"
    - path: "frontend/src/services/DefaultLearningPath/postDefaultLearningPath.test.tsx"
      name: "postDefaultLearningPath has expected behaviour"
    - path: "frontend/src/services/LearningPath/postCalculateLearningPathForAllStudents.test.tsx"
      name: "postCalculateLearningPathForAllStudents"
    # Backend e2e tests
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_learning_path_default"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_default"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_calculate_learning_path_for_all_students"
    # Backend unit tests
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_default_learning_path"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_default_learning_path_by_university"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_default_learning_path_by_uni"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_get_learning_path_default"
---

## Beschreibung

Das System **shall** Lehrenden die Möglichkeit bieten, konfigurierbare Standard-Lernpfade mit Scaffolding-Elementen zu erstellen, zu bearbeiten und zu verwalten. Der Standard-Lernpfad dient als Grundlage für alle studentischen Lernpfade innerhalb eines Themas und kann mit verschiedenen Algorithmen (z.B. Graph, ACO) zur Personalisierung kombiniert werden.

## Akzeptanzkriterien

### Erstellung und Verwaltung von Standard-Lernpfaden

- [x] Lehrende können einen Standard-Lernpfad für das HASKI-System erstellen
- [x] Wenn kein Standard-Lernpfad gesetzt ist, wird der erste Kursersteller aufgefordert, einen zu erstellen
- [x] Lehrende können einen bestehenden Standard-Lernpfad aktualisieren
- [x] Die Aktualisierung eines Standard-Lernpfads löst eine Neuberechnung aller abhängigen studentischen Lernpfade aus (GH-84)

### Konfiguration von Scaffolding-Elementen

- [x] Standardmäßig ist der Lernpfad in der von Lehrenden definierten Reihenfolge (prof-standard) organisiert
- [x] Lehrende können für jedes Thema und Unter-Thema spezifische Algorithmen auswählen (z.B. Graph, ACO)
- [x] Die gewählten Algorithmus-Einstellungen werden auf alle Lernpfade der Studierenden angewendet

### Technische Anforderungen

- [x] Backend-Endpunkte für CRUD-Operationen auf Standard-Lernpfaden sind implementiert
- [x] Datenbankstruktur unterstützt Speicherung von Standard-Lernpfaden und deren Konfiguration
- [x] Rollenbasierte Zugriffskontrolle stellt sicher, dass nur autorisierte Lehrende Lernpfade konfigurieren können
- [x] Frontend-Benutzeroberfläche ermöglicht intuitive Erstellung und Bearbeitung von Lernpfaden

## Rationale

Primary implementation: GitHub issue GH-353: "Teacher can create a Default Learning Path"

Related work:

- GH-84 (Backend): Implementiert Backend-Infrastruktur mit Datenbanktabellen und API-Endpunkten für Standard-Lernpfade
- GH-306 (Frontend): Ermöglicht Auswahl von Algorithmen für Themen, was die Scaffolding-Konfiguration unterstützt

Derived from system requirement SyRS-FUNC-008 and stakeholder requirement StRS-110.

Die Konfigurierbarkeit von Lernräumen mit Scaffolding-Elementen ermöglicht Lehrenden, Lernumgebungen flexibel an unterschiedliche Lernstände und didaktische Konzepte anzupassen. Der Standard-Lernpfad bildet dabei die Grundstruktur, die durch adaptive Algorithmen personalisiert werden kann.

## Hinweise

- Primary issue: [GH-353](https://github.com/HASKI-RAK/HASKI-Frontend/issues/353)
- Related issues:
  - [GH-84](https://github.com/HASKI-RAK/HASKI-Backend/issues/84) - Backend implementation
  - [GH-306](https://github.com/HASKI-RAK/HASKI-Frontend/issues/306) - Algorithm selection UI
- Backend erfordert neue Datenbanktabellen für Speicherung von Standard-Lernpfaden
- API-Endpunkte müssen rollenbasierte Zugriffsrechte implementieren (nur Lehrende/Tutoren)
- Startup-Skripte müssen DB korrekt initialisieren
- Unit-Test-Abdeckung muss > 90% sein
