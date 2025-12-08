---
id: HASKI-REQ-0055
title: Kursinhalte (Topics) pro Studierendenkurs abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  stories:
    [
      "HASKI-RAK/HASKI-Backend#76",
      "HASKI-RAK/HASKI-Backend#30",
      "HASKI-RAK/HASKI-Frontend#264",
    ]
  parents: ["SyRS-FUNC-008"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_student_course_topics"
    - path: "frontend/src/services/Topic/fetchLearningPathTopic.test.tsx"
      name: "fetchLearningPathTopic"
    - path: "frontend/src/services/CourseTopics/CourseTopics.test.tsx"
      name: "useCourseTopics"
---

## Beschreibung

Das System **shall** allen eingeschriebenen Studierenden einen strukturierten Überblick über die Topics ihrer Kurse bereitstellen. Neben den Metadaten eines Topics sollen auch die jeweils gespeicherten Lernfortschrittsinformationen ausgegeben werden, damit Lernräume, Pfadberechnungen und Auswertungen auf dieselbe Sicht zugreifen können.

## Akzeptanzkriterien

- [x] Die bereitgestellte Liste umfasst sämtliche Topics eines belegten Kurses inklusive wesentlicher Stammdaten und des individuellen Lernkontexts.
- [x] Topics außerhalb der eigenen Einschreibung oder mit ungültigen Referenzen werden nicht ausgeliefert.
- [x] Alle beteiligten Systeme (z. B. Lernpfad-Services) können ohne zusätzliche Transformationsschritte mit den gelieferten Daten arbeiten.

## Rationale

SyRS-FUNC-008 beschreibt adaptive Lernräume auf Topic-Ebene. Ein konsistenter Topics-Feed stellt sicher, dass sowohl UI-Komponenten als auch Algorithmen auf denselben Strukturen basieren, unabhängig von der Quelle der Kursdaten.

## Hinweise

- Die Struktur orientiert sich an der zentralen OAS-Spezifikation; Änderungen sind gemeinsam mit allen Client-Teams zu koordinieren.
- Autorisierungs- und Filterlogik wird idealerweise gemeinsam mit Kurs- und Subtopic-Routen gepflegt.
