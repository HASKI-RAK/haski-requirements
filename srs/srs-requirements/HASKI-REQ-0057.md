---
id: HASKI-REQ-0057
title: Einzelnes Topic eines Studierendenkurses abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#76", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_topic_by_id_for_student"
---

## Beschreibung

Das System **shall** einen Endpoint `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic/<topic_id>` bereitstellen, der die vollständigen Daten eines Topics mitsamt `student_topic`-Kontext zurückliefert, sofern der Studierende laut Moodle für den Kurs freigeschaltet ist. Die Route **shall** dieselbe Autorisierung verwenden wie die Kurs- und Topic-Liste (GH-76) und nur Topics ausgeben, die zu den belegten Kursen gehören. Die Antwort **shall** mindestens `id`, `lms_id`, `name`, `is_topic`, `contains_le`, `university`, `parent_id` sowie den Lernfortschrittskontext enthalten, damit Lernräume und Lernpfad-Berechnungen konsistent arbeiten.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 samt vollständigem Topic-Objekt und `student_topic`.
- [x] Ungültige Studierenden-, Kurs- oder Topic-IDs (einschließlich fehlender Einschreibungen) führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Der Endpoint nutzt dieselbe Moodle-ID-Mapping-Logik wie `GET .../topic` und konsumiert die von GH-76 beschriebenen Datensätze.
- [x] Die Nutzlast entspricht der OAS-Struktur aus GH-30, sodass Frontend- und Analytics-Komponenten keine zusätzlichen Transformationen benötigen.

## Rationale

SyRS-FUNC-008 fordert konfigurierbare Lernräume; dazu müssen einzelne Topics inklusive persönlicher Lernfortschrittsdaten abrufbar sein. GH-76 beschreibt die Kurs-Topic-Relationen, und GH-30 spezifiziert die REST-Struktur. Die Anforderung stellt sicher, dass Clients gezielt einzelne Topics referenzieren können, ohne zusätzliche Filterlogik implementieren zu müssen.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/76
- Supporting issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Der Endpoint teilt sich Autorisierungs- und Fehlerbehandlung mit Subtopic- und Learning-Element-Routen; gemeinsame Middleware minimiert Inkonsistenzen.
