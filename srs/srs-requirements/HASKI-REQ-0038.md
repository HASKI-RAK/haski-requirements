---
id: HASKI-REQ-0038
title: Lehrkraft-Kurs-Zuordnung aus Moodle übernehmen
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#21"]
---

## Beschreibung

Das System **shall** Lehrkräfte automatisch den importierten Moodle-Kursen zuordnen, sobald beide Entitäten im HASKI-Datenmodell vorhanden sind. Die Zuordnung **shall** über einen abgesicherten API-Endpunkt erfolgen, der mit Moodle-LMS-IDs arbeitet und die Beziehung nur einmalig pro Kurs/Lehrkraft erstellt. Fehlerhafte Eingaben (nicht vorhandene Kurs- oder Lehrkraft-IDs) **shall** zu klaren Fehlermeldungen führen, damit keine inkonsistenten Relationen entstehen.

## Akzeptanzkriterien

- [ ] Ein POST-Endpunkt ermöglicht es berechtigten Rollen, eine Lehrkraft anhand der Moodle-ID einem Kurs zuzuweisen
- [ ] Bei existierenden Kurs- und Lehrkraft-IDs wird genau eine Relation erzeugt und mit HTTP 201 quittiert
- [ ] Nicht vorhandene Lehrkräfte werden mit HTTP 404 samt Fehlermeldung beantwortet
- [ ] Nicht vorhandene Kurse werden mit HTTP 404 samt Fehlermeldung beantwortet
- [ ] Bereits zugewiesene Lehrkräfte lösen einen Validierungsfehler (HTTP 400) aus, Duplikate werden verhindert
- [ ] Alle Fehler- und Erfolgspfade werden protokolliert, sodass Integrationsprobleme nachvollzogen werden können

## Rationale

Die Kurs- und Lehrkraft-Zuordnung ist Bestandteil der grundlegenden Backend-Struktur (GitHub Issue #21), welche die CRUD-Funktionen für Kurse und ihre Teilnehmenden bereitstellt. Ohne diese Zuordnung können Kursberechtigungen, Algorithmuskonfigurationen und Lernpfadberechnungen nicht rollenbasiert ausgeliefert werden. Die Funktionalität wird durch den End-to-End-Test `backend/tests/e2e/test_api.py::TestApi::test_add_teacher_to_course` abgesichert.

## Hinweise

- Endpoint: `POST /lms/course/<course_id>/teacher/<teacher_id>`
- Fehlercodes orientieren sich an der zentralen Fehlerbehandlung des Flask-Backends
- Die Relation dient als Grundlage für tutorielle Funktionen (z.B. Auswahl von Lernpfad-Algorithmen)
- Weitere Tests sollten negative Szenarien (nicht vorhandene IDs, bereits zugewiesen) abdecken, um Datenbankkonsistenz sicherzustellen
