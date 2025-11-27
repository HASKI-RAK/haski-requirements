---
id: HASKI-REQ-0051
title: Lernstrategien über REST abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-007
links:
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#81"]
  parents: ["SyRS-FUNC-007"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_students_learning_strategy"
---

## Beschreibung

Das System **shall** eine abgesicherte Schnittstelle bereitstellen, über die berechtigte Anwendungen die aktuell hinterlegten Lernstrategien eines Studierenden abrufen können. Die Schnittstelle muss die beim Onboarding erzeugten sowie später fortgeschriebenen Strategieeinträge konsistent ausgeben, damit Dashboards, Tutoring-Modelle und Analysen auf denselben Profilwerten basieren.

## Akzeptanzkriterien

- [x] Berechtigte Anfragen liefern den vollständigen Lernstrategie-Datensatz einschließlich aller verfügbaren Dimensionen des angefragten Studierenden.
- [x] Anfragen außerhalb des autorisierten Kontextes werden datenschutzkonform abgewiesen, ohne Informationen über andere Personen preiszugeben.
- [x] Die ausgegebenen Werte spiegeln unmittelbar die zuletzt erfassten Fragebogen- oder Analytics-Ergebnisse wider, sodass keine zusätzlichen Synchronisationsschritte notwendig sind.

## Rationale

SyRS-FUNC-007 fordert einen zentralen Zugriff auf Lernprofil-Daten, damit adaptive Funktionen konsistent arbeiten. Die abstrahierte Schnittstelle ermöglicht es, alle nachgelagerten Komponenten mit denselben Strategieinformationen zu versorgen, unabhängig davon, wann oder wie die Daten erhoben wurden.

## Hinweise

- API-Schema ist in der zentralen OAS-Dokumentation gepflegt und sollte nur gemeinsam mit den verantwortlichen Schnittstellen-Teams geändert werden.
- Frontend- und Analytics-Komponenten können dieselbe Antwortstruktur wiederverwenden, wodurch Doppelpflege vermieden wird.
