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
---

## Beschreibung

Das System **shall** eine abgesicherte REST-Schnittstelle bereitstellen, über die authentifizierte Rollen (Studierende, Lehrende) die konsolidierten Lerncharakteristika eines Studierenden abrufen können. Die Antwort **shall** mindestens den aktuellen Lernstil (ILS-Basiswerte), Lernstrategie-Vektoren, Learning-Analytics-Metriken und Wissensstände enthalten, sodass Dashboards und Lernpfad-Berechnungen auf denselben Datenpool zugreifen. Die Endpunkte **shall** Moodle-IDs akzeptieren und auf automatisch angelegte Nutzerprofile (GH-81) referenzieren, damit neu registrierte Personen ohne zusätzlichen Abgleich sichtbar werden.

## Akzeptanzkriterien

- [x] `GET /user/<user_id>/<lms_user_id>/student/<student_id>/learningCharacteristics` liefert ein JSON mit den Schlüsseln `learning_style`, `learning_strategy`, `learning_analytics`, `knowledge`.
- [x] Die Antwort bezieht sich ausschließlich auf den abgefragten Studierenden; Fremddaten werden ausgeschlossen.
- [x] Nicht vorhandene Studierende oder inkonsistente ID-Kombinationen führen zu HTTP 404 mit einer strukturierten Fehlermeldung (`{"error": "...", "message": "..."}`) ohne Seiteneffekte.
- [x] Die Implementierung folgt der im OAS von GH-30 definierten Struktur, damit Frontend-Komponenten die Daten ohne Mapping abrufen können.
- [x] Sobald ein Studierender durch GH-81 automatisch angelegt wird, stehen seine Lernprofil-Daten über denselben Endpunkt zur Verfügung.

## Rationale

Primary implementation: GitHub issue GH-30 ("Implement Basic Setup 2.0") definiert die REST-Endpunkte für Lernprofile und deren Antwortstruktur.
Related work: GH-81 stellt sicher, dass bei der ersten Anmeldung sämtliche Lerncharakteristika persistiert werden und somit abrufbar sind.
Derived from system requirement SyRS-FUNC-007 (Reports über Lernfortschritte).

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/30
- Related issue: https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Die Lernprofil-Daten werden sowohl für Lehrenden-Übersichten als auch für personalisierte Empfehlungen wiederverwendet.
- Fehlerhafte Aufrufe müssen geloggt werden, um Support- und Datenschutz-Anfragen nachvollziehen zu können.
