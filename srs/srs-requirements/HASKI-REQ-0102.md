---
id: HASKI-REQ-0102
title: Anzeige empfohlener Learning Elements
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-FUNC-001"]
  stories: ["HASKI-RAK/HASKI-Frontend#362"]
  tests:
    - path: "frontend/src/services/LearningElementRecommendation/LearningElementRecommendation.test.tsx"
      name: "LearningElementRecommendation"
    - path: "frontend/src/services/LearningElementRecommendation/fetchLearningElementRecommendation.test.ts"
      name: "fetchLearningElementRecommendation"
---

## Beschreibung

Das Frontend **shall** dem Studierenden basierend auf den vom Backend gelieferten Empfehlungen das nächste zu bearbeitende Learning Element anzeigen.

## Akzeptanzkriterien

- [ ] Abruf der Empfehlungsdaten vom Backend.
- [ ] Anzeige der empfohlenen Übung im Lernpfad.
- [ ] Wenn keine Empfehlung vorhanden ist, wird dies entsprechend behandelt (z.B. keine Anzeige).

## Rationale

Studierende sollen im adaptiven Modus geführt werden und wissen, was der nächste sinnvolle Schritt ist. Dies basiert auf User Story #362.
