---
id: HASKI-REQ-0011
title: Bereitstellung von Micro-Learning-Einheiten
type: Functional
status: Implemented
source_id: SyRS-FUNC-005
links:
  stories: ["GH-Frontend#3", "GH-Frontend#4", "GH-Frontend#135", "GH-Frontend#139", "GH-Frontend#190", "GH-Frontend#211", "GH-Frontend#263", "GH-Frontend#264", "GH-Frontend#269", "GH-Frontend#315", "GH-Frontend#331", "GH-Backend#100", "GH-Backend#120", "GH-Backend#121"]
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

### Moodle Activity Type Support
Das System unterstützt verschiedene Moodle-Aktivitätstypen als Micro-Learning-Einheiten:
- **H5P** (Interactive Content): [Frontend#139](https://github.com/HASKI-RAK/HASKI-Frontend/issues/139), [Frontend#190](https://github.com/HASKI-RAK/HASKI-Frontend/issues/190), [Frontend#211](https://github.com/HASKI-RAK/HASKI-Frontend/issues/211), [Frontend#315](https://github.com/HASKI-RAK/HASKI-Frontend/issues/315)
- **Feedback/Questionnaires**: [Frontend#3](https://github.com/HASKI-RAK/HASKI-Frontend/issues/3), [Frontend#269](https://github.com/HASKI-RAK/HASKI-Frontend/issues/269), [Backend#100](https://github.com/HASKI-RAK/HASKI-Backend/issues/100)
- **Quiz**: Completion tracking and progress monitoring via [Frontend#263](https://github.com/HASKI-RAK/HASKI-Frontend/issues/263), [Frontend#264](https://github.com/HASKI-RAK/HASKI-Frontend/issues/264)
- **Label Activities**: [Frontend#4](https://github.com/HASKI-RAK/HASKI-Frontend/issues/4)
- **General Activity Types**: User learning path setting via [Frontend#331](https://github.com/HASKI-RAK/HASKI-Frontend/issues/331)

### Content Integration
- Moodle-Kurse werden als Template für HASKI-Kurse verwendet: [Frontend#135](https://github.com/HASKI-RAK/HASKI-Frontend/issues/135)
- Solutions/Lösungen können als separate Learning Elements mit Feedback-Funktionalität bereitgestellt werden: [Backend#120](https://github.com/HASKI-RAK/HASKI-Backend/issues/120), [Backend#121](https://github.com/HASKI-RAK/HASKI-Backend/issues/121)

### Technical Implementation Notes
- Die 10-Minuten-Grenze ist eine Designrichtlinie für Content-Ersteller, keine technisch durchgesetzte Beschränkung
- Bezieht sich auf alle im System verfügbaren Learning Element-Typen
- Unterstützt durch die Learning Element-Architektur:
  - Verschiedene Learning Element-Metadaten (Difficulty, Tags, Descriptions)
  - Learning Element-Tracking (Last-Viewed, Done-Date, Time-Spent) via [Frontend#263](https://github.com/HASKI-RAK/HASKI-Frontend/issues/263)
  - Learning Element-Organisation (Topics, Learning Paths, Associations)
  - Progress calculation for Topics and Sub-Topics via [Frontend#264](https://github.com/HASKI-RAK/HASKI-Frontend/issues/264)
- Verwandte technische Umsetzung in Frontend- und Backend-Komponenten für Learning Element-Management
