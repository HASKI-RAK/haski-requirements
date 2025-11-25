---
id: HASKI-REQ-0026
title: Erstellung und Konfiguration von Standard-Lernpfaden mit Scaffolding-Elementen
type: Functional
status: Implemented
source_id: SyRS-FUNC-008
links:
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#353",
      "HASKI-RAK/HASKI-Backend#84",
      "HASKI-RAK/HASKI-Frontend#309",
      "HASKI-RAK/HASKI-Frontend#308",
      "HASKI-RAK/HASKI-Backend#93",
      "HASKI-RAK/HASKI-Frontend#306",
      "HASKI-RAK/HASKI-Frontend#66",
      "HASKI-RAK/HASKI-Frontend#269",
      "HASKI-RAK/HASKI-Frontend#257",
    ]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "frontend/src/components/CreateTopic/Table/CreateAlgorithm/CreateAlgorithmTable.test.tsx"
      name: "CreateAlgorithmTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElementClassification/CreateLearningElementClassificationTable.test.tsx"
      name: "CreateLearningElementClassificationTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElement/CreateLearningElementTable.test.tsx"
      name: "CreateLearningElementTable"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/CreateDefaultLearningPathTable.test.tsx"
      name: "CreateDefaultLearningPathTable"
    - path: "frontend/src/components/CreateDefaultLearningPath/Table/CreateDefaultLearningPathTable.hooks.test.tsx"
      name: "useCreateDefaultLearningPathTable"
    - path: "frontend/src/components/CreateLearningElement/CreateLearningElement.test.tsx"
      name: "CreateLearningElement Component"
    - path: "frontend/src/components/CreateLearningElement/CreateLearningElementModal.test.tsx"
      name: "CreateLearningElementModal Component"
    - path: "frontend/src/components/CreateTopic/Modal/CreateTopicModal/CreateTopicModal.test.tsx"
      name: "CreateTopicModal"
    - path: "frontend/src/components/CreateTopic/Modal/CreateTopicModal/CreateTopicModal.hooks.test.tsx"
      name: "useCreateTopicModal"
    - path: "frontend/src/components/CreateTopic/Modal/CreateAlgorithmsStep/CreateAlgorithmsStep.test.tsx"
      name: "CreateAlgorithmsStep"
    - path: "frontend/src/components/CreateTopic/Modal/CreateLearningElementClassificationsStep/CreateLearningElementClassificationsStep.test.tsx"
      name: "CreateLearningElementClassificationsStep"
    - path: "frontend/src/components/CreateTopic/Modal/CreateLearningElementsStep/CreateLearningElementsStep.test.tsx"
      name: "CreateLearningElementsStep"
    - path: "frontend/src/components/CreateTopic/Modal/CreateRemoteTopicsStep/CreateRemoteTopicsStep.test.tsx"
      name: "CreateRemoteTopicsStep"
    - path: "frontend/src/pages/Course/Course.test.tsx"
      name: "Course Page"
    - path: "frontend/src/components/Filter/Filter.test.tsx"
      name: "Filter Component"
    - path: "frontend/src/components/TopicCard/TopicCard.test.tsx"
      name: "TopicCard Component"
    - path: "frontend/src/components/ImageCollection/ImageCollection.test.tsx"
      name: "ImageCollection Component"
    - path: "frontend/src/components/LabeledSwitch/LabeledSwitch.test.tsx"
      name: "LabeledSwitch Component"
    - path: "frontend/src/components/Nodes/BasicNode/BasicNode.test.tsx"
      name: "BasicNode"
    - path: "frontend/src/components/Nodes/AdditionalLiteratureNode/AdditionalLiteratureNode.test.tsx"
      name: "AdditionalLiteratureNode"
    - path: "frontend/src/components/Nodes/ApplicationExampleNode/ApplicationExampleNode.test.tsx"
      name: "ApplicationExampleNode"
    - path: "frontend/src/components/Nodes/DefaultGroup/DefaultGroup.test.tsx"
      name: "DefaultGroup"
    - path: "frontend/src/components/Nodes/EvaluationQuestionnaireNode/EvaluationQuestionnaireNode.test.tsx"
      name: "EvaluationQuestionnaireNode"
    - path: "frontend/src/components/Nodes/ExampleNode/ExampleNode.test.tsx"
      name: "ExampleNode"
    - path: "frontend/src/components/Nodes/ExerciseNode/ExerciseNode.test.tsx"
      name: "ExerciseNode"
    - path: "frontend/src/components/Nodes/ExplanationNode/ExplanationNode.test.tsx"
      name: "ExplanationNode"
    - path: "frontend/src/components/Nodes/FeedbackNode/FeedbackNode.test.tsx"
      name: "FeedbackNode"
    - path: "frontend/src/components/Nodes/ForumNode/ForumNode.test.tsx"
      name: "ForumNode"
    - path: "frontend/src/components/Nodes/LearningObjectiveNode/LearningObjectiveNode.test.tsx"
      name: "LearningObjectiveNode"
    - path: "frontend/src/components/Nodes/SelfAssessmentNode/SelfAssessmentNode.test.tsx"
      name: "SelfAssessmentNode"
    - path: "frontend/src/components/Nodes/ShortTextualIntroductionNode/ShortTextualIntroductionNode.test.tsx"
      name: "ShortTextualIntroductionNode"
    - path: "frontend/src/components/Nodes/SummaryNode/SummaryNode.test.tsx"
      name: "SummaryNode"
    - path: "frontend/src/components/Nodes/VideoNode/VideoNode.test.tsx"
      name: "VideoNode"
    - path: "frontend/src/components/Nodes/NodeTypes/NodeTypes.test.tsx"
      name: "NodeTypes (getNodeIcon)"
    - path: "frontend/src/pages/Topic/Topic.test.tsx"
      name: "Topic Page"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_teacher_learning_path_learning_element_algorithm"
