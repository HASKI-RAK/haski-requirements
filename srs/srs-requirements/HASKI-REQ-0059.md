---
id: HASKI-REQ-0059
title: Tutor-Algorithmen pro Topic abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-002
links:
  stories: ["HASKI-RAK/HASKI-Backend#83", "HASKI-RAK/HASKI-Backend#93"]
  parents: ["SyRS-FUNC-002"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm"
---

## Beschreibung

Das System **shall** einen Endpoint `GET /topic/<topic_id>/teacherAlgorithm` bereitstellen, der den aktuell von Tutor:innen festgelegten Lernpfad-Algorithmus eines Topics mitsamt `short_name`, `algorithm_id` und `topic_id` zurückliefert. Die Route **shall** dieselbe Rollen- und Autorisierungslogik wie die Algorithmus-Administrationsendpunkte verwenden und ausschließlich wiedergeben, was zuvor per `POST .../teacherAlgorithm` oder Default-Lernpfad-Konfiguration gesetzt wurde. Damit Frontend-Dialoge und Automatisierungen stets den verbindlichen Tutor-Override anzeigen können, **shall** der Endpoint deterministisch 404 liefern, wenn für das Topic kein Eintrag existiert oder die aufrufende Rolle nicht berechtigt ist.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten mindestens `short_name`, `algorithm_id` und `topic_id` des aktuellen Tutor-Overrides.
- [x] Nicht vorhandene Topics bzw. fehlende Tutor-Konfigurationen führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Fehlende Berechtigungen liefern HTTP 401/403 gemäß Rollen-Decorator.
- [x] Der Endpoint verwendet dieselbe Algorithmus-Namensauflösung wie der zentrale Katalog (HASKI-REQ-0040), damit Konsistenz zwischen Auswahl und Anzeige gewährleistet ist.

## Rationale

GitHub Issues [#83](https://github.com/HASKI-RAK/HASKI-Backend/issues/83) und [#93](https://github.com/HASKI-RAK/HASKI-Backend/issues/93) verlangen, dass Tutor:innen Topic-spezifische Lernpfad-Algorithmen setzen und die Frontends diese Overrides anzeigen können. Ohne einen dedizierten Read-Endpoint könnten Studierende und Lehrende nicht erkennen, welcher Algorithmus aktuell gilt, und UI-Komponenten wie das AlgorithmSettingsModal hätten keine verlässliche Datenquelle. Die Anforderung stellt sicher, dass jede Auswahl sofort abrufbar und mit der Persistenz der Tutoring-Funktionen konsistent bleibt.

## Hinweise

- Endpoint teilt sich die Autorisierungs-Decoratoren mit `POST /user/<user_id>/<lms_user_id>/topic/<topic_id>/teacherAlgorithm`.
- Die Antwortwerte sind Grundlage für Frontend-Komponenten `AlgorithmSettingsModal` und API-Clients wie `fetchTeacherLpLeAlg`.
- Für Subtopics gelten identische Pfade; deren IDs werden in der gleichen Tabelle verwaltet.
