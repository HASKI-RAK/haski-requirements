---
id: HASKI-REQ-0082
title: Moodle-Kursobjekte löschen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003"]
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Backend#121"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_delete_le_from_moodle"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_delete_topic_from_moodle"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_delete_course_from_moodle"
    - path: "HASKI-Frontend/src/services/Course/deleteCourse.test.ts"
      name: "deleteCourse has expected behaviour"
    - path: "HASKI-Frontend/src/services/Topic/deleteTopic.test.tsx"
      name: "deleteTopic has expected behaviour"
---

## Beschreibung

Das Backend **shall** für alle von Moodle synchronisierten Kursobjekte (`course`, `topic`, `learningElement`) je einen abgesicherten `DELETE`-Endpunkt bereitstellen, damit entfernte Inhalte auch in HASKI verschwinden. Jeder Endpunkt **shall** die Kombination aus interner HASKI-ID und korrespondierender Moodle-ID validieren, bevor Datensätze gelöscht werden, und anschließend eine Bestätigung (`{"message": ...}`) zurückgeben. Während des Löschens **shall** abhängige Strukturen (Subtopics, Learning Elements, Ratings) gemäß Issue #121 konsistent bereinigt werden, sodass keine verwaisten Referenzen verbleiben.

## Akzeptanzkriterien

- [x] `DELETE /lms/learningElement/<learning_element_id>/<moodle_learning_element_id>` entfernt das adressierte Learning Element mitsamt abhängigen Ratings und liefert HTTP 200 mit Bestätigungsnachricht; nicht vorhandene IDs führen zu HTTP 404 mit standardisierter Fehlstruktur (`{"error": "...", "message": "..."}`).
- [x] `DELETE /lms/topic/<topic_id>/<moodle_topic_id>` entfernt Topics oder Subtopics inklusive ihrer Learning Elements bzw. Subrelations; Fehlzuordnungen resultieren deterministisch in HTTP 404.
- [x] `DELETE /lms/course/<course_id>/<moodle_course_id>` bereinigt Kurs-Stammdaten sowie alle zugehörigen Topics/Subtopics und bestätigt den Erfolg mit HTTP 200.
- [x] Alle Delete-Operationen sind transaktional und führen bei Fehlern zu einem vollständigen Rollback, sodass Teil-Löschungen ausgeschlossen werden.

## Rationale

GitHub Issue [#21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) definiert die CRUD-Schnittstellen für Kursstrukturen; das Löschen der Objekte stellt sicher, dass HASKI die Moodle-Quelle exakt spiegelt. Issue [#121](https://github.com/HASKI-RAK/HASKI-Backend/issues/121) ergänzt, dass abhängige Rating-Daten entfernt werden müssen, wenn Lernobjekte gelöscht werden. Die E2E-Tests `backend/tests/e2e/test_api.py::TestApi::test_api_delete_le_from_moodle`, `backend/tests/e2e/test_api.py::TestApi::test_api_delete_topic_from_moodle` und `backend/tests/e2e/test_api.py::TestApi::test_api_delete_course_from_moodle` verifizieren diese Delete-Flows inklusive Fehlerszenarien.

## Hinweise

- Delete-Operationen sollen Ereignisse in den Integrations-Logs protokollieren, um divergierende Stände zwischen Moodle und HASKI nachvollziehen zu können.
- Administrator:innen sollten Batch-Löschungen bevorzugt in der Reihenfolge Course → Topic → Learning Element anstoßen; die Endpoints unterstützen aber auch Einzeloperationen.
