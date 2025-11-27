---
id: HASKI-REQ-0057
title: Einzelnes Topic eines Studierendenkurses abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories: ["HASKI-RAK/HASKI-Backend#76", "HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_topic_by_id_for_student"
---

## Beschreibung

Das System **shall** berechtigten Anfragen die Detaildaten einzelner Topics inklusive des persönlichen Lernfortschritts bereitstellen. Dadurch können Lernräume, Prozessschritte oder Auswertungen gezielt auf ein Topic zugreifen, ohne zuvor komplette Topic-Listen übertragen zu müssen.

## Akzeptanzkriterien

- [x] Für einen gültig angefragten Kurs-/Topic-Kontext stehen sämtliche relevanten Metadaten sowie der `student_topic`-Status zur Verfügung.
- [x] Topics, die nicht zum Studierenden gehören oder nicht existieren, werden nicht ausgeliefert.
- [x] Alle beteiligten Systeme können die gelieferten Felder unverändert weiterverwenden, da sie dem zentralen Schema entsprechen.

## Rationale

Konfigurierbare Lernräume benötigen gezielte Detailabfragen, z. B. wenn einzelne Topics hervorgehoben oder bearbeitet werden. Diese Anforderung stellt sicher, dass ein Topic in isolierter Form bereitgestellt wird und dennoch denselben Kontext wie die Listenansicht besitzt.

## Hinweise

- Felddefinitionen folgen der in der OAS dokumentierten Topic-Spezifikation.
- Autorisierungsregeln sollten identisch zu den Topic- und Subtopic-Listen umgesetzt werden, um einheitliches Verhalten sicherzustellen.
