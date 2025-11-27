---
id: HASKI-REQ-0059
title: Tutor-Algorithmen pro Topic abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-002
links:
  stories: ["HASKI-RAK/HASKI-Backend#83", "HASKI-RAK/HASKI-Backend#93"]
  parents: ["SyRS-FUNC-002"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm"
---

## Beschreibung

Das System **shall** Tutor:innen-Konfigurationen für Lernpfad-Algorithmen je Topic abrufbar machen, damit alle Anwendungen erkennen, welcher Algorithmus aktuell verbindlich ist. Die Schnittstelle spiegelt ausschließlich die zuletzt gepflegte Auswahl wider und stellt sicher, dass nur berechtigte Rollen Einblick erhalten.

## Akzeptanzkriterien

- [x] Die Antwort enthält mindestens die eindeutige Algorithmusreferenz, den sprechenden Namen und den Bezug zum Topic.
- [x] Liegt für ein Topic keine Tutor:innen-Definition vor oder fehlt die Berechtigung, wird keine Konfiguration zurückgegeben.
- [x] Bezeichner und IDs entsprechen dem zentralen Algorithmuskatalog, damit Auswahl- und Anzeigeprozesse synchron bleiben.

## Rationale

SyRS-FUNC-002 fordert, dass Tutoring-Algorithmen pro Topic gesteuert werden können. Damit Benutzeroberflächen, Automationen und Auswertungen erkennen, welcher Algorithmus aktiv ist, braucht es einen standardisierten Lesezugriff auf diese Information.

## Hinweise

- Die Schnittstelle verwendet dieselben Rollenregeln wie die Verwaltung der Tutor:innen-Overrides.
- Subtopics greifen auf die gleiche Datenquelle zu, wodurch Konfigurationen einheitlich dargestellt werden können.
