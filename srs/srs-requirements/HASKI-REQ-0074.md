---
id: HASKI-REQ-0074
title: Lernstil-Dimensionen aktualisieren
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-007
links:
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#81"]
  parents: ["SyRS-FUNC-007"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_learning_style_by_student_id"
---

## Beschreibung

Das System **shall** einen REST-Endpunkt `PUT /user/<user_id>/<lms_user_id>/student/<student_id>/learningStyle` bereitstellen, über den autorisierte Rollen (Studierende selbst, Lehrende) die vier Dimensionen des Felder–Silverman-Lernstilmodells (Perception, Input, Processing, Understanding) mitsamt numerischer Ausprägung aktualisieren. Die Schnittstelle **shall** ausschließlich valide Kombinationen aus HASKI-User-ID, Moodle-User-ID und Student-ID akzeptieren und die Werte direkt dem vorhandenen `learning_style`-Datensatz des Lernprofils zuordnen, sodass Lernpfad-Berechnungen und Dashboards sofort mit den neuen Präferenzen arbeiten können. Eingaben **shall** vollständig und strukturiert übertragen werden, damit keine inkonsistenten Lernprofil-Datensätze entstehen.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 201 sowie alle acht Felder (`*_dimension`, `*_value`) der FSLSM-Darstellung und spiegeln den persistenten Datensatz wider.
- [x] Die numerischen Werte müssen im Bereich 1–11 liegen; Werte außerhalb oder fehlende Felder führen zu HTTP 400 mit der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`).
- [x] Ungültige Typen (z. B. Strings statt Integern) oder leere Requests werden deterministisch mit HTTP 400 beantwortet.
- [x] Nicht existente Nutzer- oder Studierendenkombinationen resultieren in HTTP 404 ohne Offenlegung interner Details.
- [x] Nach erfolgreichem Update geben `GET /learningStyle` sowie `GET /learningCharacteristics` dieselben Werte aus, sodass Reports und Empfehlungsalgorithmen konsistent bleiben.

## Rationale

GitHub issue GH-30 definiert den OAS-konformen Lernprofil-Endpunkt und verlangt, dass das Backend alle CRUD-Operationen unterstützt. GH-81 stellt sicher, dass bei der Erstanmeldung initiale Lernstilwerte existieren, die anschließend über diesen PUT-Endpunkt überschrieben werden können, sobald neue ILS-/LIST-K-Ergebnisse vorliegen. Die Anforderung verfeinert SyRS-FUNC-007, indem sie die Pflege der zugrunde liegenden Lernprofil-Daten beschreibt.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Fehlerfälle sollen geloggt werden, damit fehlerhafte Fragebogenimporte nachvollzogen werden können.
