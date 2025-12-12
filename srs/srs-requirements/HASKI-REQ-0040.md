---
id: HASKI-REQ-0040
title: Zentrale Verwaltung des Lernpfad-Algorithmus-Katalogs
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
merged_from: ["HASKI-REQ-0041"]
links:
  parents: ["SyRS-FUNC-008", "SyRS-FUNC-002"]
  stories: ["HASKI-RAK/HASKI-Backend#83", "HASKI-RAK/HASKI-Frontend#306"]
  tests:
    [
      "backend/tests/e2e/test_api.py::TestApi::test_post_learning_path_algorithm",
    ]
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_student_learning_path_learning_element_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_p_student_learning_path_learning_element_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_teacher_learning_path_learning_element_algorithm"
    - path: "backend/tests/unit/test_service.py"
      name: "test_student_learning_path_learning_element_algorithm"
    - path: "frontend/src/components/CreateTopic/Table/CreateAlgorithm/CreateAlgorithmTable.test.tsx"
      name: "CreateAlgorithmTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateAlgorithm/CreateAlgorithmTable.hooks.test.tsx"
      name: "useCreateAlgorithmTable"
    - path: "frontend/src/components/CreateTopic/Modal/CreateAlgorithmsStep/CreateAlgorithmsStep.test.tsx"
      name: "CreateAlgorithmsStep"
    - path: "frontend/src/services/LearningPathAlgorithm/postLearningPathAlgorithm.test.tsx"
      name: "postLearningPathAlgorithm has expected behaviour"
    - path: "frontend/src/services/LearningPathLearningElementAlgorithm/fetchStudentLpLeAlgorithm.test.tsx"
      name: "fetchStudentLpLeAlg has expected behaviour"
    - path: "frontend/src/services/LearningPathLearningElementAlgorithm/fetchTeacherLpLeAlg.test.tsx"
      name: "fetchTeacherLpLeAlg has expected behaviour"
    - path: "frontend/src/services/LearningPathLearningElementAlgorithm/postStudentLpLeAlg.test.tsx"
      name: "postStudentLpLeAlg has expected behaviour"
    - path: "frontend/src/services/LearningPathLearningElementAlgorithm/postTeacherLpLeAlg.test.tsx"
      name: "postTeacherLpLeAlg has expected behaviour"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_path_algorithm"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_path_algorithm_by_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_path_algorithm_by_short_name"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_path_learning_element_algorithm"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_lpath_le_algorithm_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_learning_path_learning_element_algorithm"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_student_lpath_le_algorithm"
    - path: "HASKI-Frontend/src/store/Slices/StudentLpLeAlgSlice.test.ts"
      name: "StudentLpLeAlgSlice cache"
    - path: "HASKI-Frontend/src/store/Slices/TeacherLpLeAlgorithmSlice.test.ts"
      name: "TeacherLpLeAlgorithmSlice cache"
---

## Beschreibung

Das System **shall** einen kanonischen Katalog der verfügbaren Lernpfad-Algorithmen bereitstellen, der über abgesicherte Backend-Endpunkte verwaltet wird. Administrator:innen und Tutor:innen **shall** neue Algorithmen mit einem eindeutigen `short_name` und einer sprechenden Bezeichnung registrieren können, damit Studierende und Lehrende dieselbe Referenz verwenden, wenn sie Lernpfade konfigurieren oder einen Algorithmus selektieren. Persistierte Algorithmen **shall** sofort für nachgelagerte Endpunkte (z.B. Auswahl eines Standard- oder individuellen Lernpfads) zur Verfügung stehen.

Aufbauend auf diesem Katalog **shall** das System es authentifizierten Studierenden ermöglichen, für jedes ihrer belegten Topics einen bevorzugten Lernpfad-Algorithmus zu wählen, sowie Tutor:innen erlauben, Standard-Algorithmen und Overrides pro Topic zu konfigurieren. Die Auswahlen **shall** persistent als Relationen `student_id`–`topic_id`–`learning_path_algorithm_id` verwaltet werden und unmittelbar bei der nächsten Lernpfadberechnung berücksichtigt werden. Wird keine individuelle Auswahl getroffen, **shall** automatisch der von Tutor:innen vorgegebene Standard-Algorithmus gelten; Tutor:innen-Overrides **shall** studentische Präferenzen deterministisch übersteuern und können kontrolliert zurückgenommen werden.

## Akzeptanzkriterien

### Algorithmus-Katalog

