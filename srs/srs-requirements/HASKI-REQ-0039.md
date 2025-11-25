---
id: HASKI-REQ-0039
title: Studierenden-Kurs-Zuordnung aus Moodle übernehmen
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#131"]
---

## Beschreibung

Das System **shall** Studierende, die in Moodle als Kursteilnehmende geführt werden, automatisiert den importierten HASKI-Kursen zuordnen. Die Zuordnung **shall** über einen abgesicherten API-Endpunkt erfolgen, der Moodle-IDs für Kurs und Studierende entgegen nimmt und für jede Kombination genau eine Relation in `student_course` erzeugt. Die Schnittstelle **shall** gleichzeitig die initialen Lerncharakteristika (ILS/Learning-Style-Basiswerte) für die neue Kurszuordnung persistieren, sodass unmittelbar personalisierte Lernpfad-Berechnungen möglich werden. Ungültige Referenzen (nicht vorhandene Kurs- oder Studierenden-IDs) **shall** deterministisch abgefangen und mit klaren Fehlermeldungen zurückgegeben werden, damit keine inkonsistenten Kursmitgliedschaften entstehen.

## Akzeptanzkriterien

- [ ] Ein POST-Endpunkt `POST /lms/course/<course_id>/student/<student_id>` erstellt genau eine Kursmitgliedschaft mit HTTP 201, wenn Kurs- und Studierenden-ID existieren
- [ ] Die Antwort des Endpunkts enthält die Kurs- und Studierenden-IDs sowie die initialen Lernstil-Dimensionen (`input`, `perception`, `processing`, `understanding`)
- [ ] Nicht vorhandene Studierende führen zu HTTP 404 mit erklärender Fehlermeldung
- [ ] Nicht vorhandene Kurse führen zu HTTP 404 mit erklärender Fehlermeldung
- [ ] Bereits bestehende Zuordnungen werden nicht dupliziert, sondern liefern einen Validierungsfehler (HTTP 400/409)
- [ ] Alle Fehler- und Erfolgspfade werden protokolliert, damit Moodle-Integrationsprobleme nachvollzogen werden können

## Rationale

GitHub Issue [#131](https://github.com/HASKI-RAK/HASKI-Backend/issues/131) fordert, dass Studierende ausschließlich Kurse sehen, an denen sie in Moodle teilnehmen. Dafür ist eine zuverlässige Übernahme der Kursmitgliedschaften inklusive Validierung obligatorisch. Die persistierten Lernstil-Basiswerte stellen sicher, dass unmittelbar nach der Zuordnung adaptive Lernpfade berechnet werden können. Verifiziert durch `backend/tests/e2e/test_api.py::TestApi::test_add_student_to_course`.

## Hinweise

- Die Zuordnung nutzt die aus Moodle gelieferten LMS-IDs, sodass keine manuelle Pflege notwendig ist
- Der Endpunkt folgt denselben Fehlercodes und Logging-Konventionen wie die Lehrkraft-Zuordnung
- Initiale Lerncharakteristika werden aus bestehenden Studentendaten kopiert, um konsistente Empfehlungen zu gewährleisten
