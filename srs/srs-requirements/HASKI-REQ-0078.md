---
id: HASKI-REQ-0078
title: Moodle-Einschreibungen bulkweise übernehmen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  stories:
    [
      "HASKI-RAK/HASKI-Backend#131",
      "HASKI-RAK/HASKI-Frontend#81",
      "HASKI-RAK/HASKI-Frontend#368",
    ]
  parents: ["SyRS-INT-003"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_add_all_students_to_course"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_add_all_students_to_topics"
---

## Beschreibung

Das Backend **shall** automatisierte Sync-Endpunkte bereitstellen, die alle in Moodle eingeschriebenen Studierenden für einen Kurs samt zugehöriger Topics in HASKI spiegeln. `POST /course/<course_id>/allStudents` **shall** jede gültige Moodle-Einschreibung prüfen, fehlende `student_course`-Relationen anlegen und eine aggregierte Quittung (`CREATED`, `course_id`, `student_count`) zurückgeben. Ergänzend **shall** `POST /course/<course_id>/topics/allStudents` sicherstellen, dass alle in HASKI erfassten Topics dieses Kurses dieselben Studierenden-Zuordnungen erhalten, damit Fortschritts- und Empfehlungsläufe sofort auf Topic-Ebene starten können.

## Akzeptanzkriterien

- [x] Erfolgreicher Kurs-Sync liefert HTTP 201 und gibt `CREATED: true`, die Kurs-ID sowie die Anzahl neu verknüpfter Studierender aus; ohne neue Zuordnungen wird HTTP 404 mit `CREATED: false` zurückgegeben.
- [x] Für jeden verarbeiteten Studierenden wird geprüft, ob die Moodle-Einschreibung zur Hochschule/Kurs-ID passt; Inkonsistenzen erzeugen keinen Eintrag und werden geloggt.
- [x] Topic-Sync ruft `services.add_student_to_topics` für alle neu verknüpften Studierenden auf und meldet analog `CREATED`, `course_id`, `student_count`.
- [x] Beide Endpunkte sind idempotent: wiederholte Aufrufe ohne neue LMS-Einschreibungen erzeugen keine Dubletten und melden `CREATED: false`.
- [x] Fehlerhafte Kurs-IDs oder fehlende Referenzdaten lösen nachvollziehbare HTTP-Fehler (z. B. 404) aus, ohne interne Informationen preiszugeben.

## Rationale

GitHub Issue GH-131 fordert, dass Studierende ausschließlich die Kurse sehen, in denen sie in Moodle tatsächlich eingeschrieben sind. Ein manueller Einzelimport wäre fehleranfällig; daher synchronisiert HASKI über Bulk-Endpunkte regelmäßig alle betroffenen Kurse und Topics, um Zugang, Lernpfade und Empfehlungen konsistent zu halten.

## Hinweise

- Die Endpunkte verwenden bestehende Servicefunktionen (`get_all_students`, `get_enrolled_university_courses`, `add_student_to_course`, `add_student_to_topics`), sodass Validierungs- und Logging-Standards wiederverwendet werden.
- Ergebnisse sollten für Monitoring-Zwecke geloggt werden (insb. `student_count`), um Integrationsprobleme früh zu erkennen.
