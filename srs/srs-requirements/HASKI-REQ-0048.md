---
id: HASKI-REQ-0048
title: Lernprofil-Daten über REST abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-007
links:
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#81"]
  parents: ["SyRS-FUNC-007"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_students_learning_characteristics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_students_learning_analytics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_students_learning_style"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_students_learning_strategy"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_students_knowledge"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_update_learning_style_by_student_id"
    - path: "backend/tests/unit/test_service.py"
      name: "test_update_learning_style_by_student_id"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_characteristics"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_learning_characteristics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_analytics"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_style"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_learning_strategy"
    - path: "backend/tests/unit/test_service.py"
      name: "test_reset_learning_strategy_by_student_id"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_reset_knowledge"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_ils_input_answers"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_ils_perception_answers"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_ils_processing_answers"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_ils_understanding_answers"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_questionnaire_list_k"
    - path: "backend/tests/unit/test_service.py"
      name: "test_delete_questionnaire_ils"
  merged_from:
    [
      "HASKI-REQ-0049",
      "HASKI-REQ-0050",
      "HASKI-REQ-0051",
      "HASKI-REQ-0052",
      "HASKI-REQ-0074",
      "HASKI-REQ-0079",
    ]
---

## Beschreibung

Das System **shall** eine abgesicherte REST-Schnittstelle bereitstellen, über die authentifizierte Rollen (Studierende, Lehrende) die konsolidierten Lerncharakteristika eines Studierenden abrufen können. Die Antwort **shall** mindestens den aktuellen Lernstil (ILS-Basiswerte), Lernstrategie-Vektoren, Learning-Analytics-Metriken und Wissensstände enthalten, sodass Dashboards und Lernpfad-Berechnungen auf denselben Datenpool zugreifen. Die Endpunkte **shall** Moodle-IDs akzeptieren und auf automatisch angelegte Nutzerprofile (GH-81) referenzieren, damit neu registrierte Personen ohne zusätzlichen Abgleich sichtbar werden.

Die folgenden spezialisierten Endpunkte werden bereitgestellt:

### Konsolidierte Lerncharakteristika

`GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningCharacteristics`

### Learning Analytics

`GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningAnalytics`

- Liefert aktuelle Learning-Analytics-Metriken (z.B. `engagement`, `activity_counts`, `last_activity_at`)

### Lernstil (Felder-Silverman-Modell)

`GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningStyle`

- Liefert die vier FSLSM-Dimensionen: `input`, `perception`, `processing`, `understanding` mit jeweiliger Dimension und Ausprägung

### Lernstrategien

`GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningStrategy`

- Liefert den vollständigen Lernstrategie-Datensatz einschließlich aller verfügbaren Dimensionen

### Wissensstände

`GET /user/<user_id>/<lms_user_id>/student/<student_id>/knowledge`

- Liefert sämtliche bekannten Wissensstandeinträge in strukturierter Form

### Aktualisierung der Lernstil-Dimensionen

`PUT /user/<user_id>/<lms_user_id>/student/<student_id>/learningStyle`

- Aktualisiert die vier Dimensionen des Felder–Silverman-Lernstilmodells (Perception, Input, Processing, Understanding) mitsamt numerischer Ausprägung für das adressierte Lernprofil.

### Reset von Lernprofil-Daten

`DELETE /user/<user_id>/<lms_user_id>/student/<student_id>/learningCharacteristics`

- Setzt sämtliche abhängigen Artefakte (Learning-Analytics-Metriken, Lernstil, Lernstrategie, Knowledge) in einem Schritt auf ihre Defaultwerte zurück und liefert den neu initialisierten Datensatz in derselben Struktur wie der `GET`-Endpoint.

Zusätzlich stehen granulare `DELETE`-Routen für `learningAnalytics`, `learningStyle`, `learningStrategy` und `knowledge` zur Verfügung, über die einzelne Teilbereiche des Lernprofils separat auf Defaultwerte zurückgesetzt werden können.

## Akzeptanzkriterien

### Allgemein

- [x] `GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningCharacteristics` liefert ein JSON mit den Schlüsseln `learning_style`, `learning_strategy`, `learning_analytics`, `knowledge`.
- [x] Die Antwort bezieht sich ausschließlich auf den abgefragten Studierenden; Fremddaten werden ausgeschlossen.
- [x] Nicht vorhandene Studierende oder inkonsistente ID-Kombinationen führen zu HTTP 404 mit einer strukturierten Fehlermeldung (`{"error": "...", "message": "..."}`) ohne Seiteneffekte.
- [x] Die Implementierung folgt der im OAS von GH-30 definierten Struktur, damit Frontend-Komponenten die Daten ohne Mapping abrufen können.
- [x] Sobald ein Studierender durch GH-81 automatisch angelegt wird, stehen seine Lernprofil-Daten über denselben Endpunkt zur Verfügung.

### Learning Analytics

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und serialisieren den Learning-Analytics-Datensatz (z.B. `engagement`, `activity_counts`, `last_activity_at`); Leerlisten sind zulässig.
- [x] Der Endpoint akzeptiert Moodle-IDs (`lms_user_id`) und mappt sie deterministisch auf HASKI-Studenten.
- [x] Lernanalytics-Datensätze, die durch GH-81 automatisch angelegt werden, sind unmittelbar abrufbar.

### Lernstil

- [x] Erfolgreiche Aufrufe liefern HTTP 200 sowie alle acht erwarteten Schlüssel (`perception_dimension`, `perception_value`, `input_dimension`, `input_value`, `processing_dimension`, `processing_value`, `understanding_dimension`, `understanding_value`).
- [x] Die Werte spiegeln exakt den gespeicherten Lernstil-Datensatz aus der `learning_style`-Tabelle wider und berücksichtigen Updates aus ILS-/LIST-K-Fragebögen.

### Aktualisierung der Lernstil-Dimensionen

- [x] Erfolgreiche Aufrufe des `PUT /.../learningStyle`-Endpoints liefern HTTP 201 sowie alle acht Felder (`*_dimension`, `*_value`) der FSLSM-Darstellung und spiegeln den persistenten Datensatz wider.
- [x] Die numerischen Werte müssen im Bereich 1–11 liegen; Werte außerhalb oder fehlende Felder führen zu HTTP 400 mit der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`).
- [x] Ungültige Typen (z. B. Strings statt Integern) oder leere Requests werden deterministisch mit HTTP 400 beantwortet.
- [x] Nicht existente Nutzer- oder Studierendenkombinationen resultieren in HTTP 404 ohne Offenlegung interner Details.
- [x] Nach erfolgreichem Update geben `GET /learningStyle` sowie `GET /learningCharacteristics` dieselben Werte aus, sodass Reports und Empfehlungsalgorithmen konsistent bleiben.

### Reset von Lernprofil-Daten

- [x] Ein valider Aufruf von `DELETE /.../learningCharacteristics` liefert HTTP 200 sowie ein JSON mit den Schlüsseln `learning_style`, `learning_strategy`, `learning_analytics`, `knowledge` und verweist auf die neu initialisierten Defaultdatensätze.
- [x] Die Einzel-Endpoints (`.../learningAnalytics`, `.../learningStyle`, `.../learningStrategy`, `.../knowledge`) liefern jeweils HTTP 200 samt neuem Datensatz und verändern ausschließlich den adressierten Teilbereich.
- [x] Nicht vorhandene oder nicht zusammenpassende `user_id`/`lms_user_id`/`student_id`-Kombinationen werden mit HTTP 404 und der standardisierten Fehlstruktur (`{"error": "...", "message": "..."}`) beantwortet.
- [x] Direkt nach einem Reset liefern die entsprechenden `GET`-Endpoints wieder die Defaultwerte aus GH-81, sodass Lernpfadberechnungen deterministisch weiterlaufen.

### Lernstrategien

- [x] Berechtigte Anfragen liefern den vollständigen Lernstrategie-Datensatz einschließlich aller verfügbaren Dimensionen.
- [x] Die ausgegebenen Werte spiegeln unmittelbar die zuletzt erfassten Fragebogen- oder Analytics-Ergebnisse wider.

### Wissensstände

- [x] Die Antwort enthält sämtliche bekannten Wissensstandeinträge des angefragten Studierenden in strukturierter Form.
- [x] Aktualisierte Werte stehen ohne Verzögerung für Lernpfadberechnungen, Dashboards und externe Auswertungen zur Verfügung.

### Autorisierung (alle Endpunkte)

- [x] Zugriff erfordert authentifizierte Nutzer (Tutor oder Studierende), die nur ihre eigenen oder berechtigten Datensätze abrufen dürfen.
- [x] Anfragen außerhalb des autorisierten Kontextes werden datenschutzkonform abgewiesen.
- [x] Autorisierung wird über bestehende Middleware/Decorator sichergestellt; direkte Zugriffe ohne Session/Cookie werden abgelehnt.

## Rationale

Primary implementation: GitHub issue GH-30 ("Implement Basic Setup 2.0") definiert die REST-Endpunkte für Lernprofile und deren Antwortstruktur.
Related work: GH-81 stellt sicher, dass bei der ersten Anmeldung sämtliche Lerncharakteristika persistiert werden und somit abrufbar sind.
Derived from system requirement SyRS-FUNC-007 (Reports über Lernfortschritte).

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Die Lernprofil-Daten werden sowohl für Lehrenden-Übersichten als auch für personalisierte Empfehlungen wiederverwendet.
- Fehlerhafte Aufrufe müssen geloggt werden, um Support- und Datenschutz-Anfragen nachvollziehen zu können.
