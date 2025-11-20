---
id: HASKI-REQ-0036
title: Automatische Topic- und Subtopic-Anlage aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#21"]
  tests:
    [
      "backend/tests/e2e/test_api.py::TestApi::test_api_create_topic_from_moodle",
    ]
---

## Beschreibung

Das System **shall** Topics und Subtopics automatisch anhand der aus Moodle übermittelten Kursstruktur anlegen. Für jeden Moodle-Kurs **shall** sowohl der Topic-Knoten als auch die optionale Subtopic-Hierarchie mit allen Metadaten (Name, LMS-ID, Universitätszuordnung, Erstellungskontext) übernommen werden. Bereits angelegte Topics **shall** erkannt und nicht dupliziert werden.

## Akzeptanzkriterien

- [ ] Ein REST-Endpunkt erlaubt das Anlegen von Topics/Subtopics pro Moodle-Kurs.
- [ ] Pflichtattribute (Name, LMS-ID, Typ, Universität, Zeitstempel) werden validiert und persistiert.
- [ ] Subtopics erhalten automatisch den Parent-Topic- oder Kurs-Bezug sowie ihr `contains_le`-Flag.
- [ ] Duplicate Topic-Anlagen auf Basis derselben LMS-ID werden verhindert und führen zu Fehlerantworten.
- [ ] Ungültige Datentypen oder fehlende Felder resultieren in nachvollziehbaren Fehlercodes.
- [ ] Erfolgreich angelegte Topics stehen sofort für Lernpfad-Berechnungen und Zuordnungen zur Verfügung.

## Rationale

Die automatische Übernahme der Topic-Struktur stellt sicher, dass Lerninhalte aus Moodle ohne manuelle Nacharbeit in HASKI abgebildet werden können. Die Funktionalität wurde im Rahmen der Grundstruktur des Backends implementiert (GitHub Issue [GH-21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21)).
