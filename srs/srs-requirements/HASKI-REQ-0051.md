---
id: HASKI-REQ-0051
title: Lernstrategien über REST abrufen
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
      name: "TestApi::test_get_students_learning_strategy"
---

## Beschreibung

Das System **shall** einen Endpoint `GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningStrategy` bereitstellen, der die aktuell hinterlegten Lernstrategie-Vektoren eines Studierenden (z. B. `metacognitive`, `resource_management`, `collaboration`) als strukturiertes JSON zurückliefert. Die Schnittstelle **shall** dieselben Datensätze verwenden, die beim Nutzer-Onboarding (GH-81) angelegt und später durch Fragebögen oder Analytics aktualisiert werden, sodass Dashboards und Tutoring-Algorithmen auf konsistente Werte zugreifen.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten den vollständigen Lernstrategie-Vektor; leere Arrays sind erlaubt, wenn noch keine Daten erfasst wurden.
- [x] Ungültige Kombinationen aus `student_id` und `lms_user_id` führen zu HTTP 404 mit strukturierter Fehlermeldung ohne Offenlegung anderer Daten.
- [x] Die Route akzeptiert Moodle-IDs und folgt dem von GH-30 definierten OAS-Schema, wodurch Frontends keine zusätzlichen Transformationen benötigen.
- [x] Daten stehen unmittelbar nach automatischer Nutzeranlage durch GH-81 zur Verfügung und spiegeln spätere Anpassungen deterministisch wider.

## Rationale

GitHub issue GH-30 definierte die REST-Oberfläche für Lernprofil-Daten, einschließlich `learningStrategy`. GH-81 garantiert, dass jede neu angelegte Person initiale Strategieeinträge besitzt. Die Anforderung leitet sich aus SyRS-FUNC-007 ab, damit Lernfortschrittsberichte und Empfehlungssysteme auf die gleiche Datenbasis zurückgreifen können.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Konsistenz mit den Fragebogen-Endpunkten ist sicherzustellen; Änderungen an Feldern müssen rückwärtskompatibel sein.
