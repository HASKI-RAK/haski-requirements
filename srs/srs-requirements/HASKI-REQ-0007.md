---
id: HASKI-REQ-0007
title: Automatische Anpassung von Lernpfaden basierend auf Lernstil
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Demonstration
source_id: SyRS-FUNC-001
links:
  stories: ["GH-239", "GH-209", "GH-220", "GH-182"]
  parents: [SyRS-FUNC-001]
---

## Beschreibung

Das HASKI-System **shall** Lernpfade automatisch an die individuellen Lernstile, Interessen und Kompetenzen der Studierenden anpassen. Das System **shall** basierend auf den Ergebnissen des ILS-Fragebogens (Index of Learning Styles) personalisierte Lernempfehlungen generieren und den Studierenden adaptive Lernpfade bereitstellen.

## Akzeptanzkriterien

### Lernpfad-Berechnung (GH-239)
- [x] Lernpfad wird automatisch nach dem Absenden des ILS-Fragebogens berechnet
- [x] Berechnung berücksichtigt die ILS-Dimensionen des Studierenden
- [x] Algorithmen sind konfigurierbar für verschiedene Standorte (Kempten, Aschaffenburg)
- [x] Topic-IDs werden in die Lernpfad-Generierung einbezogen

### ILS-Verarbeitung (GH-209)
- [x] ILS-Antworten werden durch einen Algorithmus im Backend verarbeitet
- [x] Lernstil-Dimensionen werden aus den ILS-Antworten bestimmt
- [x] Studierende können ihre ILS-Ergebnisse im Frontend einsehen
- [x] Lernpfad-Algorithmus kann die bestimmten Dimensionen verwenden

### ILS-Pflichterfüllung (GH-220)
- [x] System prüft beim Start, ob ILS-Ergebnisse vorliegen (fetch ILS)
- [x] Wenn ILS-Ergebnisse vorhanden sind, wird localStorage entsprechend gesetzt
- [x] Ohne ILS-Ergebnisse wird der ILS-Fragebogen angezeigt
- [x] Modal kann weggeklickt werden, öffnet sich aber erneut, wenn Antworten nicht gesendet wurden
- [x] Nach erfolgreichem Absenden wird die Information im Cookie gespeichert

### Datenpersistierung (GH-182)
- [x] ILS-Fragebogen-Antworten werden an Backend gesendet
- [x] Antworten werden persistent gespeichert
- [x] ILS-Short und LIST-K Fragebogen-Antworten werden ebenfalls persistiert

### Adaptive Lernpfad-Funktionalität
- [x] Lernpfade werden individuell für jeden Studierenden generiert
- [x] System berücksichtigt Lernstil-Präferenzen bei der Content-Empfehlung
- [x] Lernpfade sind zugänglich und nutzbar nach ILS-Absolvierung
- [x] System verhindert Nutzung ohne absolvierte ILS-Erfassung

## Rationale

Primary implementation: GitHub issue GH-239: "User learning path is calculated after submitting ILS questionnaire"

Related work:
- GH-209: Implementiert den ILS-Algorithmus zur Verarbeitung der Fragebogen-Antworten und Bestimmung der Lernstil-Dimensionen
- GH-220: Stellt sicher, dass Studierende den ILS-Fragebogen ausfüllen, bevor sie das System nutzen können (Voraussetzung für personalisierte Lernpfade)
- GH-182: Implementiert die Persistierung der Fragebogen-Antworten (ILS, ILS-Short, LIST-K) im Backend

Derived from system requirement SyRS-FUNC-001, which implements stakeholder requirement StRS-101.

Die automatische Anpassung von Lernpfaden ist eine Kernfunktionalität des HASKI-Systems und differenziert es von herkömmlichen Lernmanagementsystemen. Durch die Berücksichtigung individueller Lernstile (basierend auf dem ILS-Modell), Interessen und Kompetenzen wird die Motivation, Akzeptanz und der Lernerfolg der Studierenden gefördert.

## Hinweise

- **Primary issue**: [GH-239](https://github.com/HASKI-RAK/HASKI-Frontend/issues/239) - Implementiert die eigentliche Lernpfad-Berechnung nach ILS-Absolvierung
- **Related issues**: 
  - [GH-209](https://github.com/HASKI-RAK/HASKI-Frontend/issues/209) - ILS-Algorithmus im Backend
  - [GH-220](https://github.com/HASKI-RAK/HASKI-Frontend/issues/220) - ILS-Pflicht für Frontend-Nutzung
  - [GH-182](https://github.com/HASKI-RAK/HASKI-Frontend/issues/182) - Fragebogen-Datenpersistierung
- **Technical details**:
  - Verwendet den Index of Learning Styles (ILS) zur Bestimmung von Lernstil-Präferenzen
  - Algorithmen sind hardcoded aber konfigurierbar für verschiedene Hochschul-Standorte
  - Integration mit "Marc's Learning Path Algorithm" für die eigentliche Pfad-Generierung
  - Speicherung des ILS-Status in localStorage und Cookie
- **Dependencies**: ILS-Fragebogen muss ausgefüllt sein, bevor Lernpfade generiert werden können
- **Status**: Alle vier Issues sind implementiert und geschlossen (Juli 2023 - Dezember 2023)

