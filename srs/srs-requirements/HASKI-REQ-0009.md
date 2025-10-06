---
id: HASKI-REQ-0009
title: Unmittelbares Feedback zu Aufgaben
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: [SyRS-FUNC-003]
  stories: ["NodeGrade#10", "NodeGrade#11", "NodeGrade#9", "NodeGrade#19", "NodeGrade#37", "NodeGrade#40"]
  tests: []
---

## Beschreibung
Das System **shall** Studierenden unmittelbar nach der Abgabe von Aufgaben verständliches Feedback bereitstellen, das folgende Aufgabentypen abdeckt:

- **Quiz-Aufgaben**: Automatische Bewertung mit Ergebnisanzeige
- **Freitextaufgaben**: KI-gestütztes Feedback zu frei formulierten Antworten
- **Code-Aufgaben**: Bewertung und Rückmeldung zu Programmieraufgaben
- **Diagrammaufgaben**: Feedback zu grafischen und diagrammatischen Lösungen

## Rationale
Unmittelbares Feedback ist ein zentraler Bestandteil wirksamen Lernens (formative Assessment). Studierende benötigen zeitnahe, präzise und verständliche Rückmeldungen, um:
- Fehler zu erkennen und zu korrigieren
- Lernfortschritte zu reflektieren
- Motivation und Selbstwirksamkeit zu fördern
- Die Abhängigkeit von manueller Korrekturbewertung zu reduzieren

Das NodeGrade-System ermöglicht automatisierte Bewertungen mittels konfigurierbarer Workflows und LLM-basierter Textanalyse, wodurch sowohl strukturierte als auch offene Aufgabenformate unterstützt werden.

## Akzeptanzkriterien
1. **Unmittelbarkeit**: Feedback wird innerhalb akzeptabler Ladezeiten (< 10 Sekunden für einfache Aufgaben, < 60 Sekunden für komplexe LLM-Analysen) nach Abgabe angezeigt
2. **Verständlichkeit**: Feedback ist in natürlicher Sprache formuliert und enthält:
   - Bewertungsergebnis (Punkte, Prozentsatz oder qualitative Einschätzung)
   - Spezifische Hinweise zu Stärken und Schwächen der Lösung
   - Konstruktive Verbesserungsvorschläge
3. **Aufgabentypen-Abdeckung**:
   - Quiz: Sofortige richtig/falsch-Bewertung
   - Freitext: Semantische Analyse mit Keyword-Erkennung und LLM-Bewertung
   - Code: Syntaxprüfung, Testausführung oder regelbasierte Bewertung
   - Diagramme: Strukturelle oder inhaltliche Bewertung (je nach Implementierung)
4. **Feedbackqualität**: Studierende können bei Unklarheiten Rückfragen zum Feedback stellen (Issue #40)
5. **Transparenz**: Bewertungskriterien sind für Studierende nachvollziehbar

## Implementierungshinweise
- **NodeGrade-System** (https://github.com/HASKI-RAK/NodeGrade) wird als LTI-Tool in Moodle integriert
- Workflow-basierte Evaluation mit konfigurierbaren Nodes (LLM, Feedback Output, Answer Input)
- Lehrende erstellen Bewertungsgraphen über grafische Oberfläche
- Unterstützung für Musterantworten und mehrstufige Bewertungskriterien
- LTI 1.3 Integration für Rollenverwaltung und Ergebnisübermittlung

## Abhängigkeiten
- NodeGrade-Deployment und LTI-Konfiguration
- Moodle-Integration (LTI 1.3)
- LLM-Infrastruktur für Freitextbewertung (z.B. DeepSeek, lokale Modelle)
- Learning Analytics (LRS) für Tracking der Feedbacknutzung (optional, Issue #12)

## Verifikation
- **Test**: Automatisierte Tests für verschiedene Aufgabentypen und Antwortszenarien
- **Demonstration**: Pilotveranstaltungen mit Studierenden-Feedback zur Verständlichkeit
- **Analyse**: Messung der Feedbackqualität (Präzision, Hilfsbereitschaft) durch Nutzerbefragungen

