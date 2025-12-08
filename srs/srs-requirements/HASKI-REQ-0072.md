---
id: HASKI-REQ-0072
title: Learning-Element-Empfehlungen abrufen und anzeigen
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-001
links:
  parents: ["SyRS-FUNC-001"]
  stories:
    - "HASKI-RAK/HASKI-Backend#125"
    - "HASKI-RAK/HASKI-Frontend#362"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_element_recommendation"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_recommended_exercises_for_student_in_topic"
    - path: "frontend/src/services/LearningElementRecommendation/LearningElementRecommendation.test.tsx"
      name: "LearningElementRecommendation"
    - path: "frontend/src/services/LearningElementRecommendation/fetchLearningElementRecommendation.test.ts"
      name: "fetchLearningElementRecommendation"
    - path: "HASKI-Frontend/src/services/LearningElementRecommendation/fetchLearningElementRecommendation.test.ts"
      name: "fetchLearningElementRecommendation"
    - path: "HASKI-Frontend/src/store/Slices/LearningElementRecommendationSlice/LearningElementRecommendationSlice.test.ts"
      name: "LearningElementRecommendationSlice"
---

## Beschreibung

Das Backend **shall** einen GET-Endpunkt `GET /user/<user_id>/course/<course_id>/topic/<topic_id>/recommendation` bereitstellen, der für einen angemeldeten Studierenden eine nach Relevanz sortierte Liste empfohlener Learning Elements (Exercises) desselben Topics liefert. Der Endpunkt **shall** die HASKI-User-ID auflösen, den zugehörigen LMS-User und Studentendatensatz bestimmen und anschließend den Recommendation-Service (z. B. Elo-/Bayes-basierte Gewichtung) ausführen. Die Antwort **shall** ausschließlich Learning Elements enthalten, die dem angefragten Topic und Kurs zugeordnet sind; fehlende Empfehlungen führen zu einer leeren Liste statt eines Fehlers. Fehlerhafte IDs oder fehlende Berechtigungen **shall** deterministisch mit HTTP-Fehlercodes (z. B. 404/401) beantwortet werden, ohne interne Details offenzulegen.

Das Frontend **shall** dem Studierenden basierend auf den vom Backend gelieferten Empfehlungen das nächste zu bearbeitende Learning Element anzeigen.

## Akzeptanzkriterien

### Backend

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und ein JSON-Array von Learning-Element-Objekten mit mindestens `id`, `lms_id`, `name`, `activity_type`, `classification`, `student_learning_element`.
- [x] Die Liste ist stabil nach dem vom Recommendation-Service gelieferten Ranking sortiert (höchste Priorität zuerst); bei Gleichstand bleibt die ursprüngliche Berechnungsreihenfolge erhalten.
- [x] Der Endpunkt validiert `user_id`, `course_id`, `topic_id` gegen bestehende Zuordnungen und antwortet bei ungültigen IDs mit `{"error": ..., "message": ...}` und passendem HTTP-Status.
- [x] Gibt es keine passenden Empfehlungen, wird eine leere Liste zurückgegeben; das Format bleibt unverändert.

### Frontend

- [x] Abruf der Empfehlungsdaten vom Backend.
- [x] Anzeige der empfohlenen Übung im Lernpfad.
- [x] Wenn keine Empfehlung vorhanden ist, wird dies entsprechend behandelt (z.B. keine Anzeige).

## Rationale

Issue [#125](https://github.com/HASKI-RAK/HASKI-Backend/issues/125) fordert einen Backend-Service, der Studierenden eine sortierte Empfehlungsliste von Übungen in einem Topic bereitstellt. User Story [#362](https://github.com/HASKI-RAK/HASKI-Frontend/issues/362) fordert die Anzeige dieser Empfehlungen im Frontend. Diese Funktion operationalisiert SyRS-FUNC-001 (adaptive Lernpfade), indem sie konkrete REST-Schnittstellen definiert, mit denen Frontends die nächsten sinnvollen Learning Elements abrufen und anzeigen können. Studierende sollen im adaptiven Modus geführt werden und wissen, was der nächste sinnvolle Schritt ist.

## Hinweise

- Die Implementierung nutzt `services.get_recommended_exercises_for_student_in_topic`, das Rating- und Kursdaten kombiniert.
- Erweiterungen wie alternative Ranking-Strategien oder Filter (z. B. bereits erledigte Aufgaben) sind zulässig, solange das Grundformat des Endpunkts unverändert bleibt.
