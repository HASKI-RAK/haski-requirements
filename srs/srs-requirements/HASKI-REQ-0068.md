---
id: HASKI-REQ-0068
title: Remote-LMS-Kursinhalte abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-005
links:
  parents: ["SyRS-INT-005"]
  stories: ["HASKI-RAK/HASKI-Backend#30"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_remote_course_content"
    - path: "HASKI-Frontend/src/services/RemoteTopics/fetchRemoteTopics.test.tsx"
      name: "fetchRemoteTopics has expected behaviour"
    - path: "HASKI-Frontend/src/store/Slices/RemoteTopicSlice.test.tsx"
      name: "RemoteTopicSlice"
---

## Beschreibung

Das Backend **shall** einen GET-Endpunkt `GET /lms/remote/course/<course_id>/content` bereitstellen, der die aus dem Moodle-LMS gelieferten Kurssektionen inklusive aller Module (Learning Elements) unverändert an HASKI-Clients zurückgibt. Vor dem Abruf **shall** die Kurs-ID validiert und die Moodle-Webservice-Anfrage ausgeführt werden; fehlerhafte Antworten (HTTP-Fehler, invalide JSON-Strukturen) **shall** deterministisch behandelt werden. Jedes Topic-Objekt **shall** mindestens `topic_lms_id`, `topic_lms_name` und eine Liste `lms_learning_elements` enthalten, wobei jedes Learning Element die Felder `lms_id`, `lms_learning_element_name` und `lms_activity_type` bereitstellt, damit Import- und Scaffolding-Funktionen vollständige Metadaten besitzen.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und eine Liste von Topic-Objekten mit den oben genannten Pflichtfeldern.
- [x] Jedes Topic enthält eine nicht-leere Liste `lms_learning_elements`, deren Einträge mindestens `lms_id`, `lms_learning_element_name`, `lms_activity_type` umfassen und beliebige Zusatzfelder aus Moodle beibehalten.
- [x] Ungültige oder nicht erreichbare Moodle-Kurse führen zu einer strukturierten Fehlermeldung (HTTP 404/502), ohne interne Stacktraces preiszugeben.
- [x] Der Endpunkt kapselt Netz-/Authentifizierungsfehler von Moodle und schreibt Fehlversuche in die Betriebslogs.

## Rationale

Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) verlangt, dass alle im neuen OAS beschriebenen Integrations-Endpunkte bereitstehen. Die Kursinhalt-API ist Voraussetzung, um Moodle-Strukturen in HASKI-Themen und Learning Elements zu überführen und bildet damit die Grundlage für weitere Anforderungen (z. B. HASKI-REQ-0036/HASKI-REQ-0037). `backend/tests/e2e/test_api.py::TestApi::test_get_remote_course_content` bestätigt das Antwortschema und die Feldabdeckung.

## Hinweise

- Die Funktionalität nutzt denselben Moodle-Proxy wie der Kurslisten-Endpunkt und sollte identische Timeout-/Retry-Strategien verwenden.
- Erweiterungen wie Paging oder Filter nach Abschnittsstatus sind möglich, solange die Mindestfelder unverändert bereitgestellt und Fehlermeldungen konsistent bleiben.
