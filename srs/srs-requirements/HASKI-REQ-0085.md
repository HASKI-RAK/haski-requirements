---
id: HASKI-REQ-0085
title: Visualisierung des Lernelement-Lernpfads im Frontend
type: Interface
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-008
links:
  parents: ["SyRS-FUNC-008"]
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#66",
      "HASKI-RAK/HASKI-Frontend#141",
      "HASKI-RAK/HASKI-Frontend#257",
      "HASKI-RAK/HASKI-Frontend#276",
      "HASKI-RAK/HASKI-Frontend#306",
    ]
  tests:
    - path: "frontend/src/components/LabeledSwitch/LabeledSwitch.test.tsx"
      name: "LabeledSwitch Component"
    - path: "frontend/src/components/Nodes/BasicNode/BasicNode.test.tsx"
      name: "BasicNode"
    - path: "frontend/src/components/BorderedPaper/BorderedPaper.test.tsx"
      name: "BorderedPaper"
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
    - path: "frontend/src/pages/ThemePresentation/LearningElementLearningPath.test.tsx"
      name: "LearningElementLearningPath tests"
    - path: "frontend/src/pages/ThemePresresentation/TopicsLearningPath.test.tsx"
      name: "TopicsLearningPath"
    - path: "frontend/src/services/LearningPath/fetchLearningPathElement.test.tsx"
      name: "fetchLearningPathElement has expected behaviour"
    - path: "frontend/src/services/LearningPath/fetchLearningPathElementStatus.test.tsx"
      name: "fetchLearningPathElementStatus has expected behaviour"
    - path: "frontend/src/services/LearningPath/postCalculateLearningPathForAllStudents.test.tsx"
      name: "postCalculateLearningPathForAllStudents has expected behaviour"
    - path: "frontend/src/services/LearningPath/postCalculateLearningPathILS.test.tsx"
      name: "postCalculateLearningPathILS tests"
    - path: "frontend/src/services/Topic/fetchLearningPathTopic.test.tsx"
      name: "fetchLearningPathElement has expected behaviour"
    - path: "frontend/src/store/Slices/LearningPathTopicSlice.test.ts"
      name: "LearningPathTopicSlice caching"
---

## Beschreibung

Das Frontend **shall** den Standard-Lernpfad eines Topics als interaktives Node-Graph-Layout darstellen. Jede Lernaktivität wird als Klassifikations-spezifischer Node mit Icon, Status (offen, erledigt, deaktiviert, empfohlen) und Klick-Interaktion visualisiert. Studierende sollen ihre individuellen Lernelemente als Knoten sehen, verbunden durch Kanten, die die empfohlene oder vorgeschriebene Reihenfolge darstellen. Lehrende und Studierende **shall** zwischen gruppierter und ungeordneter Darstellung wechseln können, ohne dass Daten neu geladen werden müssen. Die Visualisierung **shall** als Single Source of Truth für Lernpfad-Interaktionen dienen und unmittelbar auf Änderungen reagieren, die aus Backend-Synchronisationen stammen.

## Akzeptanzkriterien

### Grundlegende Darstellung

- [x] Der Lernpfad wird als Graph mit Knoten (Lernelemente) und Kanten (Verbindungen) dargestellt.
- [x] Der Status der Lernelemente (erledigt, offen, gesperrt) wird visuell hervorgehoben.
- [x] Lernelemente mit gleicher Klassifikation (z.B. mehrere Übungen) werden gruppiert dargestellt (GH-276).
- [x] Ein Klick auf ein Lernelement öffnet dieses (z.B. in einem Modal oder IFrame).
- [x] Die Ansicht unterscheidet sich je nach Rolle (Studierende sehen ihren Fortschritt, Lehrende sehen eine Vorschau oder Bearbeitungsansicht).
- [x] Fehler beim Laden der Daten (User, Lernpfad, Status) werden abgefangen und dem Nutzer gemeldet.

### Node-Darstellung

- [x] Für jede unterstützte Lernaktivitäts-Klassifikation (z.B. Beispiel, Feedback, Selbsttest) existiert ein eigener Node-Typ mit passendem Icon gemäß Projektdesign.
- [x] Nodes zeigen den Bearbeitungsstatus (done/disabled/recommended) über Farbe, Rahmen oder Symbolik konsistent an.
- [x] Ein Klick auf einen Node öffnet das zugehörige Lern- oder Verwaltungs-Modal (z.B. IFrame, Delete-Dialog) mit den hinterlegten Metadaten.

### Layout und Interaktion

- [x] Die Lernpfad-Darstellung nutzt ReactFlow mit Stable Layouting und Drag-Blocking, sodass die Reihenfolge der Aktivitäten erhalten bleibt.
- [x] Ein Toggle erlaubt den Wechsel zwischen gruppierter und linearer Ansicht (z.B. "Grouped" vs. "Single"), ohne dass ReactFlow neu initialisiert wird.
- [x] Tooltipps, Kontextmenüs oder Modals für Einstellungen (z.B. Algorithmuswechsel, Delete) funktionieren aus jeder Ansicht heraus und schließen konsistent.

### Status- und Icon-Verwaltung

- [x] Die `getNodeIcon`-Utility liefert für jede Klassifikation ein passendes Material-Icon und wird zentral durch die NodeTypes-Registry verifiziert.
- [x] Neue Klassifikationen können über die Registry eingebunden werden, ohne den Rendering-Flow zu brechen (z.B. Additional Literature für AB/FO/LZ aus GH-257).
- [x] Fehlende Daten (z.B. Topic ohne Learning Elements) führen zu einer robusten, aber leeren Darstellung anstatt zu Fehlern.

## Rationale

Die Visualisierung des Lernpfads ist das zentrale Element für die Orientierung der Studierenden. Sie macht den Lernfortschritt transparent und ermöglicht die Navigation durch die Inhalte. SyRS-FUNC-008 verlangt eine durchgängige Visualisierung der adaptiven Lernräume. GitHub Issue [#66](https://github.com/HASKI-RAK/HASKI-Frontend/issues/66) definiert die Node-Graph-Darstellung als Kernfunktion des Topic-Frontends. Issue [#141](https://github.com/HASKI-RAK/HASKI-Frontend/issues/141) beschreibt die Learning-Path-Komponente, die Lernelemente rendert. Issue [#257](https://github.com/HASKI-RAK/HASKI-Frontend/issues/257) erweitert die Node-Typen, um standortspezifische Klassifikationen abzubilden, Issue [#276](https://github.com/HASKI-RAK/HASKI-Frontend/issues/276) definiert die Gruppierung von Lernelementen, und Issue [#306](https://github.com/HASKI-RAK/HASKI-Frontend/issues/306) verknüpft die Visualisierung mit Algorithmus-Overrides. Zusammen stellen die verlinkten Komponenten sicher, dass die Lernpfad-Oberfläche sämtliche Klassifikationen und Statuszustände konsistent im Frontend abbildet.

## Hinweise

- Die Visualisierung basiert auf ReactFlow und den Memo-optimierten Node-Komponenten unter `frontend/src/components/Nodes/`.
- Nutzt `useTopic` Hook für die Logik.
- LabeledSwitch erlaubt Lehrenden und Studierenden, den Graph bedarfsgerecht umzuschalten (Grouped vs. Single view).
- Node-spezifische Modals (Algorithmus, Delete-Dialoge) stammen aus den jeweiligen Komponenten und sind für die Interaktionskette relevant.
- Styling und Icons folgen den Vorgaben in `assets/css/rtm.css` und den Material Icons, wodurch Barrierefreiheit (Kontrast, Fokus) gewährleistet bleibt.
