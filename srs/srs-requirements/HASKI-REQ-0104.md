---
id: HASKI-REQ-0104
title: Einreichung und Persistierung von Fragebogen-Antworten
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: ["SyRS-FUNC-007"]
  stories: ["HASKI-RAK/HASKI-Frontend#182"]
  tests:
    - path: "frontend/src/services/Questionnaire/postILS.test.tsx"
      name: "postILS has expected behaviour"
    - path: "frontend/src/services/Questionnaire/postListK.test.tsx"
      name: "postListK has expected behaviour"
---

## Beschreibung

Das System **shall** Endpunkte bereitstellen, um Antworten der Studierenden auf die Fragebögen (ILS, LIST-K) entgegenzunehmen und persistent zu speichern.

## Akzeptanzkriterien

- [x] Antworten des ILS-Fragebogens werden an das Backend gesendet und gespeichert.
- [x] Antworten des LIST-K-Fragebogens werden an das Backend gesendet und gespeichert.
- [x] Die Speicherung erfolgt verknüpft mit der User-ID.
- [x] Nach erfolgreicher Speicherung wird eine Bestätigung (HTTP 201) zurückgegeben.

## Rationale

Die Erfassung der Lernereigenschaften ist Voraussetzung für die Adaptivität des Systems (Lernpfadgenerierung). Issue #182 fordert explizit die Persistierung der Antworten.
