---
id: HASKI-REQ-0071
title: Moodle-Aktivitätsstatus abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-005
links:
  parents: ["SyRS-INT-005", "SyRS-FUNC-007"]
  stories:
    - "HASKI-RAK/HASKI-Backend#30"
    - "HASKI-RAK/HASKI-Frontend#264"
    - "HASKI-RAK/HASKI-Frontend#263"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_activity_status_for_student"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_activity_status_for_student_for_learning_element"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_moodle_rest_url_for_completion_status"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_activity_status_for_student_for_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_activity_status_for_student_for_learning_element_for_course"
    - path: "frontend/src/common/hooks/LearningPathTopicProgress/LearningPathTopicProgress.test.tsx"
      name: "LearningPathTopicProgress tests"
    - path: "frontend/src/services/LearningPath/fetchLearningPathElementStatus.test.tsx"
      name: "fetchLearningPathElementStatus has expected behaviour"
    - path: "frontend/src/services/LearningPath/fetchLearningPathElementSpecificStatus.test.tsx"
      name: "fetchLearningPathElementSpecificStatus has expected behaviour"
    - path: "frontend/src/components/StyledLinearProgress/StyledLinearProgress.test.tsx"
      name: "StyledLinearProgress tests"
    - path: "HASKI-Frontend/src/components/StyledLinearProgress/LinearProgressWithLabel.test.tsx"
      name: "LinearProgressWithLabel"
    - path: "HASKI-Frontend/src/store/Slices/LearningPathElementSpecificStatusSlice.test.ts"
      name: "LearningPathElementSpecificStatusSlice"
    - path: "HASKI-Frontend/src/store/Slices/LearningPathElementStatusSlice.test.ts"
      name: "LearningPathElementStatusSlice"
---

## Beschreibung

Das Backend **shall** zwei GET-Endpunkte bereitstellen, die den Moodle-Webservice `core_completion_get_activities_completion_status` kapseln:

1. `GET /lms/course/<course_id>/student/<lms_user_id>/activitystatus` liefert für einen Kurs alle vom LMS gemeldeten Aktivitätsstatus einschließlich `cmid`, `state` und `timecompleted`.
2. `GET /lms/course/<course_id>/student/<lms_user_id>/learningElementId/<learning_element_id>/activitystatus` filtert diese Daten serverseitig auf exakt das angefragte Learning Element.

Beide Endpunkte **shall** ausschließlich die von Moodle gelieferten Completion-Daten serialisieren, lokale Kurs-/User-Zuordnungen über gespeicherte LMS-IDs auflösen und Fehler (Ungültige IDs, LMS-Timeouts, HTTP-Fehler) deterministisch behandeln, sodass Aufrufer:innen entweder eine valide Liste oder eine wohldefinierte Fehlermeldung erhalten.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und eine JSON-Liste von Objekten mit mindestens `cmid`, `state`, `timecompleted`; zusätzliche Felder aus Moodle dürfen unverändert enthalten bleiben.
- [x] Die Learning-Element-Variante reduziert die Antwort deterministisch auf den angefragten `cmid`; existiert der `cmid` nicht, wird eine leere Liste zurückgegeben.
- [x] Fehlerhafte LMS-Aufrufe (z. B. HTTP != 200 oder ungültiges JSON) führen zu einer strukturierten Fehlermeldung oder einer leeren Liste, ohne interne Tracebacks offenzulegen.
- [x] Beide Endpunkte verwenden die im Kursdatensatz hinterlegte `lms_id` sowie die `lms_user_id`, um den Moodle-Aufruf konsistent aufzubauen.
- [x] Client-seitige Fortschrittsberechnungen nutzen die gelieferten Statusdaten, reagieren auf Fehlerfälle deterministisch und ignorieren deaktivierte Klassifikationen (verifiziert durch "LearningPathTopicProgress tests").
- [x] UI-Progressleisten visualisieren die berechneten Werte inklusive Fehler- und Grenzfälle (verifiziert durch "StyledLinearProgress tests").

## Rationale

Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) verpflichtet das Backend, sämtliche im OAS beschriebenen Integrations-Endpunkte umzusetzen. Die Aktivitätsstatus-Endpunkte stellen sicher, dass Fortschritt und Completion-Daten aus Moodle in HASKI verfügbar sind, damit UI-Module (z. B. Kursübersichten, Lernpfadsteuerung) den Bearbeitungsstatus einzelner Learning Elements zuverlässig anzeigen können. Die automatisierten Tests `backend/tests/e2e/test_api.py::TestApi::test_get_activity_status_for_student` und `backend/tests/e2e/test_api.py::TestApi::test_get_activity_status_for_student_for_learning_element` validieren die Antwortstruktur.

## Hinweise

- Beide Endpunkte nutzen `services.get_activity_status_for_student_for_course` als Single Source of Truth und können von Caching/Retry-Strategien profitieren, falls das Moodle-API hohe Latenzen aufweist.
- Die Filterung nach `learning_element_id` erfolgt serverseitig; Aufrufer:innen müssen daher keine zusätzlichen Daten übertragen, was konsistente Sicherheitsprüfungen erleichtert.
