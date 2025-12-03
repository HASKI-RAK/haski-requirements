---
id: HASKI-REQ-0101
title: Visualisierung der Kurs-Seite
type: Interface
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: []
  stories: []
  tests:
    - path: "frontend/src/pages/Course/Course.test.tsx"
      name: "Course Page"
---

## Beschreibung

Das System **shall** eine Kurs-Seite bereitstellen, die eine Übersicht aller Themen (Topics) des Kurses anzeigt. Die Seite **shall** die Navigation zu den einzelnen Themen ermöglichen. Für Lehrende (Course Creator) **shall** zusätzlich ein Button zum Erstellen neuer Themen angezeigt werden.

## Akzeptanzkriterien

- [x] Die Seite zeigt eine Liste aller Themen des Kurses an.
- [x] Ein Klick auf ein Thema navigiert zur entsprechenden Themen-Seite.
- [x] Lehrende sehen einen Button "Thema erstellen".
- [x] Studierende sehen den Button "Thema erstellen" nicht.

## Rationale

Die Kurs-Seite ist der zentrale Einstiegspunkt für Studierende und Lehrende, um auf die Lerninhalte zuzugreifen und diese zu verwalten.
