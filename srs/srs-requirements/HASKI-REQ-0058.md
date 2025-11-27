---
id: HASKI-REQ-0058
title: Persistierte Lernpfade pro Topic abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#2", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_for_student"
---

## Beschreibung

Das System **shall** den zuletzt berechneten Lernpfad eines Studierenden für ein Topic aus dem Persistenzspeicher abrufbar machen. Die Schnittstelle muss alle relevanten Metadaten (z. B. Berechnungszeitpunkt, Grundlage, Sequenz der Elemente) bereitstellen, damit Frontend, Tutoring-Modell und Analytics denselben Stand verwenden können, ohne eine erneute Berechnung anzustoßen.

## Akzeptanzkriterien

- [x] Für gültige Kurs-/Topic-Kombinationen steht der vollständige Lernpfad inklusive Sequenzdaten, Bezugswerte und Zeitstempel zur Verfügung.
- [x] Lernpfade außerhalb der eigenen Einschreibung werden nicht ausgeliefert.
- [x] Der zurückgegebene Datensatz entspricht exakt dem zuletzt gespeicherten Persistenzstand und kann ohne Zusatzlogik in allen Kanälen angezeigt werden.

## Rationale

SyRS-FUNC-008 schreibt konsistente adaptive Lernräume vor. Das Abrufen eines gespeicherten Lernpfads stellt sicher, dass Studierende und Lehrende jederzeit denselben Vorschlag sehen wie die Tutoring-Algorithmen, selbst wenn aktuell keine neue Berechnung läuft.

## Hinweise

- Die Felder und Beziehungen orientieren sich am Lernpfad-Datenmodell (siehe OAS und Backend-Dokumentation).
- Autorisierungs- und Filterregeln sollten deckungsgleich mit Topic- und Subtopic-Abfragen umgesetzt sein.
