---
id: HASKI-REQ-0011
title: Bereitstellung von Micro-Learning-Einheiten
type: Functional
status: Implemented
source_id: SyRS-FUNC-005
links:
  stories: []
  parents: [SyRS-FUNC-005]
---

## Beschreibung

Das System **shall** Lerninhalte als atomare, kombinierbare Micro-Learning-Einheiten bereitstellen, wobei jede Lerneinheit (Learning Element) so gestaltet ist, dass sie innerhalb von maximal 10 Minuten bearbeitet werden kann.

## Akzeptanzkriterien

- [ ] Alle Learning Element-Typen im System sind auf eine maximale Bearbeitungszeit von 10 Minuten ausgelegt
- [ ] Learning Elements können unabhängig voneinander abgerufen und bearbeitet werden (atomare Einheiten)
- [ ] Learning Elements können zu Lernpfaden kombiniert werden (kombinierbar)
- [ ] Das System unterstützt verschiedene Learning Element-Typen (Text, Video, Quiz, interaktive Elemente, etc.)
- [ ] Jedes Learning Element hat einen definierten Umfang, der Micro-Learning-Prinzipien entspricht
- [ ] Learning Elements sind in Topics organisiert und können flexibel angeordnet werden

## Rationale

Diese Anforderung implementiert das Micro-Learning-Prinzip als fundamentales Designprinzip des HASKI-Systems. Die 10-Minuten-Grenze ermöglicht es Studierenden, Lerninhalte flexibel in ihren Alltag zu integrieren und unterstützt nachhaltiges Lernen durch fokussierte, überschaubare Lerneinheiten.

Die atomare Struktur erlaubt:
- Flexible Zusammenstellung von Lernpfaden
- Wiederverwendung von Lerninhalten
- Adaptive Anpassung an individuelle Lernbedürfnisse
- Integration in verschiedene Lernszenarien

Abgeleitet von Systemanforderung SyRS-FUNC-005 und Stakeholder-Anforderung StRS-107.

## Hinweise

- Die 10-Minuten-Grenze ist eine Designrichtlinie für Content-Ersteller, keine technisch durchgesetzte Beschränkung
- Bezieht sich auf alle im System verfügbaren Learning Element-Typen
- Unterstützt durch die Learning Element-Architektur, wie in den folgenden Issues implementiert:
  - Verschiedene Learning Element-Metadaten (Difficulty, Tags, Descriptions)
  - Learning Element-Tracking (Last-Viewed, Done-Date, Time-Spent)
  - Learning Element-Organisation (Topics, Learning Paths, Associations)
- Verwandte technische Umsetzung in Frontend- und Backend-Komponenten für Learning Element-Management
