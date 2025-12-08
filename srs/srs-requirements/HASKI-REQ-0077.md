---
id: HASKI-REQ-0077
title: Learning Elements aus Moodle aktualisieren
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  stories: ["HASKI-RAK/HASKI-Backend#21"]
  parents: ["SyRS-INT-003"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_le_from_moodle"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_learning_element"
---

## Beschreibung

Das Backend **shall** einen Endpunkt `PUT /lms/learningElement/<learning_element_id>/<moodle_learning_element_id>` bereitstellen, über den Moodle aktualisierte Metadaten eines Learning Elements (z. B. Aktivitätstyp, Klassifikation, Name, Verantwortliche Person, Zeitstempel, Universität) nach HASKI synchronisiert. Die Route **shall** die Kombination aus interner Learning-Element-ID und Moodle-ID validieren, bevor Änderungen geschrieben werden, damit bestehende Zuordnungen zu Topics/Subtopics unverändert bleiben.

## Akzeptanzkriterien

- [x] Erfolgreiche Updates liefern HTTP 201 und geben `id`, `lms_id`, `activity_type`, `classification`, `name`, `created_by`, `created_at`, `university` zurück.
- [x] Fehlende Pflichtfelder oder falsche Datentypen führen zu HTTP 400 mit der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) und resultieren in keiner Datenänderung.
- [x] Ungültige ID-Kombinationen werden mit HTTP 404 beantwortet, ohne interne Details offenzulegen.
- [x] Die Zuordnung zum Topic/Subtopic bleibt unverändert; für verschobene Elemente muss ein eigener Move-Workflow verwendet werden.
- [x] Zeitstempel werden auf valide ISO-8601-Formate geprüft, um Änderungsverfolgung und Synchronisation mit Moodle zu gewährleisten.

## Rationale

Nachdem Learning Elements (HASKI-REQ-0037) automatisch angelegt werden, müssen spätere Anpassungen aus Moodle (z. B. neue Benennungen oder Klassifikationen) in HASKI gespiegelt werden, damit Empfehlungen, Ratings und Lernpfade mit den aktuellen Aktivitätsdaten arbeiten. Die Umsetzung basiert auf GitHub issue GH-21, welches sämtliche CRUD-Funktionalität für Moodle-Schnittstellen fordert, und konkretisiert SyRS-INT-003.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/21
- Die Backend-Validierung der Felder `activity_type` und `classification` folgt den in der Domain-Logik hinterlegten Wertemengen, um fehlerhafte Moodle-Plugins frühzeitig zu erkennen.
