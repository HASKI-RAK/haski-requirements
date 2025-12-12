---
id: HASKI-REQ-0036
title: Automatische Topic- und Subtopic-Anlage aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-008
merged_from: ["HASKI-REQ-0076"]
links:
  parents:
    - "SyRS-INT-003"
    - "SyRS-FUNC-008"
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Frontend#135"
    - "HASKI-RAK/HASKI-Backend#131"
  tests:
    - path: "frontend/src/components/CreateTopic/Modal/CreateRemoteTopicsStep/CreateRemoteTopicsStep.test.tsx"
      name: "CreateRemoteTopicsStep"
    - path: "frontend/src/components/CreateTopic/Table/CreateRemoteTopics/CreateRemoteTopicsTable.hooks.test.tsx"
      name: "useCreateRemoteTopicsTable"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_create_topic_from_moodle"
    - path: "frontend/src/components/CreateTopic/Modal/CreateTopicModal/CreateTopicModal.test.tsx"
      name: "CreateTopicModal"
    - path: "frontend/src/components/CreateTopic/Modal/CreateTopicModal/CreateTopicModal.hooks.test.tsx"
      name: "useCreateTopicModal"
    - path: "frontend/src/components/TopicCard/TopicCard.test.tsx"
      name: "TopicCard Component"
    - path: "frontend/src/components/CreateTopic/Table/CreateRemoteTopics/CreateRemoteTopicsTable.test.tsx"
      name: "CreateRemoteTopicsTable"
    - path: "frontend/src/components/CreateTopic/Table/ExistingTopics/ExistingTopicsTable.test.tsx"
      name: "ExistingTopicsTable"
    - path: "frontend/src/services/Topic/postTopic.test.tsx"
      name: "postTopic has expected behaviour"
    - path: "frontend/src/pages/Course/Course.test.tsx"
      name: "Course Page"
    - path: "frontend/src/services/RemoteTopics/fetchRemoteTopics.test.tsx"
      name: "fetchRemoteTopics has expected behaviour"
    - path: "HASKI-Frontend/src/services/Topic/postAddAllStudentsToTopics.test.ts"
      name: "postAddAllStudentsToTopics has expected behaviour"
    - path: "frontend/src/services/LearningElement/postLearningElement.test.tsx"
      name: "postLearningElement has expected behaviour"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_topic_learning_element"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topic_learning_element_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topic_learning_element_by_le"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_topic_learning_element_by_topic"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_topic_learning_element_by_le"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_learning_element"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_topic_from_moodle"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_topic"
---

## Beschreibung

Das System **shall** Topics und Subtopics automatisch anhand der aus Moodle übermittelten Kursstruktur anlegen. Für jeden Moodle-Kurs **shall** sowohl der Topic-Knoten als auch die optionale Subtopic-Hierarchie mit allen Metadaten (Name, LMS-ID, Universitätszuordnung, Erstellungskontext) übernommen werden. Bereits angelegte Topics **shall** erkannt und nicht dupliziert werden. Das Frontend **shall** Lehrenden die aus Moodle synchronisierten Topics in einem Create-Topic-Dialog anzeigen, damit die automatische Anlage nachvollziehbar und bei Bedarf gezielt ausgelöst werden kann; der Dialog **shall** den Import als mehrstufigen Assistenten abbilden, in dem die Topic-Auswahl die nachfolgenden Schritte steuert und Zwischenergebnisse bis zum Abschluss konserviert.

Ergänzend **shall** das Backend einen OAS-konformen Endpunkt `PUT /lms/topic/<topic_id>/<moodle_topic_id>` bereitstellen, über den Moodle aktualisierte Topic- und Subtopic-Metadaten nach HASKI synchronisiert. Die Route **shall** anhand der Kombination aus Topic-ID und Moodle-ID eindeutig bestimmen, welcher Knoten angepasst wird, und die Felder `name`, `is_topic`, `parent_id`, `contains_le`, `created_by`, `created_at`, `last_updated` sowie `university` gemäß Payload übernehmen. Bei Subtopics **shall** die Parent-Relation automatisch auf den referenzierten Topic gesetzt werden, damit Lernpfad- und Content-Zuordnungen konsistent bleiben.

