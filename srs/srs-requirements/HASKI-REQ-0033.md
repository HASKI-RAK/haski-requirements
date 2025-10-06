---
id: HASKI-REQ-0033
title: Automatisierte Bewertung von Freitextantworten
type: Functional
status: Implemented
source_id: SyRS-FUNC-006
links:
  stories: ["GH-10", "GH-9", "GH-11", "GH-26", "GH-22", "GH-37"]
  parents: ["SyRS-FUNC-006"]
---

## Beschreibung

Das System **shall** automatisierte Bewertung für Freitextaufgaben durchführen, indem es Studierendenantworten analysiert und unmittelbar Feedback mit Bewertungsergebnissen bereitstellt.

Das System **shall** die automatisierte Bewertung innerhalb akzeptabler Ladezeiten durchführen und die Ergebnisse im Eingabeformular anzeigen.

Das System **shall** spezifisches, auf die Aufgabe zugeschnittenes Feedback bereitstellen, das Studierenden aufzeigt, was verbessert werden muss.

## Akzeptanzkriterien

### Eingabe und Verarbeitung
- [x] Eingabeformular für mehrzeilige Freitextantworten (siehe [GH-9](https://github.com/HASKI-RAK/NodeGrade/issues/9))
- [x] Übermittlung der Studierendenantworten zur automatisierten Bewertung
- [x] Feedback zur erfolgreichen Übermittlung

### Bewertung und Ergebnisanzeige  
- [x] Ergebnis wird im Eingabeformular angezeigt (siehe [GH-10](https://github.com/HASKI-RAK/NodeGrade/issues/10))
- [ ] Ladeindikator während der Bewertung
- [x] Akzeptable Ladezeiten für die Bewertung

### Feedback-Qualität
- [ ] Feedback ist auf die spezifische Aufgabe zugeschnitten (siehe [GH-11](https://github.com/HASKI-RAK/NodeGrade/issues/11))
- [ ] Hinweise, was verbessert werden kann
- [ ] Darstellung der Bewertungsergebnisse

### Bewertungsmethoden
- [x] Schlüsselwort-basierte Bewertung: Rating basierend auf dem Verhältnis vorhandener Schlüsselwörter in der Studierendenantwort (siehe [GH-26](https://github.com/HASKI-RAK/NodeGrade/issues/26))
- [x] LLM-basierte Bewertung: Integration von Large Language Models zur semantischen Analyse (siehe [GH-22](https://github.com/HASKI-RAK/NodeGrade/issues/22))
- [ ] Präzises Feedback durch LLM-gestützte Analyse (siehe [GH-37](https://github.com/HASKI-RAK/NodeGrade/issues/37))

## Rationale

Primary implementation: GitHub issue [GH-10: Feedback on TA Result](https://github.com/HASKI-RAK/NodeGrade/issues/10)

Related work:
- [GH-9: Submit freeform answer](https://github.com/HASKI-RAK/NodeGrade/issues/9) - Grundlage für Freitexteingabe
- [GH-11: TA correcting Feedback](https://github.com/HASKI-RAK/NodeGrade/issues/11) - Qualitatives Feedback mit Verbesserungshinweisen
- [GH-26: Keywords](https://github.com/HASKI-RAK/NodeGrade/issues/26) - Schlüsselwort-basierter Bewertungsalgorithmus
- [GH-22: LLM Node](https://github.com/HASKI-RAK/NodeGrade/issues/22) - LLM-Integration für semantische Bewertung
- [GH-37: Demo Graph for precise feedback](https://github.com/HASKI-RAK/NodeGrade/issues/37) - Präzisierung des LLM-Feedbacks

Derived from system requirement SyRS-FUNC-006.

Diese SRS-Anforderung fokussiert sich auf die **Freitextbewertung**, da das NodeGrade-Repository primär für die automatisierte Bewertung von Kurzantworten (Short Answer Grading) mittels LLM-basierter Workflows entwickelt wurde. Die im SyRS-FUNC-006 genannten weiteren Aufgabentypen (Quiz, Code, Diagramme) erfordern separate Implementierungen und SRS-Anforderungen.

## Hinweise

- Primary issue: [GH-10](https://github.com/HASKI-RAK/NodeGrade/issues/10)
- Related issues: [GH-9](https://github.com/HASKI-RAK/NodeGrade/issues/9), [GH-11](https://github.com/HASKI-RAK/NodeGrade/issues/11), [GH-26](https://github.com/HASKI-RAK/NodeGrade/issues/26), [GH-22](https://github.com/HASKI-RAK/NodeGrade/issues/22), [GH-37](https://github.com/HASKI-RAK/NodeGrade/issues/37)
- Repository: [HASKI-RAK/NodeGrade](https://github.com/HASKI-RAK/NodeGrade)
- Die automatisierte Bewertung nutzt einen workflow-basierten Ansatz mit konfigurierbaren Bewertungsgraphen
- Unterstützt sowohl regelbasierte (Schlüsselwörter) als auch LLM-basierte Bewertungsverfahren
- Integration mit LTI (Learning Tools Interoperability) für nahtlose Einbettung in Learning Management Systeme
