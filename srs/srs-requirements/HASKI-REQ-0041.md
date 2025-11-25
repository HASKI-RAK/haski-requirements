---
id: HASKI-REQ-0041
title: Studierende konfigurieren Lernpfad-Algorithmen pro Topic
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-002
links:
  parents: ["SyRS-FUNC-002"]
  stories: ["HASKI-RAK/HASKI-Backend#83"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_student_learning_path_learning_element_algorithm"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_p_student_learning_path_learning_element_algorithm"
---

## Beschreibung

Das System **shall** authentifizierten Studierenden ermöglichen, für jedes ihrer belegten Topics einen bevorzugten Lernpfad-Algorithmus aus dem zentralen Algorithmus-Katalog auszuwählen. Die Auswahl **shall** persistent als Relation `student_id`–`topic_id`–`learning_path_algorithm_id` gespeichert werden und unmittelbar bei der nächsten Lernpfadberechnung berücksichtigt werden. Wird keine individuelle Auswahl getroffen, **shall** automatisch der von Tutor:innen vorgegebene Standard-Algorithmus gelten und als Initialwert in der Relation abgelegt werden. Änderungen durch Tutor:innen (z.B. Override oder Reset) **shall** deterministisch auf die studentische Auswahl propagiert werden, sodass keine divergierenden Zustände entstehen.

## Akzeptanzkriterien

- [ ] Ein abgesicherter REST-Endpunkt `POST /student/<student_id>/topic/<topic_id>/algorithm` akzeptiert den Payload `{ "algorithm": "<short_name>" }`, validiert den `short_name` gegen den Algorithmus-Katalog und liefert bei Erfolg HTTP 201 mitsamt `id`, `student_id`, `topic_id` und `algorithm_id` zurück.
- [ ] Fehlende Felder, ungültige Kurzbezeichner oder fehlende Berechtigungen führen zu einer Validierungs- bzw. Autorisierungsantwort (HTTP 400/401) ohne neue Relationseinträge zu erzeugen.
- [ ] Bei Erstellung eines Topics oder einer neuen Einschreibung wird automatisch eine Relation mit dem aktuell von Tutor:innen gesetzten Standard-Algorithmus angelegt, sodass Studierende ohne manuelle Aktion eine gültige Konfiguration besitzen.
- [ ] Tutor:innen können ein Override setzen oder zurücknehmen; bei einem aktiven Override sind studentische Änderungsversuche gesperrt (HTTP 409/423), nach dem Zurücknehmen sind individuelle Änderungen sofort wieder erlaubt und werden persistiert.
- [ ] Jede Änderung (Erstellung, Aktualisierung, abgelehnte Änderung) wird protokolliert und kann über den Traceability-Monitor nachvollzogen werden.

## Rationale

GitHub Issue [#83](https://github.com/HASKI-RAK/HASKI-Backend/issues/83) beschreibt die Notwendigkeit, dass Studierende den für sie passenden Lernpfad-Algorithmus auswählen können, während Tutor:innen bei Bedarf Standard-Algorithmen oder Overrides für einzelne Topics setzen. Die Relation `student_topic_learning_path_algorithm` stellt sicher, dass Lernpfadberechnungen konsistent auf aktuelle Präferenzen zugreifen. Die End-to-End-Prüfungen `backend/tests/e2e/test_api.py::TestApi::test_post_student_learning_path_learning_element_algorithm` (direkter `POST /student/<student_id>/topic/<topic_id>/algorithm`-Aufruf) und `backend/tests/e2e/test_api.py::TestApi::test_p_student_learning_path_learning_element_algorithm` (LMS-gebundener Pfad `POST /user/<student_id>/<lms_user_id>/course/<course_id>/topic/<topic_id>/studentAlgorithm`) verifizieren beide API-Varianten und stellen sicher, dass die Persistierung sowie das Antwortschema konsistent umgesetzt sind.

## Hinweise

- Die Endpoint-Implementierung wiederverwendet bestehende Rollen- und Permission-Decoratoren, sodass nur der betroffene Studierende oder autorisierte Lehrende/Administrator:innen die Auswahl ändern können.
- Die Datenbank benötigt Foreign-Key-Constraints auf `student`, `topic` und `learning_path_algorithm`, um inkonsistente Kombinationen auszuschließen.
- Frontend-Komponenten (z.B. AlgorithmSettingsModal) konsumieren die API über denselben `short_name`, wodurch der Wechsel zwischen adaptivem und selbstgesteuertem Modus transparent bleibt.
- Beim Reset eines Overrides soll der zuvor gewählte studentische Algorithmus reaktiviert werden, sofern er weiterhin verfügbar ist; andernfalls greift der Standard aus dem Katalog.
