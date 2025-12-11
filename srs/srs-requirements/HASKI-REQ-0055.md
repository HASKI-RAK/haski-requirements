---
id: HASKI-REQ-0055
title: Kursinhalte (Topics) pro Studierendenkurs abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
merged_from: ["HASKI-REQ-0057", "HASKI-REQ-0061"]
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
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_topic_by_id_for_student"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_sub_topics_for_topic"
---

## Beschreibung

Das System **shall** allen eingeschriebenen Studierenden einen strukturierten Überblick über die Topics ihrer Kurse bereitstellen. Neben den Metadaten eines Topics sollen auch die jeweils gespeicherten Lernfortschrittsinformationen ausgegeben werden, damit Lernräume, Pfadberechnungen und Auswertungen auf dieselbe Sicht zugreifen können.

Darüber hinaus **shall** das System berechtigten Anfragen die Detaildaten einzelner Topics inklusive des persönlichen Lernfortschritts bereitstellen, sodass Lernräume, Prozessschritte oder Auswertungen gezielt auf ein Topic zugreifen können. Ergänzend **shall** das System alle Subtopics eines Topics für eingeschriebene Studierende zugänglich machen, einschließlich der individuellen Lernkontexte, damit die hierarchische Struktur eines Kurses vollständig nachvollzogen werden kann.

## Akzeptanzkriterien

- [x] Die bereitgestellte Liste umfasst sämtliche Topics eines belegten Kurses inklusive wesentlicher Stammdaten und des individuellen Lernkontexts.
- [x] Topics außerhalb der eigenen Einschreibung oder mit ungültigen Referenzen werden nicht ausgeliefert.
- [x] Alle beteiligten Systeme (z. B. Lernpfad-Services) können ohne zusätzliche Transformationsschritte mit den gelieferten Daten arbeiten.

### Einzelnes Topic eines Studierendenkurses

- [x] Für einen gültig angefragten Kurs-/Topic-Kontext stehen sämtliche relevanten Metadaten sowie der `student_topic`-Status zur Verfügung.
- [x] Topics, die nicht zum Studierenden gehören oder nicht existieren, werden nicht ausgeliefert.
- [x] Alle beteiligten Systeme können die gelieferten Felder unverändert weiterverwenden, da sie dem zentralen Schema entsprechen.

### Subtopics eines belegten Kurses abrufen

- [x] Die Ausgabe enthält sämtliche Subtopics inklusive Metadaten (z. B. Kennung, Titel, Parent-Bezug, Lernstatus).
- [x] Fehlen Subtopics, wird eine leere, aber gültige Antwort geliefert, sodass Aufrufer deterministisch planen können.
- [x] Anfragen außerhalb der eigenen Kurs-/Topic-Zuordnung liefern keine Daten.

## Rationale

SyRS-FUNC-008 beschreibt adaptive Lernräume auf Topic-Ebene. Ein konsistenter Topics-Feed stellt sicher, dass sowohl UI-Komponenten als auch Algorithmen auf denselben Strukturen basieren, unabhängig von der Quelle der Kursdaten.

## Hinweise

- Die Struktur orientiert sich an der zentralen OAS-Spezifikation; Änderungen sind gemeinsam mit allen Client-Teams zu koordinieren.
- Autorisierungs- und Filterlogik wird idealerweise gemeinsam mit Kurs- und Subtopic-Routen gepflegt.