---

## Beschreibung

Das System **shall** Lehrenden die Möglichkeit bieten, konfigurierbare Standard-Lernpfade mit Scaffolding-Elementen zu erstellen, zu bearbeiten und zu verwalten. Der Standard-Lernpfad dient als Grundlage für alle studentischen Lernpfade innerhalb eines Themas und kann mit verschiedenen Algorithmen (z.B. Graph, ACO) zur Personalisierung kombiniert werden.

## Akzeptanzkriterien

### Erstellung und Verwaltung von Standard-Lernpfaden

- [ ] Lehrende können einen Standard-Lernpfad für das HASKI-System erstellen
- [ ] Wenn kein Standard-Lernpfad gesetzt ist, wird der erste Kursersteller aufgefordert, einen zu erstellen
- [ ] Lehrende können einen bestehenden Standard-Lernpfad aktualisieren
- [ ] Die Aktualisierung eines Standard-Lernpfads löst eine Neuberechnung aller abhängigen studentischen Lernpfade aus

### Konfiguration von Scaffolding-Elementen

- [ ] Standardmäßig ist der Lernpfad in der von Lehrenden definierten Reihenfolge (prof-standard) organisiert
- [ ] Lehrende können für jedes Thema und Unter-Thema spezifische Algorithmen auswählen (z.B. Graph, ACO)
- [ ] Die gewählten Algorithmus-Einstellungen werden auf alle Lernpfade der Studierenden angewendet

### Technische Anforderungen

- [ ] Backend-Endpunkte für CRUD-Operationen auf Standard-Lernpfaden sind implementiert
- [ ] Datenbankstruktur unterstützt Speicherung von Standard-Lernpfaden und deren Konfiguration
- [ ] Rollenbasierte Zugriffskontrolle stellt sicher, dass nur autorisierte Lehrende Lernpfade konfigurieren können
- [ ] Frontend-Benutzeroberfläche ermöglicht intuitive Erstellung und Bearbeitung von Lernpfaden

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
