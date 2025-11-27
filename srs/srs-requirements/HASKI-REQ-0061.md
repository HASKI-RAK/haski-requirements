---
id: HASKI-REQ-0061
title: Subtopics eines belegten Kurses abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#76", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_sub_topics_for_topic"
---

## Beschreibung

Das System **shall** alle Subtopics eines Topics für eingeschriebene Studierende zugänglich machen. Neben den Stammdaten des jeweiligen Unterabschnitts sind auch die individuellen Lernkontexte bereitzustellen, damit Lernräume und Analysen die hierarchische Struktur vollständig nachvollziehen können.

## Akzeptanzkriterien

- [x] Die Ausgabe enthält sämtliche Subtopics inklusive Metadaten (z. B. Kennung, Titel, Parent-Bezug, Lernstatus).
- [x] Fehlen Subtopics, wird eine leere, aber gültige Antwort geliefert, sodass Aufrufer deterministisch planen können.
- [x] Anfragen außerhalb der eigenen Kurs-/Topic-Zuordnung liefern keine Daten.

## Rationale

Subtopics bilden die nächste Detailebene der Lernraumstruktur (SyRS-FUNC-008). Eine standardisierte Bereitstellung ermöglicht es, Wochenabschnitte, Module oder andere Untergliederungen konsistent darzustellen und in Lernpfaden zu berücksichtigen.

## Hinweise

- Datenstruktur und Feldnamen orientieren sich an der zentralen Topic-Spezifikation.
- Autorisierungsregeln sollten mit den Kurs- und Topic-Abfragen identisch sein, um gleiche Sichtbarkeiten zu gewährleisten.
