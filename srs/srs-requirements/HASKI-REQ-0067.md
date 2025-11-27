---
id: HASKI-REQ-0067
title: Remote-LMS-Kursliste abrufen
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
      name: "TestApi::test_get_remote_courses"
---

## Beschreibung

Das Backend **shall** einen authentifizierten GET-Endpunkt `GET /lms/user/<user_id>/remote/courses` bereitstellen, der anhand der gespeicherten Moodle-LMS-ID alle vom Nutzer belegten Kurse aus dem angebundenen Moodle-System abruft und als JSON-Liste weitergibt. Vor dem Proxy-Aufruf **shall** die HASKI-User-ID validiert sowie die zugehörige `lms_user_id` geladen werden; schlägt einer der Schritte fehl, wird kein Moodle-Request ausgeführt. Jede Kursantwort **shall** mindestens die Felder `id`, `shortname`, `fullname`, `startdate`, `enddate`, `timecreated` und `timemodified` enthalten, sodass Kursimport- und Scaffolding-Workflows alle Metadaten vollständig erhalten.

## Akzeptanzkriterien

- [x] Erfolgreiche Anfragen liefern HTTP 200 sowie ein JSON-Array, dessen Elemente die oben genannten Pflichtfelder enthalten.
- [x] Der Endpunkt nutzt die hinterlegte `lms_user_id` des authentifizierten Nutzers und gibt ausschließlich dessen Moodle-Kurse zurück.
- [x] Fehlerhafte HASKI-User-IDs oder ungültige LMS-Zuordnungen führen zu einer deterministischen Fehlermeldung (z. B. HTTP 404 oder 400) ohne Weitergabe sensibler Daten.
- [x] Der Endpunkt kapselt Moodle-Fehler (z. B. Netz- oder Authentifizierungsprobleme) und liefert eine aussagekräftige Fehlermeldung an den Client.

## Rationale

GitHub Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) fordert die Implementierung sämtlicher im aktualisierten OAS beschriebenen Backend-Endpunkte. Die Remote-Kursliste bildet die Grundlage für Kursimporte, Kurskonfigurationen sowie Scaffolding-Workflows, weil nur so alle im LMS existierenden Kurse sichtbar und auswählbar sind. Das Verhalten wird durch `backend/tests/e2e/test_api.py::TestApi::test_get_remote_courses` abgesichert, das die vollständige Feldausprägung der Moodle-Antwort prüft.

## Hinweise

- Die Route nutzt dieselbe Authentifizierungs- und Pfadstruktur wie andere `/lms/user/<user_id>/…`-Endpunkte und kann dadurch identisch abgesichert werden.
- Der Proxy-Aufruf gegen Moodle erfolgt über `services.get_courses_for_user_from_moodle`; Timeout- und Fehlerbehandlung müssen zentral geloggt werden, um Integrationsprobleme nachvollziehen zu können.
- Erweiterungen wie Paging oder zusätzliche Filter (Semester, Sichtbarkeit) dürfen hinzugefügt werden, solange die Mindestfelder und Sicherheitsgarantien bestehen bleiben.
