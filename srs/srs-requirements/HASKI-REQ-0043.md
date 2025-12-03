---
id: HASKI-REQ-0043
title: Ratings für Lernende und Learning Elements verwalten
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-007
links:
  stories:
    [
      "HASKI-RAK/HASKI-Backend#106",
      "HASKI-RAK/HASKI-Backend#120",
      "HASKI-RAK/HASKI-Backend#121",
    ]
  parents: ["SyRS-FUNC-007"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_create_student_rating"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_student_ratings"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_create_learning_element_rating"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_element_ratings"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_calculate_rating"
    - path: "frontend/src/components/Dashboards/Rating/RatingDashboard/RatingDashboard.test.tsx"
      name: "RatingDashboard"
    - path: "frontend/src/components/Dashboards/Rating/StudentRatingDashboard/StudentRatingDashboard.test.tsx"
      name: "StudentRatingDashboard"
    - path: "frontend/src/components/Dashboards/Rating/LearningElementRatingDashboard/LearningElementRatingDashboard.test.tsx"
      name: "useLearningElementRatingDashboard"
    - path: "frontend/src/components/Dashboards/Rating/RatingDashboardDrawer/RatingDashboardDrawer.test.tsx"
      name: "RatingDashboardDrawer"
    - path: "frontend/src/components/Dashboards/Rating/RatingDashboardDrawerButton/RatingDashboardDrawerButton.test.tsx"
      name: "RatingDashboardDrawerButton"
    - path: "frontend/src/pages/Rating/Rating.test.tsx"
      name: "Rating"
    - path: "frontend/src/services/Rating/fetchLearningElementRatings.test.tsx"
      name: "fetchLearningElementRatings"
    - path: "frontend/src/services/Rating/fetchStudentRatings.test.tsx"
      name: "fetchStudentRatings"
    - path: "frontend/src/services/Rating/postCalculateRating.test.tsx"
      name: "postCalculateRating"
    - path: "backend/tests/unit/test_domain_model.py"
      name: "test_calculate_learning_element_rating"
    - path: "backend/tests/unit/test_learners_model.py"
      name: "test_calculate_student_rating"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_student_rating"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_student_ratings_on_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_student_ratings"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_element_rating"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_element_ratings_on_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_element_ratings"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_learning_element_ratings_by_learning_element"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_learning_element_ratings_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_student_ratings_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_ratings"
---

## Beschreibung

Das System **shall** persistente Ratings für Studierende (pro Topic) und für einzelne Learning Elements verwalten, damit Lehrende Lernfortschritts- und Qualitätseinschätzungen unmittelbar abrufen können. Die Bewertung basiert auf einem Bayes-/Elo-ähnlichen Modell mit `rating_value` und `rating_deviation`, wird über dedizierte REST-Endpunkte aktualisiert und dient als Grundlage für Lernfortschrittsberichte (SyRS-FUNC-007) sowie für spätere Empfehlungssysteme. Rating-Berechnungen **shall** sowohl manuell ausgelöst als auch automatisiert aus den Moodle-Versuchsdaten rekonstruiert werden können, ohne bestehende Lernpfade zu beeinträchtigen.

## Akzeptanzkriterien

### Student:innen-Ratings

- [x] `POST /student/<student_id>/topic/<topic_id>/rating` legt einen Rating-Eintrag mit `rating_value`, `rating_deviation`, `timestamp` an oder aktualisiert ihn (GH-106)
- [x] Der Endpunkt ermittelt den adressierten Studierenden aus der zugehörigen Moodle-ID und verknüpft den Rating-Datensatz mit dem Topic
- [x] `GET /user/<user_id>/student/<student_id>/rating` liefert alle vorhandenen Ratings eines Studierenden einschließlich Topic-Referenzen in chronologischer Reihenfolge

### Learning-Element-Ratings

- [x] `POST /topic/<topic_id>/learningElement/<learning_element_id>/rating` erzeugt oder aktualisiert einen Rating-Datensatz für ein Learning Element samt Topic-Referenz
- [x] `GET /learningElement/rating` stellt eine Liste aller Learning-Element-Ratings bereit, sodass Dashboards Qualitäts- und Schwierigkeitsdaten visualisieren können

### Rating-Neuberechnung aus Moodle-Daten

- [x] `POST /user/<user_id>/course/<course_id>/topic/<topic_id>/learningElement/<learning_element_id>/rating` iteriert über die in Moodle hinterlegten Aktivitäten und aktualisiert Student- und Learning-Element-Ratings in einem Lauf
- [x] Der Endpunkt ruft dafür die Moodle-Module und die zugehörigen `usersattempts` ab; unvollständige Daten führen zu einer nachvollziehbaren Fehlermeldung, verursachen aber keinen Eintrag (GH-120)
- [x] Der Workflow unterstützt Batch-Neuberechnungen für mehrere Learning Elements eines Topics, ohne inkonsistente Doppelwerte zu erzeugen

### Datenlebenszyklus

- [x] Löschen eines Learning Elements oder Topics entfernt abhängige Rating-Datensätze (GH-121)
- [x] Alle Rating-Endpunkte validieren Eingaben und liefern HTTP-Statuscodes (`201` für erfolgreiche Berechnung, `200` für Leseoperationen, `4xx` für Invalidität)

## Rationale

Bewertungsdaten ergänzen die Lernpfad- und Analytics-Funktionen des HASKI-Systems: Lehrende sehen auf einen Blick, welche Studierenden in einem Topic Unterstützung benötigen und welche Learning Elements auffällig sind. Die Anforderung operationalisiert System Requirement SyRS-FUNC-007 (Lernfortschrittsreports) durch konkrete REST-Schnittstellen und Datenpersistenz.

## Hinweise

- Primäre Implementierung: [HASKI-Backend#106](https://github.com/HASKI-RAK/HASKI-Backend/issues/106) – führt Datenbanktabellen, Services und Endpunkte für Ratings ein
- Fehlerbehandlung: [HASKI-Backend#120](https://github.com/HASKI-RAK/HASKI-Backend/issues/120) stellt sicher, dass rating-bezogene Berechnungen bei fehlenden Learning-Element-IDs nicht abstürzen
- Datenkonsistenz: [HASKI-Backend#121](https://github.com/HASKI-RAK/HASKI-Backend/issues/121) entfernt verwaiste Ratings beim Löschen von Kursen, Topics oder Learning Elements
- Langfristig dienen die gleichen Rating-Datensätze als Feature-Input für Recommendation Engines und adaptives Monitoring
