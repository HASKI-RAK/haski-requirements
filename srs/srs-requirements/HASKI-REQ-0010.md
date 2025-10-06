---
id: HASKI-REQ-0010
title: H5P-basierte interaktive Lerninhalte und Videos
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Demonstration
links:
  stories: ["HASKI-RAK/HASKI-Frontend#139", "HASKI-RAK/HASKI-Frontend#211", "HASKI-RAK/HASKI-Frontend#188", "HASKI-RAK/HASKI-Frontend#315", "HASKI-RAK/HASKI-Frontend#331"]
  tests: []
  parents: [SyRS-FUNC-004]
---

## Beschreibung

Das System **shall** H5P-basierte interaktive Lerninhalte und eingebettete Lehrvideos über die Moodle-Integration bereitstellen.

## Rationale

H5P ist das zentrale Framework für die Bereitstellung interaktiver Inhalte im HASKI-System. Es ermöglicht:
- Animierte, interaktive Lernelemente (Quizze, Präsentationen, Simulationen)
- Einbettung und Wiedergabe von Lehrvideos
- Tracking von Lerninteraktionen über xAPI/LRS
- Nahtlose Integration in die adaptive Lernpfad-Darstellung

Die Implementierung erfolgt durch H5P-Aktivitäten in Moodle, die über iFrames im HASKI-Frontend dargestellt werden.

## Akzeptanzkriterien

1. H5P-Lernelemente sind in Moodle-Kursen erstellt und verfügbar
2. H5P-Inhalte werden im HASKI-Frontend über optimierte iFrames angezeigt
3. H5P-Aktivitäten sind als Knoten im adaptiven Lernpfad darstellbar
4. Lösungen zu H5P-Aufgaben können über Button in iFrame angezeigt werden
5. H5P-Ergebnisse werden vom LogStore Moodle Plugin an das LRS gesendet
6. Backend kann H5P-Lerndaten vom LRS abrufen und verarbeiten
7. Videos innerhalb von H5P-Inhalten sind abspielbar

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

