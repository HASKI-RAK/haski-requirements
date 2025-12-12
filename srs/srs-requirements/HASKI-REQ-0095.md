---
id: HASKI-REQ-0095
title: Adaptive Learning Path Generation
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  stories: ["GH-1", "GH-2", "GH-6", "GH-8", "GH-22", "GH-23", "GH-24", "GH-76"]
  tests:
    - path: "backend/tests/unit/test_service.py"
      name: "test_student_learning_element_visit"
    - path: "backend/tests/unit/test_service.py"
      name: "test_student_topic_visit"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_path"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_learning_paths_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_knowledge_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_analytics_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_path"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_knowledge_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_learning_analytics_by_student_id"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_aco"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_distance"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_get_coordinates"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_tyche"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_nestor"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_training_nestor"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_with_out_of_range_learning_style_for_ga"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_learning_style_check"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_calculate_variable_score_graf"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_ga_2"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_ga"
    - path: "backend/tests/unit/test_tutoring_model.py"
      name: "test_prepare_les_for_ga_for_all"
  parents: []
---

## Beschreibung

Das System **shall** adaptive Lernpfade für Studierende auf Basis ausgewählter Algorithmen (z. B. ACO, Graph-basiert) generieren.
Das System **shall** die generierten Lernpfade persistent speichern.
Das System **shall** das Abrufen des generierten Lernpfads für eine:n Studierende:n in einem bestimmten Kurs/Topic ermöglichen.
Das System **shall** das Löschen von Lernpfaden für eine:n Studierende:n ermöglichen (z. B. zur Neu-Generierung).

## Akzeptanzkriterien

### Generierung adaptiver Lernpfade

- [x] Für eine:n angemeldete:n Studierende:n und ein gültiges Kurs/Topic-Paar kann ein adaptiver Lernpfad über einen REST-Endpunkt erzeugt werden.
- [x] Die Generierung berücksichtigt die gewählten Lernpfad-Algorithmen (z. B. ACO, Graph-basiert, GA, Nestor, Tyche) und nutzt die im System hinterlegten Lernstildaten, Wissensstände und Learning Analytics.
- [x] Die Reihenfolge der im Lernpfad enthaltenen Learning Elements entspricht deterministisch der Ausgabe des jeweils gewählten Algorithmus.
- [x] Bei ungültigen oder nicht unterstützten Algorithmen wird keine Pfadgenerierung durchgeführt und eine geeignete Fehlermeldung zurückgegeben.

### Persistenz der Lernpfade

- [x] Nach erfolgreicher Generierung ist der Lernpfad in der Datenbank persistent gespeichert und eindeutig einem/einer Studierenden, einem Kurs und ggf. einem Topic zugeordnet.
- [x] Eine erneute Generierung für dieselbe Studierenden‑/Kurs‑/Topic-Kombination ersetzt den bisherigen Lernpfad konsistent (kein Mischen von alten und neuen Einträgen).
- [x] Teilweise fehlgeschlagene Generierungen führen zu keinem inkonsistenten Persistenzzustand; entweder existiert ein vollständiger Lernpfad oder gar keiner (transaktionales Verhalten).

### Abruf der Lernpfade

- [x] Ein REST-Endpunkt liefert für eine:n Studierende:n den aktuellen Lernpfad für einen Kurs bzw. ein Topic als geordnete Liste von Learning Elements mit allen für die Darstellung erforderlichen Metadaten.
- [x] Nur Lernpfade der anfragenden Person oder von berechtigten Rollen (z. B. Tutor:innen, Admins) können abgerufen werden; unberechtigte Zugriffe werden abgewiesen.
- [x] Änderungen an zugrunde liegenden Learning Elements (z. B. gelöschte Elemente) werden beim Abruf berücksichtigt, sodass keine ungültigen Verweise im Pfad zurückgegeben werden.

### Löschen und Neu-Generierung

- [x] Ein gesicherter REST-Endpunkt erlaubt das Löschen aller gespeicherten Lernpfade einer:s Studierenden (optional eingeschränkt auf Kurs/Topic), ohne andere Personen zu beeinflussen.
- [x] Nach dem Löschen ist kein Lernpfad für die betroffene Studierenden‑/Kurs‑/Topic-Kombination mehr abrufbar, bis eine erneute Generierung durchgeführt wird.
- [x] Lösch- und Neu-Generierungsoperationen werden protokolliert, sodass Änderungen an Lernpfaden nachvollziehbar sind.

## Rationale

Primäre Implementierung: GitHub-Issues GH-1, GH-2, GH-6, GH-8, GH-22, GH-23, GH-24 und GH-76 beschreiben die Einführung und Weiterentwicklung der adaptiven Lernpfad-Algorithmen (z. B. ACO, GA, graphbasierte Verfahren) sowie deren Integration in das Tutoring-Modell.
Die Anforderung bündelt diese Arbeiten zu einem konsistenten Funktionsumfang für die Generierung, Persistenz, den Abruf und das Zurücksetzen individueller Lernpfade pro Studierende:n, Kurs und Topic.

## Hinweise

- Primäre Issues (Auswahl):
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/1
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/2
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/6
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/8
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/22
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/23
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/24
  - https://github.com/HASKI-RAK/HASKI-Backend/issues/76
- Die technische Umsetzung greift auf das Tutoring-Modell, Lernstildaten, Wissensstände und Learning Analytics zu und ist damit von stabilen Domänenmodellen in diesen Bereichen abhängig.
- Performance- und Skalierbarkeitsaspekte (z. B. bei vielen gleichzeitigen Pfadgenerierungen) sind in der Infrastruktur zu berücksichtigen, insbesondere hinsichtlich Caching-Strategien und asynchroner Verarbeitung.
- Änderungen an den zugrunde liegenden Algorithmen müssen abwärtskompatibel gestaltet oder über Migrationspfade für bestehende Lernpfade abgesichert werden.
