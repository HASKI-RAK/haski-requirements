---
id: HASKI-REQ-0040
title: Zentrale Verwaltung des Lernpfad-Algorithmus-Katalogs
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-008
links:
  parents: ["SyRS-FUNC-008"]
  stories: ["HASKI-RAK/HASKI-Backend#83"]
  tests:
    [
      "backend/tests/e2e/test_api.py::TestApi::test_post_learning_path_algorithm",
    ]
---

## Beschreibung

Das System **shall** einen kanonischen Katalog der verfügbaren Lernpfad-Algorithmen bereitstellen, der über abgesicherte Backend-Endpunkte verwaltet wird. Administrator:innen und Tutor:innen **shall** neue Algorithmen mit einem eindeutigen `short_name` und einer sprechenden Bezeichnung registrieren können, damit Studierende und Lehrende dieselbe Referenz verwenden, wenn sie Lernpfade konfigurieren oder einen Algorithmus selektieren. Persistierte Algorithmen **shall** sofort für nachgelagerte Endpunkte (z.B. Auswahl eines Standard- oder individuellen Lernpfads) zur Verfügung stehen.

## Akzeptanzkriterien

- [ ] Ein REST-Endpunkt `POST /algorithm` akzeptiert die Pflichtfelder `short_name` (URI-tauglicher Schlüssel) und `full_name` (Anzeigename) und liefert bei Erfolg HTTP 201 mit den persistierten Werten sowie einer internen ID zurück.
- [ ] Fehlende oder falsch typisierte Pflichtfelder führen zu einer Validierungsantwort (HTTP 400) mit erzwingender Fehlermeldung; keine inkonsistenten Datensätze werden gespeichert.
- [ ] Der `short_name` ist systemweit eindeutig; doppelte Einträge werden mit HTTP 409/400 abgelehnt, ohne bestehende Algorithmen zu überschreiben.
- [ ] Neu erfasste Algorithmen sind unmittelbar in den Auswahl- und Konfigurations-Endpunkten für Lernpfade verfügbar (z.B. `POST /student/<id>/topic/<id>/algorithm`).
- [ ] Der Endpunkt ist mit der bestehenden Rollen-/Rechteprüfung geschützt, sodass nur autorisierte Rollen (Kursersteller:innen, Tutor:innen, Admins) den Katalog verändern können.
- [ ] Alle erfolgreichen und fehlgeschlagenen Katalogänderungen werden serverseitig protokolliert, damit Konfigurationsfehler nachvollziehbar bleiben.

## Rationale

GitHub Issue [#83](https://github.com/HASKI-RAK/HASKI-Backend/issues/83) verlangt, dass Studierende einen Lernpfad-Algorithmus aus einer definierten Liste wählen können und Tutor:innen Standardalgorithmen für Topics vorgeben dürfen. Ein konsistenter Algorithmus-Katalog mit eindeutigen Kurzbezeichnern stellt sicher, dass alle Auswahl- und Berechnungsendpunkte dieselben Referenzen verwenden. Die Funktionalität wird durch den End-to-End-Test `backend/tests/e2e/test_api.py::TestApi::test_post_learning_path_algorithm` verifiziert, der die erfolgreiche Registrierung eines neuen Algorithmus prüft.

## Hinweise

- Beispiel-Payload: `{ "short_name": "aco", "full_name": "Ant Colony Optimization" }`. Die Antwort enthält `id`, `short_name` und `full_name`.
- Die Persistenz erfolgt in der Tabelle `learning_path_algorithm` (oder äquivalent) und dient als Foreign-Key-Ziel für studentische und tutorielle Auswahlrelationen.
- Beim Deployment sollen Default-Einträge (z.B. "aco", "graf", "ga") per Seed-Daten verfügbar sein; der Endpunkt ergänzt diese Liste um neue Verfahren.
- Bei Erweiterungen ist sicherzustellen, dass API-Schemata der Frontends (z.B. AlgorithmSettingsModal) unverändert konsumierbar bleiben.
