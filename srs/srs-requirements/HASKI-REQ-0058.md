---
id: HASKI-REQ-0058
title: Persistierte Lernpfade pro Topic abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#2", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_for_student"
---

## Beschreibung

Das System **shall** über `GET /user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic/<topic_id>/learningPath` den zuletzt berechneten Lernpfad eines Studierenden für das angegebene Topic ausliefern. Die Antwort **shall** mindestens `id`, `course_id`, `topic_id`, `student_id`, `based_on`, `path` und `calculated_on` enthalten, damit Frontend, Analytics und Tutoring-Modell denselben Persistenzstand verwenden. Der Endpoint **shall** dieselben Einschreibungs- und Autorisierungsprüfungen wie die Kurs- und Topic-Routen anwenden und ausschließlich Lernpfade zurückgeben, die zu den belegten Kursen des Studierenden gehören.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten die genannten Felder inklusive vollständigem `path`-Array.
- [x] Ungültige Studierenden-, Kurs- oder Topic-IDs (einschließlich fehlender Einschreibungen) resultieren in HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Die Route akzeptiert Moodle-IDs gemäß GH-30 und nutzt dieselbe ID-Mapping-Logik wie verwandte Lernpfad-Endpunkte.
- [x] Der Endpoint greift auf den Persistenzstand zurück, den `POST .../learningPath` (GH-2) erzeugt, ohne eine erneute Berechnung anzustoßen.

## Rationale

SyRS-FUNC-008 verlangt, dass adaptive Lernräume konsistent über alle Kanäle hinweg abrufbar sind. Nachdem Lernpfade via GH-2 berechnet und gespeichert wurden, benötigen Frontend und Analytics einen Read-Endpoint, der den exakt persistierten Lernpfad mitsamt Metadaten bereitstellt. Der Endpoint stellt sicher, dass Studierende jederzeit den aktuellen Lernpfad einsehen können, ohne erneut eine Berechnung anzustoßen oder zusätzliche Filter im Frontend zu pflegen.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/2
- Supporting issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Der Endpoint wiederverwendet dieselbe Autorisierungs- und Fehlerbehandlungs-Logik wie `GET .../topic` und `GET .../subtopic`, um konsistente Antworten im Lernpfad-Kontext zu gewährleisten.
