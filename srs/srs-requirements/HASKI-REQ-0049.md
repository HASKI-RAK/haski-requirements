---
id: HASKI-REQ-0049
title: Lernanalytics pro Studierendem abrufen
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
      name: "TestApi::test_get_students_learning_analytics"
---

## Beschreibung

Das System **shall** einen REST-Endpunkt `GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningAnalytics` bereitstellen, der für authentifizierte Rollen die aktuellen Learning-Analytics-Metriken eines Studierenden liefert. Die Antwort **shall** dieselben Kennzahlen enthalten, die beim Onboarding (GH-81) initialisiert werden, sodass Dashboards und Auswertungen konsistent auf dieselben Daten zugreifen. Ungültige oder nicht verknüpfte Moodle-IDs **shall** mit einer klaren Fehlermeldung beantwortet werden, ohne dass Daten offengelegt werden.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und serialisieren den Learning-Analytics-Datensatz des angefragten Studierenden (z. B. `engagement`, `activity_counts`, `last_activity_at`); Leerlisten sind zulässig, wenn noch keine Daten vorliegen.
- [x] Ungültige Studenten-IDs oder fehlende Zuordnungen erzeugen HTTP 404 samt strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Der Endpoint akzeptiert Moodle-IDs (`lms_user_id`) und mappt sie deterministisch auf HASKI-Studenten, wie in GH-30 spezifiziert.
- [x] Zugriff erfordert authentifizierte Nutzer (Tutor oder Studierende), die nur ihre eigenen oder berechtigten Datensätze abrufen dürfen; Autorisierung wird über bestehende Middleware sichergestellt.
- [x] Lernanalytics-Datensätze, die durch GH-81 automatisch angelegt werden, sind unmittelbar nach Nutzeranlage abrufbar.

## Rationale

Die Learning-Analytics-Datenbank dient als Grundlage für Reports gemäß SyRS-FUNC-007. GitHub issue GH-30 definiert den OAS-konformen Endpoint für das Abrufen der Daten, während GH-81 sicherstellt, dass bei der ersten Anmeldung jedes Profils initiale Analytics-Werte existieren, die später aktualisiert werden können.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Die gleiche Route besitzt eine `DELETE`-Variante für Resets; deren Verhalten ist in der Backend-API dokumentiert und nutzt denselben Datenpfad.
- Antworten sollen stabil bleiben, damit Frontend-Caches und Analytics-Dashboards keine zusätzlichen Transformationen benötigen.
