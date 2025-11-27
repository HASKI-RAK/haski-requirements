---
id: HASKI-REQ-0063
title: Einzelnes Learning Element abrufen
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
      name: "TestApi::test_get_le_by_id_for_student"
---

## Beschreibung

Das System **shall** Detailinformationen zu einem einzelnen Learning Element bereitstellen, sobald ein berechtigter Studierender diese benötigt. Die Antwort umfasst sowohl die Stammdaten als auch den persönlichen Lernfortschrittsstatus, sodass UI- und Analytics-Komponenten gezielt mit einem Element arbeiten können, ohne komplette Listen zu laden.

## Akzeptanzkriterien

- [x] Für gültige Kombinationen aus Studierendem, Kurs, Topic und Learning Element werden sämtliche relevanten Metadaten sowie der `student_learning_element`-Kontext geliefert.
- [x] Nicht zugeordnete oder unbekannte Ressourcen werden nicht ausgegeben.
- [x] Die gelieferten Felder entsprechen der zentralen Learning-Element-Spezifikation und können ohne zusätzliche Transformationen verwendet werden.

## Rationale

Einzelne Lernpfad-Ansichten, Feedbackdialoge oder Auswertungen benötigen zielgerichtete Detailinformationen. Die Anforderung aus SyRS-FUNC-008 stellt sicher, dass jede Ressource isoliert adressiert werden kann und gleichzeitig die geltenden Einschreibungsregeln respektiert.

## Hinweise

- Die Struktur ist kompatibel zu den Listenendpunkten (HASKI-REQ-0062), wodurch Frontends dieselben Komponenten wiederverwenden können.
- Wird ein Learning Element entfernt, liefert die Abfrage keine Daten mehr, wodurch veraltete Verlinkungen frühzeitig auffallen.
