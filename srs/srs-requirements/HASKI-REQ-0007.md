---
id: HASKI-REQ-0007
title: Automatische Anpassung von Lernpfaden basierend auf Lernstil
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Demonstration
source_id: SyRS-FUNC-001
links:
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#239",
      "HASKI-RAK/HASKI-Frontend#209",
      "HASKI-RAK/HASKI-Frontend#220",
      "HASKI-RAK/HASKI-Frontend#182",
      "HASKI-RAK/HASKI-Backend#8",
      "HASKI-RAK/HASKI-Backend#2",
      "HASKI-RAK/HASKI-Backend#30",
      "HASKI-RAK/HASKI-Backend#23",
      "HASKI-RAK/HASKI-Backend#93",
    ]
  parents: ["SyRS-FUNC-001", "SyRS-FUNC-007", "SyRS-FUNC-008"]
  tests:
    - path: "frontend/src/components/MenuBar/MenuBar.test.tsx"
      name: "MenuBar tests"
    - path: "frontend/src/components/ResponsiveMiniMap/ResponsiveMiniMap.test.tsx"
      name: "ResponsiveMiniMap component"
    - path: "frontend/src/components/Questionnaire/OpenQuestionnaire/OpenQuestionnaire.test.tsx"
      name: "OpenQuestionnaire"
    - path: "frontend/src/components/Questionnaire/QuestionnaireQuestions/Modal/QuestionnaireQuestionsModal.test.tsx"
      name: "QuestionnaireQuestionsModal"
    - path: "frontend/src/components/Questionnaire/QuestionnaireQuestions/Table/TableILSQuestions.test.tsx"
      name: "TableILSQuestions"
    - path: "frontend/src/components/Questionnaire/QuestionnaireQuestions/Table/TableListKQuestions.test.tsx"
      name: "TableListKQuestions"
    - path: "frontend/src/components/Questionnaire/QuestionnaireResults/Graph/GraphILS.test.tsx"
      name: "GraphILS"
    - path: "frontend/src/components/Questionnaire/QuestionnaireResults/Graph/GraphListK.test.tsx"
      name: "GraphListK"
    - path: "frontend/src/components/Questionnaire/QuestionnaireResults/Table/TableILS.test.tsx"
      name: "TableILS"
    - path: "frontend/src/components/Questionnaire/QuestionnaireResults/Table/TableListK.test.tsx"
      name: "TableListK"
    - path: "frontend/src/components/Questionnaire/QuestionnaireResults/Text/ResultDescriptionILS.test.tsx"
      name: "ResultDescriptionILS"
    - path: "frontend/src/components/Questionnaire/QuestionnaireResults/Text/ResultDescriptionListK.test.tsx"
      name: "ResultDescriptionListK"
    - path: "frontend/src/services/LearningPath/postCalculateLearningPathILS.test.tsx"
      name: "postCalculateLearningPathILS"
    - path: "frontend/src/services/LearningPath/fetchLearningPathElement.test.tsx"
      name: "fetchLearningPathElement"
    - path: "backend/tests/e2e/test_api.py"
      name: "test_post_questionnaire_list_k"
    - path: "backend/tests/e2e/test_api.py"
      name: "test_post_questionnaire_ils"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_learning_path"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_learning_path_ga"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_calculate_learning_path"
    - path: "backend/tests/unit/test_learners_model.py"
      name: "TestBasicQuestionnaireAlgorithms::test_basic_ils_algorithm"
    - path: "backend/tests/unit/test_learners_model.py"
      name: "TestBasicQuestionnaireAlgorithms::test_basic_listk_algorithm"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_style_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_strategy_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_learning_style_by_student_id"
    - path: "frontend/src/services/Questionnaire/postILS.test.tsx"
      name: "postILS has expected behaviour"
    - path: "frontend/src/services/Questionnaire/postListK.test.tsx"
      name: "postListK has expected behaviour"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_for_student"
    - path: "frontend/src/store/Slices/LearningPathElementSlice.test.ts"
      name: "LearningPathElementSlice caching"
