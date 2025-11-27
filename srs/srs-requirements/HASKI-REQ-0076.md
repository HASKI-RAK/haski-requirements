---
id: HASKI-REQ-0076
title: Topics aus Moodle aktualisieren
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
      name: "TestApi::test_update_topic_from_moodle"
---

## Beschreibung

Das Backend **shall** einen OAS-konformen Endpunkt `PUT /lms/topic/<topic_id>/<moodle_topic_id>` bereitstellen, über den Moodle aktualisierte Topic- und Subtopic-Metadaten nach HASKI synchronisiert. Die Route **shall** anhand der Kombination aus Topic-ID und Moodle-ID eindeutig bestimmen, welcher Knoten angepasst wird, und die Felder `name`, `is_topic`, `parent_id`, `contains_le`, `created_by`, `created_at`, `last_updated` sowie `university` gemäß Payload übernehmen. Bei Subtopics **shall** die Parent-Relation automatisch auf den referenzierten Topic gesetzt werden, damit Lernpfad- und Content-Zuordnungen konsistent bleiben.

## Akzeptanzkriterien

- [x] Erfolgreiche Updates liefern HTTP 201 und geben den vollständigen Topic-Datensatz (`id`, `lms_id`, `is_topic`, `parent_id`, `contains_le`, Zeitsstempel, `university`) zurück.
- [x] Ungültige Kombinationen aus Topic-ID und Moodle-ID führen zu HTTP 404 mit standardisierter Fehlstruktur (`{"error": "...", "message": "..."}`), ohne interne Details preiszugeben.
- [x] Fehlende Pflichtfelder oder falsche Datentypen resultieren in HTTP 400 und hinterlassen keine Datenänderung.
- [x] Beim Aktualisieren von Subtopics wird `parent_id` auf den bestehenden Topic gesetzt, falls nicht explizit angegeben, sodass die Hierarchie stabil bleibt.
- [x] `created_at`/`last_updated` Werte werden validiert (ISO 8601) und persistiert, damit Änderungsverfolgung und Vergleich mit Moodle möglich bleiben.

## Rationale

GitHub issue GH-21 („Basic Backend Structure") fordert CRUD-Unterstützung für alle Kursstrukturelemente. Nachdem Topics initial automatisch angelegt werden (HASKI-REQ-0036), stellt diese Anforderung sicher, dass spätere Änderungen in Moodle (Umbenennungen, neue `contains_le`-Flags, Hierarchieanpassungen) verlustfrei in HASKI übernommen werden. Damit bleibt die LTI-Integration gemäß SyRS-INT-003 konsistent.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/21
- Validierungsfehler sollen auditierbar geloggt werden, da sie häufig auf veraltete LMS-IDs oder fehlerhafte Moodle-Plugins hinweisen.
- Topic-Updates triggern nachgelagerte Invalidierungen (z. B. Cache für Kursstruktur); diese Logik liegt außerhalb dieser Anforderung, muss aber berücksichtigt werden.
