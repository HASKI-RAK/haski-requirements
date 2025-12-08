---
id: HASKI-REQ-0097
title: Visualisierung des Lernpfads auf der Themenseite
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#141",
      "HASKI-RAK/HASKI-Frontend#66",
      "HASKI-RAK/HASKI-Frontend#276",
    ]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "frontend/src/pages/Topic/Topic.test.tsx"
      name: "Topic Page"
---

## Beschreibung

Das System **shall** den Lernpfad eines Themas als interaktiven Graphen visualisieren. Studierende sollen ihre individuellen Lernelemente als Knoten sehen, verbunden durch Kanten, die die empfohlene oder vorgeschriebene Reihenfolge darstellen.

## Akzeptanzkriterien

- [x] Der Lernpfad wird als Graph mit Knoten (Lernelemente) und Kanten (Verbindungen) dargestellt.
- [x] Der Status der Lernelemente (erledigt, offen, gesperrt) wird visuell hervorgehoben.
- [x] Lernelemente mit gleicher Klassifikation (z.B. mehrere Übungen) werden gruppiert dargestellt (GH-276).
- [x] Ein Klick auf ein Lernelement öffnet dieses (z.B. in einem Modal oder IFrame).
- [x] Die Ansicht unterscheidet sich je nach Rolle (Studierende sehen ihren Fortschritt, Lehrende sehen eine Vorschau oder Bearbeitungsansicht).
- [x] Fehler beim Laden der Daten (User, Lernpfad, Status) werden abgefangen und dem Nutzer gemeldet.

## Rationale

Die Visualisierung des Lernpfads ist das zentrale Element für die Orientierung der Studierenden. Sie macht den Lernfortschritt transparent und ermöglicht die Navigation durch die Inhalte.

## Hinweise

- Basiert auf ReactFlow für die Graphendarstellung.
- Nutzt `useTopic` Hook für die Logik.
- Issue #141: Learning path component which renders learning elements.
- Issue #276: Grouping of learning elements.