---

## Beschreibung

Das HASKI-System **shall** Lernpfade automatisch an die individuellen Lernstile, Interessen und Kompetenzen der Studierenden anpassen. Das System **shall** basierend auf den Ergebnissen des ILS-Fragebogens (Index of Learning Styles) personalisierte Lernempfehlungen generieren und den Studierenden adaptive Lernpfade bereitstellen.
Zusätzlich **shall** das System bereits berechnete und persistierte Lernpfade pro Kurs/Topic abrufbar machen, um konsistente Anzeigen in Frontend, Tutoring-Modell und Analytics zu ermöglichen, ohne eine erneute Berechnung anzustoßen.

## Akzeptanzkriterien

### Lernpfad-Berechnung (GH-239)

- [x] Lernpfad wird automatisch nach dem Absenden des ILS-Fragebogens berechnet
- [x] Berechnung berücksichtigt die ILS-Dimensionen des Studierenden
- [x] Algorithmen sind konfigurierbar für verschiedene Standorte (Kempten, Aschaffenburg)
- [x] Topic-IDs werden in die Lernpfad-Generierung einbezogen

### ILS-Verarbeitung (GH-209)

- [x] ILS-Antworten werden durch einen Algorithmus im Backend verarbeitet
- [x] Lernstil-Dimensionen werden aus den ILS-Antworten bestimmt
- [x] Studierende können ihre ILS-Ergebnisse im Frontend einsehen
- [x] Lernpfad-Algorithmus kann die bestimmten Dimensionen verwenden

### ILS-Pflichterfüllung (GH-220)

- [x] System prüft beim Start, ob ILS-Ergebnisse vorliegen (fetch ILS)
- [x] Wenn ILS-Ergebnisse vorhanden sind, wird localStorage entsprechend gesetzt
- [x] Ohne ILS-Ergebnisse wird der ILS-Fragebogen angezeigt
- [x] Modal kann weggeklickt werden, öffnet sich aber erneut, wenn Antworten nicht gesendet wurden
- [x] Nach erfolgreichem Absenden wird die Information im Cookie gespeichert

### Datenpersistierung (GH-182)

- [x] ILS-Fragebogen-Antworten werden an Backend gesendet
- [x] Antworten werden persistent gespeichert
- [x] ILS-Short und LIST-K Fragebogen-Antworten werden ebenfalls persistiert

### Adaptive Lernpfad-Funktionalität

- [x] Lernpfade werden individuell für jeden Studierenden generiert
- [x] System berücksichtigt Lernstil-Präferenzen bei der Content-Empfehlung
- [x] Lernpfade sind zugänglich und nutzbar nach ILS-Absolvierung
- [x] System verhindert Nutzung ohne absolvierte ILS-Erfassung
- [x] Backend stellt einen abgesicherten `POST /user/<user_id>/<moodle_user_id>/student/<student_id>/course/<course_id>/topic/<topic_id>/learningPath`-Endpunkt bereit, der berechnete Lernpfade (inkl. `based_on`, `path`, `calculated_on`) speichert und als JSON zurückliefert
- [x] Der Lernpfad-Endpunkt akzeptiert den Parameter `algorithm="ga"` und triggert den genetischen Algorithmus (GH-23)
- [x] Ein `POST /user/<user_id>/<moodle_user_id>/learningPath`-Aufruf ohne Algorithmus-Parameter löst die gespeicherten Tutor:innen-/Student:innen-Präferenzen aus und liefert den berechneten Pfad zurück (GH-93)

### Persistierter Lernpfad-Abruf (GH-30)

- [x] Das System stellt den zuletzt gespeicherten Lernpfad eines Studierenden für ein Kurs-/Topic-Paar aus dem Persistenzspeicher bereit.
- [x] Der Abruf liefert alle relevanten Metadaten (z. B. Berechnungszeitpunkt, Grundlage, Sequenz der Elemente), sodass der Datensatz ohne Zusatzlogik in allen Kanälen verwendet werden kann.
- [x] Lernpfade außerhalb der eigenen Einschreibung werden nicht ausgeliefert.

