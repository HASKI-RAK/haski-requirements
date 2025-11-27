---
id: HASKI-REQ-0052
title: Wissensstände über REST abrufen
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
      name: "TestApi::test_get_students_knowledge"
---

## Beschreibung

Das System **shall** einen dedizierten REST-Endpunkt `GET /user/<user_id>/<lms_user_id>/student/<student_id>/knowledge` bereitstellen, der authentifizierten Rollen (Studierende, Lehrende) den aktuell persistierten Wissensstand eines Studierenden zurückliefert. Die Route **shall** dieselbe Moodle-ID-Mapping-Logik verwenden wie in GH-30 beschrieben und direkt auf die durch GH-81 automatisch angelegten `knowledge`-Datensätze zugreifen, sodass auch neu registrierte Studierende sofort abgefragt werden können. Die Antwort **shall** sämtliche gespeicherten Kompetenz- und Themenwerte des Studierenden serialisieren, damit Lernpfad-Berechnungen und Dashboards denselben Datenpool nutzen.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten den vollständigen Wissensstand-Datensatz des angefragten Studierenden (inklusive thematischer IDs und Bewertungswerte) in einer strukturierten JSON-Antwort.
- [x] Ungültige oder nicht berechtigte Kombinationen von `student_id` und `lms_user_id` führen zu HTTP 404 mit einer strukturierten Fehlermeldung (`{"error": "...", "message": "..."}`) und geben keine fremden Daten preis.
- [x] Die Route akzeptiert Moodle-IDs, folgt dem in GH-30 definierten OAS-Schema und kann unmittelbar nach automatischer Nutzeranlage durch GH-81 aufgerufen werden.
- [x] Die Schnittstelle verwendet dieselben Daten wie Lernpfad- und Analytics-Funktionen; Aktualisierungen (z. B. durch Fragebögen) sind ohne Zwischenschritte sichtbar.

## Rationale

SyRS-FUNC-007 fordert, dass Lernfortschritts-Reports auf aktuelle Wissensstände zugreifen können. GitHub issue GH-30 führte den OAS-konformen Endpoint für Lernprofil-Daten ein, während GH-81 sicherstellt, dass beim ersten Login zu jedem Studierenden ein `knowledge`-Datensatz angelegt wird. Der dedizierte Endpoint vermeidet, dass Client-Anwendungen den kombinierten `learningCharacteristics`-Payload parsen müssen, wenn nur Wissensstände benötigt werden.

## Hinweise

- Primary issues: https://github.com/HASKI-RAK/HASKI-Backend/issues/30, https://github.com/HASKI-RAK/HASKI-Backend/issues/81
- Die Route teilt sich Pfad und Autorisierung mit dem `DELETE`-Endpoint zum Zurücksetzen des Wissensstandes; Konsistenz der Antwortstrukturen ist sicherzustellen.
- Änderungen an der Datenstruktur sind im OAS zu dokumentieren, weil mehrere Frontends (Tutor-UI, Analytics) direkt auf diesen Endpoint zugreifen.
