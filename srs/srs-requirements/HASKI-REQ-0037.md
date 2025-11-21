---
id: HASKI-REQ-0037
title: Automatische Learning-Element-Anlage aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#21"]
  tests:
    ["backend/tests/e2e/test_api.py::TestApi::test_api_create_le_from_moodle"]
---

## Beschreibung

Das System **shall** Learning Elements automatisch auf Basis der von Moodle gelieferten Aktivitätsdaten erzeugen. Dabei **shall** alle relevanten Metadaten (LMS-ID, Aktivitätstyp, Klassifikation, Name, Erstellungszeitpunkt, Verantwortliche Person, Hochschule) persistiert und dem passenden Topic/Subtopic zugeordnet werden. Bereits vorhandene Learning Elements **shall** über ihre LMS-ID erkannt und nicht dupliziert werden, Fehler in der Nutzereingabe (fehlende Felder, falsche Datentypen) **shall** durch klare Fehlermeldungen abgefangen werden.

## Akzeptanzkriterien

- [ ] Ein REST-Endpunkt erlaubt das Anlegen von Learning Elements je Topic/Subtopic auf Basis der Moodle-LMS-ID
- [ ] Pflichtattribute (LMS-ID, Aktivitätstyp, Klassifikation, Name, Universität, Zeitstempel, created_by) werden validiert und gespeichert
- [ ] Learning Elements werden automatisch dem korrekten Topic/Subtopic (parent_id) zugeordnet
- [ ] Duplicate LMS-IDs werden erkannt und führen zu einer 400-Fehlerantwort ohne zweite Anlage
- [ ] Ungültige Eingabedatentypen und fehlende Pflichtfelder erzeugen nachvollziehbare Fehlermeldungen
- [ ] Erfolgreich angelegte Learning Elements stehen unmittelbar für Lernpfade, Ratings und Empfehlungen zur Verfügung

## Rationale

Die automatische Übernahme der Moodle-Aktivitäten stellt sicher, dass Learning Elements ohne manuelle Nacharbeit in HASKI verfügbar sind und konsistent mit der führenden Lernplattform bleiben. Die Funktionalität wurde im Rahmen von GitHub Issue [GH-21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) implementiert und durch die E2E-Tests zur Learning-Element-Anlage verifiziert.
