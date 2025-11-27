---
id: HASKI-REQ-0062
title: Learning Elements eines Topics abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#21", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_les_for_topic_for_student"
---

## Beschreibung

Das System **shall** eingeschriebenen Studierenden über `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic/<topic_id>/learningElement` sämtliche Learning Elements eines Topics zurückliefern. Die Antwort **shall** den Schlüssel `learning_elements` mit Einträgen liefern, die mindestens `id`, `lms_id`, `activity_type`, `classification`, `name`, `university` und den Lernfortschrittskontext `student_learning_element` enthalten, damit adaptive Lernpfade, Dashboards und Empfehlungssysteme identische Datensichten verwenden.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten `learning_elements` inklusive der genannten Felder.
- [x] Ungültige Studierenden-, Kurs- oder Topic-IDs resultieren in HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Topic-Zugriffe werden nur gestattet, wenn der Studierende für den Kurs eingeschrieben ist; andernfalls 404.
- [x] Die Route nutzt dieselbe Moodle-ID- und Rollenlogik wie die übrigen Kurs-/Topic-Endpunkte und bleibt konsistent mit dem OAS-Schema aus GH-30.

## Rationale

GitHub Issue [#21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) fordert, dass Kursinhalte aus Moodle in das HASKI-Backend übernommen und kontextsensitiv ausgeliefert werden. Für Lernpfade und Tracking benötigen Clients Zugriff auf die Learning-Element-Liste eines Topics inklusive Lernfortschritt. Ohne diesen Endpoint müssten Frontends eigenständig filtern oder mehrere Routen kombinieren, was zu Inkonsistenzen führt. Der Endpoint stellt sicher, dass alle Lern- und Analytics-Funktionen denselben konsistenten Datenpool erhalten.

## Hinweise

- Der Endpoint kann leer zurückgeben, falls für das Topic keine Learning Elements existieren.
- Antwortschema ist Grundlage für Frontend-Komponenten wie Topic-Detailseiten und den Lernpfadgraphen.
- Fehler- und Logging-Mechanismen sollen diejenigen aus HASKI-REQ-0056 widerspiegeln, um Debugging zu vereinheitlichen.
