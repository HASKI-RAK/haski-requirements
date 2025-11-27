---
id: HASKI-REQ-0060
title: Studentische Lernpfad-Algorithmen abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-002
links:
  stories: ["HASKI-RAK/HASKI-Backend#83"]
  parents: ["SyRS-FUNC-002"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm_student"
---

## Beschreibung

Das System **shall** den aktuell wirksamen Lernpfad-Algorithmus eines Studierenden pro Topic ausgeben können. So erkennen Anwendungen unmittelbar, ob eine individuelle Wahl aktiv ist oder ein Tutor:innen-Override greift, ohne eigene Vergleichslogik pflegen zu müssen.

## Akzeptanzkriterien

- [x] Die Antwort benennt mindestens den Algorithmus (sprechender Name, ID) sowie den Topic-Bezug.
- [x] Nur Kombinationen aus Studierendem und Topic, für die eine legitime Beziehung vorliegt, liefern Ergebnisse.
- [x] Ausgegebene Bezeichner bleiben mit dem zentralen Algorithmuskatalog sowie den Tutor:innen-Overrides synchron.

## Rationale

SyRS-FUNC-002 beschreibt, dass Lernpfad-Algorithmen sowohl von Studierenden als auch von Tutor:innen gesteuert werden können. Ein lesender Zugriff auf die studentische Auswahl verhindert Inkonsistenzen zwischen UI, Backend und den adaptiven Berechnungen.

## Hinweise

- Die Datenquelle ist identisch zu den Persistierungspfaden aus HASKI-REQ-0041; dadurch bleiben Änderungen sofort sichtbar.
- Ergebnisse werden von Frontend-Dialogen und Auswertungen wiederverwendet, daher ist ein stabiler Payload erforderlich.
