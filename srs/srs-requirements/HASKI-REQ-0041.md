---
id: HASKI-REQ-0041
title: Algorithmuszuweisung pro Topic
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-002
links:
  parents: ["SyRS-FUNC-002"]
  stories:
    - "HASKI-RAK/HASKI-Backend#83"
    - "HASKI-RAK/HASKI-Frontend#306"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_student_learning_path_learning_element_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_p_student_learning_path_learning_element_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_teacher_learning_path_learning_element_algorithm"
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
---

## Beschreibung

Das System **shall** authentifizierten Studierenden ermöglichen, für jedes ihrer belegten Topics einen bevorzugten Lernpfad-Algorithmus aus dem zentralen Algorithmus-Katalog auszuwählen. Die Auswahl **shall** persistent als Relation `student_id`–`topic_id`–`learning_path_algorithm_id` gespeichert werden und unmittelbar bei der nächsten Lernpfadberechnung berücksichtigt werden. Wird keine individuelle Auswahl getroffen, **shall** automatisch der von Tutor:innen vorgegebene Standard-Algorithmus gelten und als Initialwert in der Relation abgelegt werden. Lehrende **shall** im Frontend pro Topic eine Algorithmuswahloberfläche erhalten, um Standard-Algorithmen zu konfigurieren; diese UI spiegelt vorhandene Learning Elements, verhindert unvollständige Konfigurationen und synchronisiert Änderungen mit dem Backend. Änderungen durch Tutor:innen (z. B. Override oder Reset) **shall** deterministisch auf studentische Präferenzen propagiert werden, sodass keine divergierenden Zustände entstehen.

## Akzeptanzkriterien

### Backend-Konfiguration (GH-83)

- [x] Ein abgesicherter REST-Endpunkt `POST /student/<student_id>/topic/<topic_id>/algorithm` akzeptiert den Payload `{ "algorithm": "<short_name>" }`, validiert den `short_name` gegen den Algorithmus-Katalog und liefert bei Erfolg HTTP 201 mitsamt `id`, `student_id`, `topic_id` und `algorithm_id` zurück.
- [x] Fehlende Felder, ungültige Kurzbezeichner oder fehlende Berechtigungen führen zu einer Validierungs- bzw. Autorisierungsantwort (HTTP 400/401) ohne neue Relationseinträge zu erzeugen.
- [x] Bei Erstellung eines Topics oder einer neuen Einschreibung wird automatisch eine Relation mit dem aktuell von Tutor:innen gesetzten Standard-Algorithmus angelegt, sodass Studierende ohne manuelle Aktion eine gültige Konfiguration besitzen.
- [x] Tutor:innen können ein Override setzen oder zurücknehmen; bei einem aktiven Override sind studentische Änderungsversuche gesperrt (HTTP 409/423), nach dem Zurücknehmen sind individuelle Änderungen sofort wieder erlaubt und werden persistiert.
- [x] Jede Änderung (Erstellung, Aktualisierung, abgelehnte Änderung) wird protokolliert und kann über den Traceability-Monitor nachvollzogen werden.

### Frontend-Steuerung (GH-306)

- [x] Alle Topics eines Kurses werden mit sprechenden Namen und zugehörigen Learning Elements in einer Algorithmus-Tabelle dargestellt.
- [x] Zu jedem Topic steht eine Auswahl der unterstützten Algorithmen (z. B. Fixed Order, Graf, ACO, GA) zur Verfügung.
- [x] Wird ein Algorithmus geändert, aktualisiert die Oberfläche den gespeicherten Zustand und informiert die Backend-Schnittstelle über die neue Auswahl.
- [x] Topics ohne vorbereitete Klassifikation deaktivieren die Auswahl automatisch, sodass nur konsistente Konfigurationen gespeichert werden.
- [x] Temporär nicht verfügbare Topics werden mit Skeleton-Elementen dargestellt, bis die Daten aus dem Backend vorliegen.
- [x] Der Create-Topic-Modal-Schritt `CreateAlgorithmsStep` blockiert den Abschluss, bis für alle importierten Topics ein Algorithmus ausgewählt wurde.

## Rationale

GitHub Issue [#83](https://github.com/HASKI-RAK/HASKI-Backend/issues/83) beschreibt die Notwendigkeit, dass Studierende den für sie passenden Lernpfad-Algorithmus auswählen können, während Tutor:innen bei Bedarf Standard-Algorithmen oder Overrides für einzelne Topics setzen. Issue [#306](https://github.com/HASKI-RAK/HASKI-Frontend/issues/306) liefert die dazugehörige Frontend-Oberfläche. Die Relation `student_topic_learning_path_algorithm` stellt sicher, dass Lernpfadberechnungen konsistent auf aktuelle Präferenzen zugreifen. Die End-to-End-Prüfungen `backend/tests/e2e/test_api.py::TestApi::test_post_student_learning_path_learning_element_algorithm` (direkter `POST /student/<student_id>/topic/<topic_id>/algorithm`-Aufruf) und `backend/tests/e2e/test_api.py::TestApi::test_p_student_learning_path_learning_element_algorithm` (LMS-gebundener Pfad `POST /user/<student_id>/<lms_user_id>/course/<course_id>/topic/<topic_id>/studentAlgorithm`) verifizieren beide API-Varianten und stellen sicher, dass die Persistierung sowie das Antwortschema konsistent umgesetzt sind.

## Hinweise

- Die Endpoint-Implementierung wiederverwendet bestehende Rollen- und Permission-Decoratoren, sodass nur der betroffene Studierende oder autorisierte Lehrende/Administrator:innen die Auswahl ändern können.
- Die Datenbank benötigt Foreign-Key-Constraints auf `student`, `topic` und `learning_path_algorithm`, um inkonsistente Kombinationen auszuschließen.
- Die Algorithmen-Auswahl im Frontend nutzt die Übersetzungen aus `AlgorithmSettingsModal.algorithms` und synchronisiert Änderungen über `useCreateAlgorithmTable`.
- Beim Reset eines Overrides soll der zuvor gewählte studentische Algorithmus reaktiviert werden, sofern er weiterhin verfügbar ist; andernfalls greift der Standard aus dem Katalog.
- Der `CreateAlgorithmsStep` im Topic-Modal erzwingt eine vollständige Zuordnung, bevor neue Topics importiert werden können.
