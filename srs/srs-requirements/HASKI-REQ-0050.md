---
id: HASKI-REQ-0050
title: Lernstil-Dimensionen über dedizierte API bereitstellen
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
      name: "TestApi::test_get_students_learning_style"
---

## Beschreibung

Das System **shall** einen REST-Endpunkt `GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningStyle` nach dem OAS aus GH-30 bereitstellen, der die vier Felder des Felder-Silverman-Modells (`input`, `perception`, `processing`, `understanding`) inklusive Dimension und Ausprägung in strukturierter Form zurückgibt. Die Route **shall** ausschließlich berechtigten Nutzenden (Studierenden selbst oder deren Lehrenden) zugänglich sein und eine deterministische Abbildung zwischen Moodle-IDs und HASKI-Studentenkonten verwenden. Lernstilwerte, die beim automatischen Onboarding über GH-81 initialisiert werden, **shall** unverändert ausgegeben werden, bis Fragebögen oder Lernpfadberechnungen neue Werte schreiben.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 sowie alle acht erwarteten Schlüssel (`perception_dimension`, `perception_value`, `input_dimension`, `input_value`, `processing_dimension`, `processing_value`, `understanding_dimension`, `understanding_value`).
- [x] Ungültige oder nicht berechtigte Kombinationen aus `student_id` und `lms_user_id` führen zu HTTP 404 mit strukturierter Fehlermeldung ohne Datenleck.
- [x] Die Werte spiegeln exakt den gespeicherten Lernstil-Datensatz aus der `learning_style`-Tabelle wider und berücksichtigen Updates aus ILS-/LIST-K-Fragebögen.
- [x] Autorisierung wird über bestehende Rollenprüfungen im Backend (Decorator) sichergestellt; direkte Zugriffe ohne Session/Cookie werden abgelehnt.

## Rationale

GitHub issue GH-30 (Basic Setup 2.0) führte die OAS-konformen Endpunkte für das Learner-Profile ein, darunter das dedizierte `learningStyle`-Retrieval. GH-81 sorgt dafür, dass bei der ersten Anmeldung jedes Profil initiale FSLSM-Werte besitzt und damit sofort abrufbar ist. Die Anforderung konkretisiert SyRS-FUNC-007, indem Lernfortschrittsreports auf fein-granulare Lernstilwerte zugreifen können.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Ergänzende Fragebogen-Endpunkte (ILS/LIST-K) aktualisieren dieselben Datensätze und bleiben kompatibel mit dieser Schnittstelle.
- Die Daten dienen sowohl dem Lernpfad-Algorithmus als auch Analytics-Dashboards; Änderungen müssen rückwärtskompatibel bleiben.
