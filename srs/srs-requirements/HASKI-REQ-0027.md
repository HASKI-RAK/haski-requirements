---
id: HASKI-REQ-0027
title: Video-Lernelement-Komponente mit Animationssoftware-Unterstützung
type: Interface
status: Proposed
source_id: SyRS-INT-001
links:
  stories: ["GH-188"]
  parents: ["SyRS-INT-001"]
---

## Beschreibung

Das HASKI-System **shall** eine Frontend-Komponente (VideoNode) zur Darstellung und Integration von Video-Lernelementen bereitstellen, die professionell animierte Lehrvideos unterstützt und als Schnittstelle für Video-Animationssoftware dient.

Die VideoNode-Komponente **shall** folgende Funktionalität bereitstellen:
- Darstellung von Video-Lernelementen im adaptiven Lernpfad mit eindeutiger Klassifizierung ("AN")
- Integration in das ReactFlow-basierte Lernpfad-Interface
- Unterstützung für die Anzeige von Videoinhalten aus dem LMS (z.B. Moodle)
- Einheitliche Benutzeroberfläche konsistent mit anderen Lernelement-Typen
- Klickbare Interaktion zum Öffnen des Video-Inhalts im entsprechenden LMS-Kontext

## Akzeptanzkriterien

- [ ] Die VideoNode-Komponente ist als eigenständiger Node-Typ mit der Klassifizierung "AN" implementiert
- [ ] Die Komponente nutzt die gemeinsame BasicNode-Infrastruktur für konsistentes Verhalten
- [ ] Ein eindeutiges Video-Icon (Videocam) wird zur Identifizierung des Node-Typs verwendet
- [ ] Die Komponente kann innerhalb eines ReactFlow-Diagramms gerendert werden
- [ ] Video-Lernelemente können durch Klick geöffnet werden und zeigen den entsprechenden LMS-Inhalt
- [ ] Die VideoNode-Komponente ist in das nodeTypes-Objekt registriert und verfügbar
- [ ] Unit-Tests decken sowohl den isDone=false als auch isDone=true Zustand ab
- [ ] Unit-Tests decken sowohl den isDisabled=false als auch isDisabled=true Zustand ab
- [ ] Die Test-Coverage liegt bei mindestens 90%
- [ ] Die Komponente ist vollständig mit TypeScript typisiert
- [ ] Die Komponente folgt dem Memo-Pattern für Performance-Optimierung
- [ ] Videos können in verschiedenen Formaten und von verschiedenen Quellen eingebunden werden (iframe-Unterstützung)
- [ ] Die Darstellung von Moodle-Videos im iFrame ist optimiert und passt sich dem Frontend-Layout an

## Rationale

Primary implementation: GitHub issue GH-188: Frontend Videoplayer

Die VideoNode-Komponente wurde als Teil des adaptiven Lernpfad-Systems implementiert, um video-basierte Lerninhalte nahtlos in die personalisierte Lernumgebung zu integrieren. Videos sind ein essentieller Bestandteil moderner E-Learning-Systeme und unterstützen verschiedene Lernstile (insbesondere visuelle Lerner).

Die Schnittstelle ermöglicht es Lehrenden, professionell animierte Lehrvideos zu erstellen und in das HASKI-System einzubinden, wie in der Stakeholder-Anforderung StRS-112 gefordert.

Die Implementierung basiert auf der bestehenden BasicNode-Architektur, wodurch Code-Wiederverwendung maximiert und Konsistenz über alle Lernelement-Typen hinweg sichergestellt wird.

Derived from system requirement SyRS-INT-001 and stakeholder requirement StRS-112.

## Hinweise

- Primary issue: [GH-188](https://github.com/HASKI-RAK/HASKI-Frontend/issues/188) - Frontend Videoplayer (fokussiert auf Video-Analytics, erweitert die VideoNode-Funktionalität)
- Related work: 
  - [GH-272](https://github.com/HASKI-RAK/HASKI-Frontend/issues/272) - Optimierung der Moodle-Video-Darstellung (abgeschlossen)
  - [GH-57](https://github.com/HASKI-RAK/HASKI-Frontend/issues/57) - Skalierung von Lernelementen (inkl. Videos)
- Implementierung befindet sich in `frontend/src/components/Nodes/VideoNode/`
- Die VideoNode-Komponente nutzt die Klassifizierung "AN" (Animierte Narration/Animation)
- Verwandte Stakeholder-Anforderung: [StRS-112](../../strs/stakeholder-requirements/StRS-112.md)
- Die Komponente ist bereits implementiert und getestet, GH-188 erweitert diese um Analytics-Funktionalität
- Verifizierung erfolgt durch Unit-Tests, Integration-Tests im Lernpfad-Kontext und Demonstration der Video-Wiedergabe
- Die iFrame-Integration mit Moodle wurde in GH-272 optimiert, um Videos korrekt im Frontend einzubetten
- Zukünftige Erweiterungen (GH-188) umfassen detailliertes Tracking von Video-Interaktionen für Learning Analytics
