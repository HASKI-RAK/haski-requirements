---
id: HASKI-REQ-0010
title: H5P-basierte interaktive Lerninhalte und Videos
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Demonstration
links:
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#139",
      "HASKI-RAK/HASKI-Frontend#211",
      "HASKI-RAK/HASKI-Frontend#188",
      "HASKI-RAK/HASKI-Frontend#315",
      "HASKI-RAK/HASKI-Frontend#331",
      "HASKI-RAK/HASKI-Frontend#272",
      "HASKI-RAK/HASKI-Frontend#57",
    ]
  tests: []
  parents: ["SyRS-FUNC-004", "SyRS-INT-001"]
---

## Beschreibung

Das System **shall** H5P-basierte interaktive Lerninhalte und eingebettete Lehrvideos über die Moodle-Integration bereitstellen.

Das Frontend **shall** hierfür eine spezialisierte Video-Lernelement-Komponente (VideoNode) im adaptiven Lernpfad bereitstellen, die Video-Lernelemente mit der Klassifizierung "AN" rendert, in das ReactFlow-Layout integriert und Videoinhalte aus dem LMS (z. B. Moodle) konsistent mit anderen Lernelement-Typen darstellt.

## Rationale

H5P ist das zentrale Framework für die Bereitstellung interaktiver Inhalte im HASKI-System. Es ermöglicht:

- Animierte, interaktive Lernelemente (Quizze, Präsentationen, Simulationen)
- Einbettung und Wiedergabe von Lehrvideos
- Tracking von Lerninteraktionen über xAPI/LRS
- Nahtlose Integration in die adaptive Lernpfad-Darstellung

Die Implementierung erfolgt durch H5P-Aktivitäten in Moodle, die über iFrames im HASKI-Frontend dargestellt werden.

Die spezialisierte VideoNode-Komponente konkretisiert diese Anforderung für video-basierte und professionell animierte Lehrinhalte (vgl. StRS-112) und stellt sicher, dass Videos als eigenständige, im Lernpfad klar erkennbare Lernelemente integriert sind.

## Akzeptanzkriterien

1. H5P-Lernelemente sind in Moodle-Kursen erstellt und verfügbar
2. H5P-Inhalte werden im HASKI-Frontend über optimierte iFrames angezeigt
3. H5P-Aktivitäten sind als Knoten im adaptiven Lernpfad darstellbar
4. Lösungen zu H5P-Aufgaben können über Button in iFrame angezeigt werden
5. H5P-Ergebnisse werden vom LogStore Moodle Plugin an das LRS gesendet
6. Backend kann H5P-Lerndaten vom LRS abrufen und verarbeiten
7. Videos innerhalb von H5P-Inhalten sind abspielbar

### Video-Lernelement-Komponente (VideoNode)

- [x] Die VideoNode-Komponente ist als eigenständiger Node-Typ mit der Klassifizierung "AN" implementiert.
- [x] Die Komponente nutzt die gemeinsame BasicNode-Infrastruktur für konsistentes Verhalten.
- [x] Ein eindeutiges Video-Icon wird zur Identifizierung des Node-Typs verwendet.
- [x] Die Komponente kann innerhalb eines ReactFlow-Diagramms gerendert und im `nodeTypes`-Objekt registriert werden.
- [x] Video-Lernelemente können durch Klick geöffnet werden und zeigen den entsprechenden LMS-Inhalt im iFrame-Kontext an.
- [x] Unit-Tests decken die Zustände `isDone` true/false sowie `isDisabled` true/false ab und erreichen eine Testabdeckung von mindestens 100 %.
- [x] Die Komponente ist vollständig mit TypeScript typisiert und folgt dem Memo-Pattern für Performance-Optimierung.
- [x] Videos können in verschiedenen Formaten und von verschiedenen Quellen eingebunden werden; die iFrame-Darstellung von Moodle-Videos ist für das HASKI-Layout optimiert.

## Abhängigkeiten

- Moodle-Integration mit H5P-Plugin
- LogStore Moodle Plugin für xAPI-Statements
- LRS (Learning Record Store) für Tracking-Daten
- Frontend-Komponente für iFrame-Darstellung

## Implementierungshinweise

### Primäre Implementierung

- **GH-139**: Grundlegende H5P-Integration (Alpha-Version, abgeschlossen)
  - Dokumentation der Moodle-Endpunkte für H5P-Elemente
  - Bereitstellung von H5P-Aktivitäten in Kursen

### Layout & Darstellung

- **GH-211**: Optimiertes iFrame-Layout für H5P-Aktivitäten (abgeschlossen)
  - Moodle-Theme-Anpassungen für bessere Frontend-Integration
  - H5P als prioritäre Aktivität für Layout-Optimierung

### Video-Funktionalität

- **GH-188**: Videoplayer mit Learning Analytics
  - Tracking von 13 Video-Interaktionstypen (Play, Pause, Seek, etc.)
  - Bereits verknüpft mit SyRS-INT-001

### Erweiterte Features (in Entwicklung)

- **GH-315**: Lösungsanzeige für H5P-Aufgaben über Button/iFrame
- **GH-331**: Lernpfad-Steuerung basierend auf H5P-Resultaten
  - Integration der H5P-Ergebnisdaten in die adaptive Lernpfad-Logik

## Verifikation

- **Methode**: Demonstration
- **Kriterium**: H5P-Inhalte (inkl. Videos) sind im Frontend sichtbar und voll funktionsfähig
- **Status**: Grundfunktionalität implementiert (Alpha), erweiterte Features in Entwicklung
