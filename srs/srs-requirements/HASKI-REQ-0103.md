---
id: HASKI-REQ-0103
title: Abruf des Bearbeitungsstatus von Learning Elements
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
links:
  parents: ["SyRS-FUNC-007"]
  stories: ["HASKI-RAK/HASKI-Frontend#263"]
  tests:
    - path: "frontend/src/services/LearningPath/fetchLearningPathElementSpecificStatus.test.tsx"
      name: "fetchLearningPathElementStatus has expected behaviour"
---

## Beschreibung

Das Frontend **shall** den Bearbeitungsstatus (Done/Not Done) eines Learning Elements vom Backend (welches diesen vom LMS abruft) abfragen können.

## Akzeptanzkriterien

- [ ] Abruf des Status für ein spezifisches Learning Element.
- [ ] Status enthält Information ob erledigt und wann.

## Rationale

Studierende müssen wissen, welche Aufgaben sie bereits erledigt haben. Dies basiert auf User Story #263.
