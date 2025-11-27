---
id: HASKI-REQ-0066
title: Lehrkraft-Kursübersicht abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-016
links:
  parents: ["SyRS-FUNC-016"]
  stories: ["HASKI-RAK/HASKI-Backend#21"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_courses_by_teacher_id"
---

## Beschreibung

Das Backend **shall** einen authentifizierten GET-Endpunkt `GET /user/<user_id>/<lms_user_id>/teacher/<teacher_id>/course` bereitstellen, der einer verifizierten Lehrkraft ausschließlich die Kurse liefert, denen sie laut Moodle/HASKI-Zuordnung zugewiesen ist. Vor der Auslieferung **shall** die Schnittstelle sowohl die HASKI-User-ID als auch die Moodle-LMS-ID validieren und bei fehlender Zuordnung deterministisch abbrechen. Jede Kursantwort **shall** mindestens die Felder `id`, `name` und `lms_id` enthalten, damit didaktische Dashboards und Kurskonfiguratoren eine konsistente Ausgangsbasis besitzen.

## Akzeptanzkriterien

- [x] Erfolgreiche Anfragen liefern HTTP 200 und ein JSON-Objekt mit dem Key `courses`, dessen Elemente ausschließlich Kurse der angeforderten Lehrkraft enthalten.
- [x] Jede Kursrepräsentation beinhaltet mindestens `id`, `name` und `lms_id`; zusätzliche Felder verletzen keine Datenschutzvorgaben.
- [x] Fehlende oder inkonsistente Lehrkraft-IDs führen zu HTTP 404 und einer generischen Fehlermeldung mit den Keys `error` und `message`.
- [x] Die Endpoint-Implementierung prüft Lehrkraft- und Kurszuordnungen bevor Datenmaterial aggregiert wird und protokolliert beide Fehlermodi.

## Rationale

GitHub Issue [#21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) definiert die grundlegenden CRUD-Funktionen für Kurse und deren Rollenzuordnung. Lehrkräfte benötigen eine gefilterte Kursübersicht, um Lernräume, Scaffolding-Elemente und Evaluationsaufgaben effizient zu verwalten. Die Anforderung stellt sicher, dass nach erfolgter Zuordnung (vgl. HASKI-REQ-0038) auch die darauf basierende Lesefunktion implementiert, getestet und nachvollziehbar dokumentiert ist.

## Hinweise

- Endpoint folgt derselben Pfadstruktur und Authentifizierung wie andere rollenbasierte Nutzerendpunkte (`/user/<user_id>/<lms_user_id>/...`).
- Die Antwortstruktur ist kompatibel zu Frontend-Komponenten, welche Kurslisten für Lehrkräfte rendern.
- Weitere Filter (Semester, Status) können auf dem bestehenden JSON-Schema aufsetzen, sofern sie die oben genannten Garantien nicht verletzen.
