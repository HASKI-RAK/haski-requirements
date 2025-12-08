---
id: HASKI-REQ-0059
title: Lernpfad-Algorithmen pro Topic abrufen
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
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm_student"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_student_learning_path_learning_element_algorithm"
  merged_from: ["HASKI-REQ-0060"]
---

## Beschreibung

Das System **shall** Lernpfad-Algorithmus-Konfigurationen je Topic abrufbar machen, damit alle Anwendungen erkennen, welcher Algorithmus aktuell verbindlich ist. Die Schnittstelle spiegelt ausschließlich die zuletzt gepflegte Auswahl wider und stellt sicher, dass nur berechtigte Rollen Einblick erhalten.

### Tutor:innen-Perspektive

Ermöglicht das Abrufen der Tutor:innen-Konfigurationen für Lernpfad-Algorithmen.

### Studierenden-Perspektive

Ermöglicht das Abrufen des aktuell wirksamen Lernpfad-Algorithmus eines Studierenden pro Topic. So erkennen Anwendungen unmittelbar, ob eine individuelle Wahl aktiv ist oder ein Tutor:innen-Override greift, ohne eigene Vergleichslogik pflegen zu müssen.

## Akzeptanzkriterien

### Allgemein

- [x] Die Antwort enthält mindestens die eindeutige Algorithmusreferenz, den sprechenden Namen und den Bezug zum Topic.
- [x] Bezeichner und IDs entsprechen dem zentralen Algorithmuskatalog, damit Auswahl- und Anzeigeprozesse synchron bleiben.

### Tutor:innen-Perspektive

- [x] Liegt für ein Topic keine Tutor:innen-Definition vor oder fehlt die Berechtigung, wird keine Konfiguration zurückgegeben.

### Studierenden-Perspektive

- [x] Nur Kombinationen aus Studierendem und Topic, für die eine legitime Beziehung vorliegt, liefern Ergebnisse.
- [x] Ausgegebene Bezeichner bleiben mit dem zentralen Algorithmuskatalog sowie den Tutor:innen-Overrides synchron.

## Rationale

SyRS-FUNC-002 fordert, dass Tutoring-Algorithmen pro Topic gesteuert werden können, sowohl von Studierenden als auch von Tutor:innen. Damit Benutzeroberflächen, Automationen und Auswertungen erkennen, welcher Algorithmus aktiv ist, braucht es standardisierte Lesezugriffe auf diese Information. Ein lesender Zugriff auf die studentische Auswahl verhindert Inkonsistenzen zwischen UI, Backend und den adaptiven Berechnungen.

## Hinweise

- Die Schnittstelle verwendet dieselben Rollenregeln wie die Verwaltung der Tutor:innen-Overrides.
- Subtopics greifen auf die gleiche Datenquelle zu, wodurch Konfigurationen einheitlich dargestellt werden können.
- Die Datenquelle ist identisch zu den Persistierungspfaden aus HASKI-REQ-0041; dadurch bleiben Änderungen sofort sichtbar.
- Ergebnisse werden von Frontend-Dialogen und Auswertungen wiederverwendet, daher ist ein stabiler Payload erforderlich.
