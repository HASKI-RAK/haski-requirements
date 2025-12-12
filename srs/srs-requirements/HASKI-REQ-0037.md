---
id: HASKI-REQ-0037
title: Automatische Learning-Element-Anlage aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003", "SyRS-FUNC-008"]
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Frontend#135"
    - "HASKI-RAK/HASKI-Frontend#257"
    - "HASKI-RAK/HASKI-Backend#30"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_create_le_from_moodle"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_topics_and_elements_from_moodle_course"
    - path: "backend/tests/unit/test_service.py"
      name: "test_create_learning_element"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_learning_element_by_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_get_moodle_course_content"
    - path: "frontend/src/components/CreateLearningElement/CreateLearningElement.test.tsx"
      name: "CreateLearningElement Component"
    - path: "frontend/src/components/CreateLearningElement/CreateLearningElementModal.test.tsx"
      name: "CreateLearningElementModal Component"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElement/CreateLearningElementTable.test.tsx"
      name: "CreateLearningElementTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElement/CreateLearningElementTable.hooks.test.tsx"
      name: "useCreateLearningElementTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElementClassification/CreateLearningElementClassificationTable.test.tsx"
      name: "CreateLearningElementClassificationTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElementClassification/CreateLearningElementClassificationTable.hooks.test.tsx"
      name: "useCreateLearningElementClassificationTable"
    - path: "frontend/src/components/CreateTopic/Modal/CreateLearningElementsStep/CreateLearningElementsStep.test.tsx"
      name: "CreateLearningElementsStep"
    - path: "frontend/src/components/CreateTopic/Modal/CreateLearningElementClassificationsStep/CreateLearningElementClassificationsStep.test.tsx"
      name: "CreateLearningElementClassificationsStep"
    - path: "frontend/src/services/LearningElement/postLearningElement.test.tsx"
      name: "postLearningElement has expected behaviour"
    - path: "frontend/src/services/LearningElement/deleteLearningElement.test.tsx"
      name: "deleteLearningElement has expected behaviour"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_le_from_moodle"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_learning_element"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_delete_le_from_moodle"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_les_for_topic_for_student"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_le_by_id_for_student"
---

## Beschreibung

Das System **shall** Learning Elements automatisch auf Basis der von Moodle gelieferten Aktivitätsdaten erzeugen. Dabei **shall** alle relevanten Metadaten (LMS-ID, Aktivitätstyp, Klassifikation, Name, Erstellungszeitpunkt, Verantwortliche Person, Hochschule) persistiert und dem passenden Topic/Subtopic zugeordnet werden. Bereits vorhandene Learning Elements **shall** über ihre LMS-ID erkannt und nicht dupliziert werden; Fehler in der Nutzereingabe (fehlende Felder, falsche Datentypen) **shall** durch klare Fehlermeldungen abgefangen werden. Das Frontend **shall** Lehrenden einen mehrstufigen Import-Dialog anbieten, der die Moodle-Aktivitäten pro Topic sichtbar macht, Auswahl- und Klassifikationsschritte orchestriert und den Import direkt mit der Backend-Synchronisation verknüpft.

Ergänzend **shall** das Backend einen Endpunkt `PUT /lms/learningElement/<learning_element_id>/<moodle_learning_element_id>` bereitstellen, über den Moodle aktualisierte Metadaten eines Learning Elements (z. B. Aktivitätstyp, Klassifikation, Name, Verantwortliche Person, Zeitstempel, Universität) nach HASKI synchronisiert. Die Route **shall** die Kombination aus interner Learning-Element-ID und Moodle-ID validieren, bevor Änderungen geschrieben werden, damit bestehende Zuordnungen zu Topics/Subtopics unverändert bleiben.

Für alle von Moodle synchronisierten Learning Elements **shall** zusätzlich ein abgesicherter `DELETE`-Endpunkt bereitstehen, der das adressierte Learning Element mitsamt abhängigen Ratings und Relationen entfernt und eine Bestätigung zurückliefert. Während des Löschens **shall** abhängige Strukturen gemäß den Vorgaben der Kursstruktur-CRUD-Schnittstellen konsistent bereinigt werden, sodass keine verwaisten Referenzen verbleiben.

Ergänzend **shall** das System eingeschriebenen Studierenden Learning Elements über REST bereitstellen, sowohl als Liste aller Elemente eines Topics als auch als gezielte Einzelabfrage. Damit können Empfehlungssysteme, Dashboards und Tracking-Funktionen identische Daten verwenden, ohne mehrere Datenquellen abgleichen zu müssen. Darüber hinaus **shall** das System allen berechtigten Studierenden eine vollständige Liste der Learning Elements eines belegten Kurses liefern, inklusive individueller Lernfortschrittsinformationen, damit Lernräume, Empfehlungen und Visualisierungen direkt mit der gelieferten Struktur arbeiten können.

## Akzeptanzkriterien

### Backend-Synchronisation (Anlage)

- [x] Ein REST-Endpunkt erlaubt das Anlegen von Learning Elements je Topic/Subtopic auf Basis der Moodle-LMS-ID.
- [x] Pflichtattribute (LMS-ID, Aktivitätstyp, Klassifikation, Name, Universität, Zeitstempel, created_by) werden validiert und gespeichert.
- [x] Learning Elements werden automatisch dem korrekten Topic/Subtopic (parent_id) zugeordnet.
- [x] Duplicate LMS-IDs werden erkannt und führen zu einer 400-Fehlerantwort ohne zweite Anlage.
- [x] Ungültige Eingabedatentypen und fehlende Pflichtfelder erzeugen nachvollziehbare Fehlermeldungen.
- [x] Erfolgreich angelegte Learning Elements stehen unmittelbar für Lernpfade, Ratings und Empfehlungen zur Verfügung.

