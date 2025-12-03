---
id: HASKI-REQ-0036
title: Automatische Topic- und Subtopic-Anlage aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Frontend#135"
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
    - path: "HASKI-Frontend/src/components/CreateTopic/Table/CreateRemoteTopics/CreateRemoteTopicsTable.test.tsx"
      name: "CreateRemoteTopicsTable"
    - path: "HASKI-Frontend/src/components/CreateTopic/Table/ExistingTopics/ExistingTopicsTable.test.tsx"
      name: "ExistingTopicsTable"
    - path: "HASKI-Frontend/src/services/Topic/postTopic.test.tsx"
      name: "postTopic has expected behaviour"
---

## Beschreibung

Das System **shall** Topics und Subtopics automatisch anhand der aus Moodle übermittelten Kursstruktur anlegen. Für jeden Moodle-Kurs **shall** sowohl der Topic-Knoten als auch die optionale Subtopic-Hierarchie mit allen Metadaten (Name, LMS-ID, Universitätszuordnung, Erstellungskontext) übernommen werden. Bereits angelegte Topics **shall** erkannt und nicht dupliziert werden. Das Frontend **shall** Lehrenden die aus Moodle synchronisierten Topics in einem Create-Topic-Dialog anzeigen, damit die automatische Anlage nachvollziehbar und bei Bedarf gezielt ausgelöst werden kann; der Dialog **shall** den Import als mehrstufigen Assistenten abbilden, in dem die Topic-Auswahl die nachfolgenden Schritte steuert und Zwischenergebnisse bis zum Abschluss konserviert.

## Akzeptanzkriterien

- [x] Ein REST-Endpunkt erlaubt das Anlegen von Topics/Subtopics pro Moodle-Kurs.
- [x] Pflichtattribute (Name, LMS-ID, Typ, Universität, Zeitstempel) werden validiert und persistiert.
- [x] Subtopics erhalten automatisch den Parent-Topic- oder Kurs-Bezug sowie ihr `contains_le`-Flag.
- [x] Duplicate Topic-Anlagen auf Basis derselben LMS-ID werden verhindert und führen zu Fehlerantworten.
- [x] Ungültige Datentypen oder fehlende Felder resultieren in nachvollziehbaren Fehlercodes.
- [x] Erfolgreich angelegte Topics stehen sofort für Lernpfad-Berechnungen und Zuordnungen zur Verfügung.
- [x] Der mehrstufige Create-Topic-Dialog blockiert das Fortschreiten, bis ein importierbares Topic gewählt wurde, behält Nutzerentscheidungen zwischen den Schritten bei und löst nach Bestätigung die Topic-Anlage inklusive abhängiger REST-Aufrufe konsistent aus.

## Rationale

Die automatische Übernahme der Topic-Struktur stellt sicher, dass Lerninhalte aus Moodle ohne manuelle Nacharbeit in HASKI abgebildet werden können. Die Funktionalität wurde im Rahmen der Grundstruktur des Backends implementiert (GitHub Issue [GH-21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21)). Issue [#135](https://github.com/HASKI-RAK/HASKI-Frontend/issues/135) ergänzt die Frontend-Oberfläche, indem sie den Importfluss für Lehrende sichtbar macht.

## Hinweise

- Die Frontend-Komponente `CreateRemoteTopicsStep` konsumiert die von der REST-Schnittstelle gelieferten Topic-Listen und verhindert das Fortfahren ohne Auswahl.
- Backend- und Frontend-Tests stellen gemeinsam sicher, dass keine doppelten Topics angelegt werden und die Auswahl für Lehrende transparent bleibt.
