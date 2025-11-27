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

Das System **shall** eine zentrale Abfragemöglichkeit bereitstellen, über die berechtigte Rollen den aktuellen Wissensstand eines Studierenden einsehen können. Die Schnittstelle muss alle gespeicherten Kompetenz- und Themenwerte konsistent liefern, unabhängig davon, ob die Daten automatisiert erzeugt oder durch Evaluationsinstrumente angepasst wurden.

## Akzeptanzkriterien

- [x] Die Antwort enthält sämtliche bekannten Wissensstandeinträge des angefragten Studierenden in strukturierter Form.
- [x] Nur legitimierte Rollen und eindeutige Studierendenbezüge erhalten Einsicht; alle anderen Anfragen werden ohne Datenrückgabe beendet.
- [x] Aktualisierte Werte stehen ohne Verzögerung für Lernpfadberechnungen, Dashboards und externe Auswertungen zur Verfügung.

## Rationale

SyRS-FUNC-007 verlangt einen einheitlichen Blick auf den Lernfortschritt. Eine abstrahierte Schnittstelle stellt sicher, dass alle Consumer – vom Lernraum bis zur Analytics-Pipeline – identische Wissensdaten erhalten, ohne unterschiedliche Datenquellen pflegen zu müssen.

## Hinweise

- Die OAS-Dokumentation beschreibt Format und Felder; Änderungen sind koordiniert mit allen Client-Teams abzustimmen.
- Die Rückgabe wird auch von Evaluationsberichten genutzt und sollte daher möglichst stabil versioniert werden.