### Backend-Synchronisation (Aktualisierung & Löschen)

- [x] Erfolgreiche Updates über `PUT /lms/learningElement/<learning_element_id>/<moodle_learning_element_id>` liefern HTTP 201 und geben `id`, `lms_id`, `activity_type`, `classification`, `name`, `created_by`, `created_at`, `university` zurück.
- [x] Fehlende Pflichtfelder oder falsche Datentypen führen zu HTTP 400 mit der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) und resultieren in keiner Datenänderung.
- [x] Ungültige ID-Kombinationen werden mit HTTP 404 beantwortet, ohne interne Details offenzulegen.
- [x] Die Zuordnung zum Topic/Subtopic bleibt unverändert; für verschobene Elemente muss ein eigener Move-Workflow verwendet werden.
- [x] Zeitstempel werden auf valide ISO-8601-Formate geprüft, um Änderungsverfolgung und Synchronisation mit Moodle zu gewährleisten.
- [x] Ein `DELETE`-Endpunkt für synchronisierte Learning Elements entfernt das adressierte Objekt mitsamt abhängigen Ratings und Relationen transaktional und bestätigt den Erfolg mit HTTP 200; Fehlerzustände führen zu einem vollständigen Rollback.

### Learning Elements über REST abrufen

- [x] Die REST-Schnittstelle stellt allen berechtigten Studierenden eine Liste der Learning Elements eines Topics zur Verfügung, einschließlich relevanter Metadaten (z. B. Typ, Klassifikation, Name, LMS-Referenz) und des zugehörigen `student_learning_element`-Status.
- [x] Topics oder Kurse, zu denen kein legitimer Zugriff besteht, liefern keine Daten; unberechtigte Abfragen werden mit geeigneten Fehlercodes beantwortet.
- [x] Änderungen an Learning Elements (z. B. Aktualisierung oder Löschen) werden ohne zusätzliche Synchronisationsschritte in Listen- und Detailaufrufen sichtbar.
- [x] Für gültige Kombinationen aus Studierendem, Kurs, Topic und Learning Element liefert ein Detailendpunkt sämtliche relevanten Metadaten sowie den `student_learning_element`-Kontext; entfernte Elemente werden nicht mehr ausgegeben.
- [x] Die REST-Endpunkte für Learning-Element-Listen und -Details verwenden eine einheitliche Datenstruktur, sodass Frontends dieselben Komponenten wiederverwenden können.

### Frontend-Import-Dialog (GH-135, GH-257)

- [x] Ein "Learning Element importieren"-Auslöser öffnet einen Modal-Dialog, der die aus Moodle geladenen Aktivitäten des aktuellen Topics auflistet.
- [x] Lehrende können mindestens ein Learning Element auswählen und innerhalb des Dialogs zur Bestätigungsansicht weiter navigieren.
- [x] Auswahlfunktionen unterstützen Einzel- sowie "Alle auswählen/abwählen"-Aktionen pro Topic und spiegeln den aktuellen Status in der Tabelle wider.
- [x] Für jedes ausgewählte Learning Element steht eine Klassifikationsauswahl zur Verfügung; Änderungen werden in die Importkonfiguration übernommen.
- [x] Fehler beim Abrufen von Nutzer-, Topic- oder Aktivitätsdaten lösen eine sichtbare Snackbar-Warnung aus, damit Lehrende auf Integrationsprobleme reagieren können.

## Rationale

Die automatische Übernahme der Moodle-Aktivitäten stellt sicher, dass Learning Elements ohne manuelle Nacharbeit in HASKI verfügbar sind und konsistent mit der führenden Lernplattform bleiben. Die Funktionalität wurde im Rahmen von GitHub Issue [GH-21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) implementiert und durch die E2E-Tests zur Learning-Element-Anlage verifiziert. Issue [#135](https://github.com/HASKI-RAK/HASKI-Frontend/issues/135) liefert den dazugehörigen Frontend-Dialog, während [#257](https://github.com/HASKI-RAK/HASKI-Frontend/issues/257) den erweiterten Klassifikationskatalog für importierte Aktivitäten ergänzt.
Die standardisierte Auslieferung von Learning-Element-Listen und -Details über REST stellt sicher, dass Lernpfadansichten, Feedbackdialoge, Auswertungen und Tutoring-Komponenten konsistent auf denselben Datenbestand zugreifen können und gleichzeitig die geltenden Einschreibungsregeln respektiert werden.

## Hinweise

- Die React-Komponenten `CreateLearningElement*` und die zugehörigen Modal-Schritte synchronisieren ihre Auswahlzustände über `useCreateLearningElementTable` und geben den Import nach erfolgreicher Klassifikation an das Backend weiter.
- Der Dialog nutzt React Flow und den Snackbar-Kontext, um Einbettung und Fehlermeldungen konsistent mit dem Lernpfad-Editor zu halten.
- Backend- und Frontend-Tests decken gemeinsam die Ende-zu-Ende-Synchronisation ab (Import → Klassifikation → Persistenz).