## Rationale

Primary implementation: GitHub issue GH-239: "User learning path is calculated after submitting ILS questionnaire"

Backend-Issue [GH-2](https://github.com/HASKI-RAK/HASKI-Backend/issues/2) stellt sicher, dass die Lernpfad-Berechnung als REST-Endpunkt verfügbar ist und die vom Tutoring-Model berechneten Sequenzen direkt an das Frontend geliefert werden.

Related work:

- GH-209: Implementiert den ILS-Algorithmus zur Verarbeitung der Fragebogen-Antworten und Bestimmung der Lernstil-Dimensionen
- GH-220: Stellt sicher, dass Studierende den ILS-Fragebogen ausfüllen, bevor sie das System nutzen können (Voraussetzung für personalisierte Lernpfade)
- GH-182: Implementiert die Persistierung der Fragebogen-Antworten (ILS, ILS-Short, LIST-K) im Backend

Derived from system requirement SyRS-FUNC-001, which implements stakeholder requirement StRS-101.

SyRS-FUNC-008 fordert konsistente adaptive Lernräume. Der Abruf eines gespeicherten Lernpfads stellt sicher, dass Studierende und Lehrende jederzeit denselben Vorschlag sehen wie die Tutoring-Algorithmen, auch wenn aktuell keine neue Berechnung läuft.

Die automatische Anpassung von Lernpfaden ist eine Kernfunktionalität des HASKI-Systems und differenziert es von herkömmlichen Lernmanagementsystemen. Durch die Berücksichtigung individueller Lernstile (basierend auf dem ILS-Modell), Interessen und Kompetenzen wird die Motivation, Akzeptanz und der Lernerfolg der Studierenden gefördert.

## Hinweise

- **Primary issue**: [GH-239](https://github.com/HASKI-RAK/HASKI-Frontend/issues/239) - Implementiert die eigentliche Lernpfad-Berechnung nach ILS-Absolvierung
- **Related issues**:
  - [GH-23](https://github.com/HASKI-RAK/HASKI-Backend/issues/23) - Genetischer Algorithmus für Lernpfad-Berechnungen
  - [GH-209](https://github.com/HASKI-RAK/HASKI-Frontend/issues/209) - ILS-Algorithmus im Backend
  - [GH-220](https://github.com/HASKI-RAK/HASKI-Frontend/issues/220) - ILS-Pflicht für Frontend-Nutzung
  - [GH-182](https://github.com/HASKI-RAK/HASKI-Frontend/issues/182) - Fragebogen-Datenpersistierung
- **Backend-Verifikation**: `backend/tests/e2e/test_api.py::test_post_questionnaire_list_k` prüft die Persistierung und Validierung der LIST-K-Antworten, während `backend/tests/e2e/test_api.py::test_post_questionnaire_ils` die ILS-Lang- und Kurzfragebögen absichert – beide in direkter Umsetzung von [GH-182](https://github.com/HASKI-RAK/HASKI-Frontend/issues/182).
- **Technical details**:
  - Verwendet den Index of Learning Styles (ILS) zur Bestimmung von Lernstil-Präferenzen
  - Algorithmen sind hardcoded aber konfigurierbar für verschiedene Hochschul-Standorte
  - Integration mit "Marc's Learning Path Algorithm" für die eigentliche Pfad-Generierung
  - Speicherung des ILS-Status in localStorage und Cookie
- **Persistierte Lernpfade**:
  - Felder und Beziehungen orientieren sich am Lernpfad-Datenmodell (siehe OAS und Backend-Dokumentation).
  - Autorisierungs- und Filterregeln sind konsistent zu Topic- und Subtopic-Abfragen umzusetzen.
- **Dependencies**: ILS-Fragebogen muss ausgefüllt sein, bevor Lernpfade generiert werden können
- **Status**: Alle vier Issues sind implementiert und geschlossen (Juli 2023 - Dezember 2023)