- [ ] Ein REST-Endpunkt `POST /algorithm` akzeptiert die Pflichtfelder `short_name` (URI-tauglicher Schlüssel) und `full_name` (Anzeigename) und liefert bei Erfolg HTTP 201 mit den persistierten Werten sowie einer internen ID zurück.
- [ ] Fehlende oder falsch typisierte Pflichtfelder führen zu einer Validierungsantwort (HTTP 400) mit erzwingender Fehlermeldung; keine inkonsistenten Datensätze werden gespeichert.
- [ ] Der `short_name` ist systemweit eindeutig; doppelte Einträge werden mit HTTP 409/400 abgelehnt, ohne bestehende Algorithmen zu überschreiben.
- [ ] Neu erfasste Algorithmen sind unmittelbar in den Auswahl- und Konfigurations-Endpunkten für Lernpfade verfügbar (z.B. `POST /student/<id>/topic/<id>/algorithm`).
- [ ] Der Endpunkt ist mit der bestehenden Rollen-/Rechteprüfung geschützt, sodass nur autorisierte Rollen (Kursersteller:innen, Tutor:innen, Admins) den Katalog verändern können.
- [ ] Alle erfolgreichen und fehlgeschlagenen Katalogänderungen werden serverseitig protokolliert, damit Konfigurationsfehler nachvollziehbar bleiben.

### Algorithmuszuweisung pro Topic und Studierenden

- [x] Ein abgesicherter REST-Endpunkt `POST /student/<student_id>/topic/<topic_id>/algorithm` akzeptiert den Payload `{ "algorithm": "<short_name>" }`, validiert den `short_name` gegen den Algorithmus-Katalog und liefert bei Erfolg HTTP 201 mitsamt `id`, `student_id`, `topic_id` und `algorithm_id` zurück.
- [x] Fehlende Felder, ungültige Kurzbezeichner oder fehlende Berechtigungen führen zu einer Validierungs- bzw. Autorisierungsantwort (HTTP 400/401) ohne neue Relationseinträge zu erzeugen.
- [x] Bei Erstellung eines Topics oder einer neuen Einschreibung wird automatisch eine Relation mit dem aktuell von Tutor:innen gesetzten Standard-Algorithmus angelegt, sodass Studierende ohne manuelle Aktion eine gültige Konfiguration besitzen.
- [x] Tutor:innen können ein Override setzen oder zurücknehmen; bei einem aktiven Override sind studentische Änderungsversuche gesperrt (HTTP 409/423), nach dem Zurücknehmen sind individuelle Änderungen sofort wieder erlaubt und werden persistiert.
- [x] Jede Änderung (Erstellung, Aktualisierung, abgelehnte Änderung) wird protokolliert und kann über den Traceability-Monitor nachvollzogen werden.

### Frontend-Steuerung (Algorithmus-UI)

- [x] Alle Topics eines Kurses werden mit sprechenden Namen und zugehörigen Learning Elements in einer Algorithmus-Tabelle dargestellt.
- [x] Zu jedem Topic steht eine Auswahl der unterstützten Algorithmen (z. B. Fixed Order, Graf, ACO, GA) zur Verfügung.
- [x] Wird ein Algorithmus geändert, aktualisiert die Oberfläche den gespeicherten Zustand und informiert die Backend-Schnittstelle über die neue Auswahl.
- [x] Topics ohne vorbereitete Klassifikation deaktivieren die Auswahl automatisch, sodass nur konsistente Konfigurationen gespeichert werden.
- [x] Temporär nicht verfügbare Topics werden mit Skeleton-Elementen dargestellt, bis die Daten aus dem Backend vorliegen.
- [x] Der Create-Topic-Modal-Schritt `CreateAlgorithmsStep` blockiert den Abschluss, bis für alle importierten Topics ein Algorithmus ausgewählt wurde.

## Rationale

GitHub Issue [#83](https://github.com/HASKI-RAK/HASKI-Backend/issues/83) verlangt, dass Studierende einen Lernpfad-Algorithmus aus einer definierten Liste wählen können und Tutor:innen Standardalgorithmen für Topics vorgeben dürfen. Ein konsistenter Algorithmus-Katalog mit eindeutigen Kurzbezeichnern stellt sicher, dass alle Auswahl- und Berechnungsendpunkte dieselben Referenzen verwenden. Die Funktionalität wird durch den End-to-End-Test `backend/tests/e2e/test_api.py::TestApi::test_post_learning_path_algorithm` verifiziert, der die erfolgreiche Registrierung eines neuen Algorithmus prüft.

## Hinweise

- Beispiel-Payload: `{ "short_name": "aco", "full_name": "Ant Colony Optimization" }`. Die Antwort enthält `id`, `short_name` und `full_name`.
- Die Persistenz erfolgt in der Tabelle `learning_path_algorithm` (oder äquivalent) und dient als Foreign-Key-Ziel für studentische und tutorielle Auswahlrelationen.
- Beim Deployment sollen Default-Einträge (z.B. "aco", "graf", "ga") per Seed-Daten verfügbar sein; der Endpunkt ergänzt diese Liste um neue Verfahren.
- Bei Erweiterungen ist sicherzustellen, dass API-Schemata der Frontends (z.B. AlgorithmSettingsModal) unverändert konsumierbar bleiben.
