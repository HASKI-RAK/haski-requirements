---
id: HASKI-REQ-0038
title: Benutzer-Kurs-Zuordnung aus Moodle übernehmen
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#21", "HASKI-RAK/HASKI-Backend#131"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_teacher_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_student_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_add_student_to_course_duplicate"
  merged_from: ["HASKI-REQ-0039"]
---

## Beschreibung

Das System **shall** Benutzer (Lehrkräfte und Studierende) automatisch den importierten Moodle-Kursen zuordnen, sobald beide Entitäten im HASKI-Datenmodell vorhanden sind. Die Zuordnung **shall** über abgesicherte API-Endpunkte erfolgen, die mit Moodle-LMS-IDs arbeiten und die Beziehung nur einmalig pro Kurs/Benutzer erstellt. Fehlerhafte Eingaben (nicht vorhandene Kurs- oder Benutzer-IDs) **shall** zu klaren Fehlermeldungen führen, damit keine inkonsistenten Relationen entstehen.

### Lehrkraft-Zuordnung

Endpoint: `POST /lms/course/<course_id>/teacher/<teacher_id>`

### Studierenden-Zuordnung

Endpoint: `POST /lms/course/<course_id>/student/<student_id>`

- Zusätzlich werden initiale Lerncharakteristika (ILS/Learning-Style-Basiswerte) für die neue Kurszuordnung persistiert, sodass unmittelbar personalisierte Lernpfad-Berechnungen möglich werden.

## Akzeptanzkriterien

### Lehrkraft-Zuordnung

- [ ] Ein POST-Endpunkt ermöglicht es berechtigten Rollen, eine Lehrkraft anhand der Moodle-ID einem Kurs zuzuweisen
- [ ] Bei existierenden Kurs- und Lehrkraft-IDs wird genau eine Relation erzeugt und mit HTTP 201 quittiert
- [ ] Nicht vorhandene Lehrkräfte werden mit HTTP 404 samt Fehlermeldung beantwortet
- [ ] Nicht vorhandene Kurse werden mit HTTP 404 samt Fehlermeldung beantwortet
- [ ] Bereits zugewiesene Lehrkräfte lösen einen Validierungsfehler (HTTP 400) aus, Duplikate werden verhindert

### Studierenden-Zuordnung

- [ ] Ein POST-Endpunkt `POST /lms/course/<course_id>/student/<student_id>` erstellt genau eine Kursmitgliedschaft mit HTTP 201, wenn Kurs- und Studierenden-ID existieren
- [ ] Die Antwort des Endpunkts enthält die Kurs- und Studierenden-IDs sowie die initialen Lernstil-Dimensionen (`input`, `perception`, `processing`, `understanding`)
- [ ] Nicht vorhandene Studierende führen zu HTTP 404 mit erklärender Fehlermeldung
- [ ] Nicht vorhandene Kurse führen zu HTTP 404 mit erklärender Fehlermeldung
- [ ] Bereits bestehende Zuordnungen werden nicht dupliziert, sondern liefern einen Validierungsfehler (HTTP 400/409)

### Allgemein

- [ ] Alle Fehler- und Erfolgspfade werden protokolliert, sodass Integrationsprobleme nachvollzogen werden können

## Rationale

Die Kurs- und Benutzer-Zuordnung ist Bestandteil der grundlegenden Backend-Struktur (GitHub Issue #21 für Lehrkräfte, #131 für Studierende), welche die CRUD-Funktionen für Kurse und ihre Teilnehmenden bereitstellt. Ohne diese Zuordnung können Kursberechtigungen, Algorithmuskonfigurationen und Lernpfadberechnungen nicht rollenbasiert ausgeliefert werden.

GitHub Issue [#131](https://github.com/HASKI-RAK/HASKI-Backend/issues/131) fordert, dass Studierende ausschließlich Kurse sehen, an denen sie in Moodle teilnehmen. Die persistierten Lernstil-Basiswerte stellen sicher, dass unmittelbar nach der Zuordnung adaptive Lernpfade berechnet werden können.

## Hinweise

- Endpoint Lehrkraft: `POST /lms/course/<course_id>/teacher/<teacher_id>`
- Endpoint Studierende: `POST /lms/course/<course_id>/student/<student_id>`
- Fehlercodes orientieren sich an der zentralen Fehlerbehandlung des Flask-Backends
- Die Relationen dienen als Grundlage für tutorielle Funktionen (z.B. Auswahl von Lernpfad-Algorithmen) und personalisierte Lernpfade
- Die Zuordnung nutzt die aus Moodle gelieferten LMS-IDs, sodass keine manuelle Pflege notwendig ist
- Initiale Lerncharakteristika werden für Studierende aus bestehenden Studentendaten kopiert, um konsistente Empfehlungen zu gewährleisten
- Weitere Tests sollten negative Szenarien (nicht vorhandene IDs, bereits zugewiesen) abdecken, um Datenbankkonsistenz sicherzustellen
