---
id: HASKI-REQ-0054
title: Einzelnen Studierendenkurs abrufen
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
      name: "TestApi::test_get_student_course"
---

## Beschreibung

Das System **shall** einen Endpoint `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>` bereitstellen, der die vollständigen Metadaten eines konkreten Kurses zurückliefert, sofern der Studierende laut LMS (Moodle) eingeschrieben ist. Die Route **shall** Autorisierung gemäß GH-131 enforce und bei fehlenden Zuordnungen deterministisch mit 404 reagieren. Zur Unterstützung konfigurierbarer Lernräume (SyRS-FUNC-008) **shall** die Antwort mindestens `id`, `name`, `lms_id` und `university` enthalten, damit Frontends Kursdetails ohne zusätzliche Queries darstellen können.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 mitsamt allen Kursmetadaten (`id`, `name`, `lms_id`, `university`).
- [x] Ungültige Studierenden- oder Kursreferenzen (inkl. IDs, zu denen keine Einschreibung existiert) führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Der Endpoint nutzt dieselbe Moodle-ID-Mapping-Logik wie die Kursliste und bezieht seine Daten direkt aus den `student_course`-Zuordnungen, wodurch Änderungen aus GH-131 sofort sichtbar werden.
- [x] Die Antwort entspricht dem in GH-30 dokumentierten OAS-Schema, damit Frontend- und Analytics-Komponenten konsistent bleiben.

## Rationale

Konfigurierbare Lernräume benötigen nicht nur eine Kursliste, sondern auch Detailinformationen pro Kurs (z. B. für Course Dashboards oder Deep Links). GitHub issue GH-131 definiert, dass Studierende nur auf eigene Kurse zugreifen dürfen, während GH-30 die Payload-Struktur vorgibt. Die Anforderung stellt sicher, dass Kursdetails ohne Umwege abrufbar sind und keine Fremddaten offengelegt werden.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/131
- Supporting issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Autorisierungslogik sollte zentral gehalten werden, damit auch verwandte Endpoints (Topics, Learning Elements) identische Checks nutzen.
