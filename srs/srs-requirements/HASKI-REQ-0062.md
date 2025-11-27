---
id: HASKI-REQ-0062
title: Learning Elements eines Topics abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#21", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_les_for_topic_for_student"
---

## Beschreibung

Das System **shall** eingeschriebenen Studierenden sämtliche Learning Elements eines Topics inklusive ihres persönlichen Fortschritts bereitstellen. Damit können Empfehlungssysteme, Dashboards und Tracking-Funktionen identische Daten verwenden, ohne mehrere Datenquellen abgleichen zu müssen.

## Akzeptanzkriterien

- [x] Die Antwort umfasst alle Learning Elements des Topics mit den relevanten Metadaten (z. B. Typ, Klassifikation, Name, LMS-Referenz) und dem zugehörigen `student_learning_element`-Status.
- [x] Topics, zu denen kein legitimer Zugriff besteht, liefern keine Daten.
- [x] Änderungen an Learning Elements werden ohne Zusatzaufwand in der Ausgabe sichtbar.

## Rationale

SyRS-FUNC-008 sieht lernpfadfähige Räume vor, in denen pro Topic sämtliche Elemente verfügbar sind. Eine standardisierte Auslieferung verhindert Inkonsistenzen zwischen Frontend, Analytics und Tutoring-Komponenten.

## Hinweise

- Die Datenstruktur entspricht der in der OAS beschriebenen Topic/LE-Spezifikation.
- Wird kein Learning Element gefunden, wird eine leere Liste zurückgegeben, damit Aufrufer deterministisch reagieren können.
