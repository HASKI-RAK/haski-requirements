---
id: HASKI-REQ-0053
title: Studierendenkurse über REST abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#131", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_student_courses"
---

## Beschreibung

Das System **shall** einen abgesicherten Endpoint `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course` bereitstellen, der für authentifizierte Rollen ausschließlich die Kurse eines Studierenden zurückliefert, in denen er oder sie laut LMS (Moodle) eingeschrieben ist. Die Route **shall** Moodle-IDs deterministisch auf HASKI-Studenten abbilden und nur jene Kursobjekte serialisieren, die den Autorisierungsregeln aus GH-131 entsprechen. Die Antwort **shall** pro Kurs die Metadaten (`id`, `lms_id`, `name`, `university`) enthalten, damit Lernräume und Dashboards die verfügbaren Kurse ohne zusätzliche Backendschritte darstellen können.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten eine `courses`-Liste mit mindestens den Schlüsseln `id`, `lms_id`, `name`, `university` für jeden Kurs, dem der Studierende zugeordnet ist.
- [x] Studierende sehen ausschließlich eigene Kurse; falsche Kombinationen aus `student_id` und `lms_user_id` führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Die Route übernimmt ihre Daten direkt aus den durch GH-131 gepflegten `student_course`-Zuordnungen und reflektiert Aktualisierungen ohne zusätzliche Sync-Schritte.
- [x] Der Endpoint folgt der im OAS aus GH-30 dokumentierten Struktur, damit Frontends und Analytics-Komponenten Konsistenz sicherstellen können.

## Rationale

SyRS-FUNC-008 verlangt konfigurierbare Lernräume pro Studierendem. Damit Nutzer:innen zwischen Kurskontexten wechseln können, muss das Backend eine gefilterte Kursliste bereitstellen, die ausschließlich belegte Veranstaltungen umfasst. GitHub issue GH-131 definiert die Zugangsbeschränkungen für diese Kursliste, während GH-30 die OAS-Baseline für sämtliche Kurs-Endpunkte liefert.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/131
- Supporting issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Der Endpoint teilt sich den Pfad mit Kurs-spezifischen Unterrouten (Topics, Learning Elements); Konsistenz der Autorisierungschecks ist zwingend sicherzustellen.
