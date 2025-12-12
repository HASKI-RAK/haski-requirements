---
id: HASKI-REQ-0059
title: Lernpfad-Algorithmen pro Topic abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-002
links:
  stories:
    [
      "HASKI-RAK/HASKI-Backend#83",
      "HASKI-RAK/HASKI-Backend#93",
      "HASKI-RAK/HASKI-Backend#2",
      "HASKI-RAK/HASKI-Backend#30",
    ]
  parents: ["SyRS-FUNC-002", "SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm_student"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_student_learning_path_learning_element_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_for_student"
    - path: "HASKI-Frontend/src/store/Slices/LearningPathElementSlice.test.ts"
      name: "LearningPathElementSlice caching"
  merged_from: ["HASKI-REQ-0060", "HASKI-REQ-0058"]
---

## Beschreibung

Das System **shall** Lernpfad-Algorithmus-Konfigurationen je Topic abrufbar machen, damit alle Anwendungen erkennen, welcher Algorithmus aktuell verbindlich ist, und gleichzeitig den zuletzt berechneten Lernpfad eines Studierenden für ein Topic aus dem Persistenzspeicher bereitstellen. Die Schnittstellen **shall** alle relevanten Metadaten (z. B. Berechnungszeitpunkt, Grundlage, Sequenz der Elemente sowie die zugrunde liegende Algorithmusauswahl) zurückliefern, damit Frontend, Tutoring-Modell und Analytics denselben Stand verwenden können, ohne eine erneute Berechnung anzustoßen.

### Tutor:innen-Perspektive

Ermöglicht das Abrufen der Tutor:innen-Konfigurationen für Lernpfad-Algorithmen pro Topic und ihrer Wirkung auf persistierte Lernpfade.

### Studierenden-Perspektive

Ermöglicht das Abrufen des aktuell wirksamen Lernpfad-Algorithmus eines Studierenden pro Topic sowie des dazugehörigen persistierten Lernpfads. So erkennen Anwendungen unmittelbar, ob eine individuelle Wahl aktiv ist oder ein Tutor:innen-Override greift und welcher konkrete Pfad zuletzt berechnet wurde, ohne eigene Vergleichslogik pflegen zu müssen.

## Akzeptanzkriterien

### Allgemein

- [x] Die Antwort enthält mindestens die eindeutige Algorithmusreferenz, den sprechenden Namen, den Bezug zum Topic sowie – falls vorhanden – den zuletzt berechneten Lernpfad inklusive Sequenzdaten und Zeitstempel.
- [x] Bezeichner und IDs entsprechen dem zentralen Algorithmuskatalog, damit Auswahl- und Anzeigeprozesse synchron bleiben.

### Tutor:innen-Perspektive

- [x] Liegt für ein Topic keine Tutor:innen-Definition vor oder fehlt die Berechtigung, wird keine Konfiguration zurückgegeben.

### Studierenden-Perspektive

- [x] Nur Kombinationen aus Studierendem und Topic, für die eine legitime Beziehung vorliegt, liefern Ergebnisse.
- [x] Ausgegebene Bezeichner bleiben mit dem zentralen Algorithmuskatalog sowie den Tutor:innen-Overrides synchron.
- [x] Der zurückgegebene Lernpfaddatensatz entspricht exakt dem zuletzt gespeicherten Persistenzstand und kann ohne Zusatzlogik in allen Kanälen angezeigt werden.

## Rationale

SyRS-FUNC-002 fordert, dass Tutoring-Algorithmen pro Topic gesteuert werden können, sowohl von Studierenden als auch von Tutor:innen. Damit Benutzeroberflächen, Automationen und Auswertungen erkennen, welcher Algorithmus aktiv ist, braucht es standardisierte Lesezugriffe auf diese Information. Ein lesender Zugriff auf die studentische Auswahl verhindert Inkonsistenzen zwischen UI, Backend und den adaptiven Berechnungen.

## Hinweise

- Die Schnittstelle verwendet dieselben Rollenregeln wie die Verwaltung der Tutor:innen-Overrides.
- Subtopics greifen auf die gleiche Datenquelle zu, wodurch Konfigurationen einheitlich dargestellt werden können.
- Die Datenquelle ist identisch zu den Persistierungspfaden aus HASKI-REQ-0041; dadurch bleiben Änderungen sofort sichtbar.
- Ergebnisse werden von Frontend-Dialogen und Auswertungen wiederverwendet, daher ist ein stabiler Payload erforderlich.
