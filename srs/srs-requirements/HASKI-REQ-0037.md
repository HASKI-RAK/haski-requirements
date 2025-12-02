---
id: HASKI-REQ-0037
title: Automatische Learning-Element-Anlage aus Moodle
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003"]
  stories:
    - "HASKI-RAK/HASKI-Backend#21"
    - "HASKI-RAK/HASKI-Frontend#135"
    - "HASKI-RAK/HASKI-Frontend#257"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_create_le_from_moodle"
    - path: "frontend/src/components/CreateLearningElement/CreateLearningElement.test.tsx"
      name: "CreateLearningElement Component"
    - path: "frontend/src/components/CreateLearningElement/CreateLearningElementModal.test.tsx"
      name: "CreateLearningElementModal Component"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElement/CreateLearningElementTable.test.tsx"
      name: "CreateLearningElementTable"
    - path: "frontend/src/components/CreateTopic/Table/CreateLearningElementClassification/CreateLearningElementClassificationTable.test.tsx"
      name: "CreateLearningElementClassificationTable"
    - path: "frontend/src/components/CreateTopic/Modal/CreateLearningElementsStep/CreateLearningElementsStep.test.tsx"
      name: "CreateLearningElementsStep"
    - path: "frontend/src/components/CreateTopic/Modal/CreateLearningElementClassificationsStep/CreateLearningElementClassificationsStep.test.tsx"
      name: "CreateLearningElementClassificationsStep"
---

## Beschreibung

Das System **shall** Learning Elements automatisch auf Basis der von Moodle gelieferten Aktivitätsdaten erzeugen. Dabei **shall** alle relevanten Metadaten (LMS-ID, Aktivitätstyp, Klassifikation, Name, Erstellungszeitpunkt, Verantwortliche Person, Hochschule) persistiert und dem passenden Topic/Subtopic zugeordnet werden. Bereits vorhandene Learning Elements **shall** über ihre LMS-ID erkannt und nicht dupliziert werden; Fehler in der Nutzereingabe (fehlende Felder, falsche Datentypen) **shall** durch klare Fehlermeldungen abgefangen werden. Das Frontend **shall** Lehrenden einen mehrstufigen Import-Dialog anbieten, der die Moodle-Aktivitäten pro Topic sichtbar macht, Auswahl- und Klassifikationsschritte orchestriert und den Import direkt mit der Backend-Synchronisation verknüpft.

## Akzeptanzkriterien

### Backend-Synchronisation (GH-21)

- [x] Ein REST-Endpunkt erlaubt das Anlegen von Learning Elements je Topic/Subtopic auf Basis der Moodle-LMS-ID.
- [x] Pflichtattribute (LMS-ID, Aktivitätstyp, Klassifikation, Name, Universität, Zeitstempel, created_by) werden validiert und gespeichert.
- [x] Learning Elements werden automatisch dem korrekten Topic/Subtopic (parent_id) zugeordnet.
- [x] Duplicate LMS-IDs werden erkannt und führen zu einer 400-Fehlerantwort ohne zweite Anlage.
- [x] Ungültige Eingabedatentypen und fehlende Pflichtfelder erzeugen nachvollziehbare Fehlermeldungen.
- [x] Erfolgreich angelegte Learning Elements stehen unmittelbar für Lernpfade, Ratings und Empfehlungen zur Verfügung.

### Frontend-Import-Dialog (GH-135, GH-257)

- [x] Ein "Learning Element importieren"-Auslöser öffnet einen Modal-Dialog, der die aus Moodle geladenen Aktivitäten des aktuellen Topics auflistet.
- [x] Lehrende können mindestens ein Learning Element auswählen und innerhalb des Dialogs zur Bestätigungsansicht weiter navigieren.
- [x] Auswahlfunktionen unterstützen Einzel- sowie "Alle auswählen/abwählen"-Aktionen pro Topic und spiegeln den aktuellen Status in der Tabelle wider.
- [x] Für jedes ausgewählte Learning Element steht eine Klassifikationsauswahl zur Verfügung; Änderungen werden in die Importkonfiguration übernommen.
- [x] Fehler beim Abrufen von Nutzer-, Topic- oder Aktivitätsdaten lösen eine sichtbare Snackbar-Warnung aus, damit Lehrende auf Integrationsprobleme reagieren können.

## Rationale

Die automatische Übernahme der Moodle-Aktivitäten stellt sicher, dass Learning Elements ohne manuelle Nacharbeit in HASKI verfügbar sind und konsistent mit der führenden Lernplattform bleiben. Die Funktionalität wurde im Rahmen von GitHub Issue [GH-21](https://github.com/HASKI-RAK/HASKI-Backend/issues/21) implementiert und durch die E2E-Tests zur Learning-Element-Anlage verifiziert. Issue [#135](https://github.com/HASKI-RAK/HASKI-Frontend/issues/135) liefert den dazugehörigen Frontend-Dialog, während [#257](https://github.com/HASKI-RAK/HASKI-Frontend/issues/257) den erweiterten Klassifikationskatalog für importierte Aktivitäten ergänzt.

## Hinweise

- Die React-Komponenten `CreateLearningElement*` und die zugehörigen Modal-Schritte synchronisieren ihre Auswahlzustände über `useCreateLearningElementTable` und geben den Import nach erfolgreicher Klassifikation an das Backend weiter.
- Der Dialog nutzt React Flow und den Snackbar-Kontext, um Einbettung und Fehlermeldungen konsistent mit dem Lernpfad-Editor zu halten.
- Backend- und Frontend-Tests decken gemeinsam die Ende-zu-Ende-Synchronisation ab (Import → Klassifikation → Persistenz).
