---
id: HASKI-REQ-0035
title: Automatische Kursanlage und -synchronisation aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#21"]
  tests:
    [
      "backend/tests/e2e/test_api.py::TestApi::test_api_create_course_from_moodle_without_start_date",
      "backend/tests/e2e/test_api.py::TestApi::test_api_create_course_from_moodle",
    ]
---

## Beschreibung

Das System **shall** Kurse automatisch basierend auf Daten aus dem Learning Management System (Moodle) anlegen und aktualisieren. Dabei **shall** die Kursstruktur, Metadaten (wie Name, ID, Startdatum) und die Zuordnung zur Hochschule übernommen werden.

## Akzeptanzkriterien

- [ ] Das System stellt einen Endpunkt zur Erstellung von Kursen bereit
- [ ] Kurse werden mit korrekter Moodle-ID (LMS-ID) angelegt
- [ ] Metadaten wie Name, Erstellungsdatum und Startdatum werden korrekt übernommen
- [ ] Das System verhindert das Anlegen von Duplikaten (basierend auf LMS-ID)
- [ ] Fehlende optionale Parameter (z.B. Startdatum) werden robust behandelt
- [ ] Ungültige Eingabedaten führen zu entsprechenden Fehlermeldungen

## Rationale

Die Synchronisation der Kursdaten ist essenziell, um die Lernumgebung in HASKI mit dem führenden System (Moodle) konsistent zu halten. Dies wurde initial im Rahmen der Basic Backend Structure (Issue #21) umgesetzt.