Neben der automatischen Anlage und Aktualisierung **shall** das System Topics, Subtopics und deren Learning-Element-Zuordnungen vollständig verwaltbar machen (Erstellen, Aktualisieren, Löschen, Abfragen). Jede Änderung **shall** konsistent mit `course_topic` sowie `topic_learning_element` Relationen erfolgen, sodass Lernpfade und Kurs-Detailansichten sofort die aktuelle Struktur widerspiegeln.

## Akzeptanzkriterien

### Anlage von Topics und Subtopics aus Moodle

- [x] Ein REST-Endpunkt erlaubt das Anlegen von Topics/Subtopics pro Moodle-Kurs.
- [x] Pflichtattribute (Name, LMS-ID, Typ, Universität, Zeitstempel) werden validiert und persistiert.
- [x] Subtopics erhalten automatisch den Parent-Topic- oder Kurs-Bezug sowie ihr `contains_le`-Flag.
- [x] Duplicate Topic-Anlagen auf Basis derselben LMS-ID werden verhindert und führen zu Fehlerantworten.
- [x] Ungültige Datentypen oder fehlende Felder resultieren in nachvollziehbaren Fehlercodes.
- [x] Erfolgreich angelegte Topics stehen sofort für Lernpfad-Berechnungen und Zuordnungen zur Verfügung.

### Aktualisierung von Topics/Subtopics aus Moodle

- [x] Erfolgreiche Updates über `PUT /lms/topic/<topic_id>/<moodle_topic_id>` liefern HTTP 201 und geben den vollständigen Topic-Datensatz (`id`, `lms_id`, `is_topic`, `parent_id`, `contains_le`, Zeitstempel, `university`) zurück.
- [x] Ungültige Kombinationen aus Topic-ID und Moodle-ID führen zu HTTP 404 mit standardisierter Fehlstruktur (`{"error": "...", "message": "..."}`), ohne interne Details preiszugeben.
- [x] Fehlende Pflichtfelder oder falsche Datentypen resultieren in HTTP 400 und hinterlassen keine Datenänderung.
- [x] Beim Aktualisieren von Subtopics wird `parent_id` auf den bestehenden Topic gesetzt, falls nicht explizit angegeben, sodass die Hierarchie stabil bleibt.
- [x] `created_at`/`last_updated` Werte werden validiert (ISO 8601) und persistiert, damit Änderungsverfolgung und Vergleich mit Moodle möglich bleiben.

### Verwaltung & Abfragen

- [x] Der mehrstufige Create-Topic-Dialog blockiert das Fortschreiten, bis ein importierbares Topic gewählt wurde, behält Nutzerentscheidungen zwischen den Schritten bei und löst nach Bestätigung die Topic-Anlage inklusive abhängiger REST-Aufrufe konsistent aus.
- [x] Topics und Subtopics können nachträglich aktualisiert oder gelöscht werden, ohne die Parent/Child-Hierarchie zu verletzen.
- [x] Topic-Learning-Element-Zuordnungen lassen sich erstellen, auflösen und aus beiden Richtungen abfragen (Topic oder Learning Element).
- [x] Service-Endpunkte liefern Topics, Subtopics und Learning Elements über Kurs- oder Topic-IDs sowie pro Studierendem konsistent aus.

## Rationale

Die automatische Übernahme der Topic-Struktur stellt sicher, dass Lerninhalte aus Moodle ohne manuelle Nacharbeit in HASKI abgebildet werden können. Die Funktionalität wurde im Rahmen der Grundstruktur des Backends implementiert (GitHub Issue [GH-21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21)). Issue [#135](https://github.com/HASKI-RAK/HASKI-Frontend/issues/135) ergänzt die Frontend-Oberfläche, indem sie den Importfluss für Lehrende sichtbar macht.

## Hinweise

- Die Frontend-Komponente `CreateRemoteTopicsStep` konsumiert die von der REST-Schnittstelle gelieferten Topic-Listen und verhindert das Fortfahren ohne Auswahl.
- Backend- und Frontend-Tests stellen gemeinsam sicher, dass keine doppelten Topics angelegt werden und die Auswahl für Lehrende transparent bleibt.
