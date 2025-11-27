---
id: HASKI-REQ-0060
title: Studentische Lernpfad-Algorithmen abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-002
links:
  stories: ["HASKI-RAK/HASKI-Backend#83"]
  parents: ["SyRS-FUNC-002"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_learning_path_algorithm_student"
---

## Beschreibung

Das System **shall** über `GET /user/<user_id>/<lms_user_id>/topic/<topic_id>/studentAlgorithm` den aktuell für ein Topic gespeicherten Lernpfad-Algorithmus eines Studierenden zurückliefern. Die Antwort **shall** mindestens `short_name`, `algorithm_id` und `topic_id` enthalten, damit Frontend-Komponenten unmittelbar erkennen, ob eine individuelle Auswahl oder ein Tutor-Override aktiv ist. Die Route **shall** dieselbe Moodle-ID-Mapping- und Rollenlogik wie die POST-Endpunkte aus HASKI-REQ-0041 verwenden und ausschließlich Datensätze zurückgeben, die zur angefragten Einschreibung gehören.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 mit `short_name`, `algorithm_id` und `topic_id` des aktuell persistierten studentischen Algorithmus.
- [x] Ungültige Studierenden-, Topic- oder LMS-IDs führen zu HTTP 404 mit strukturierter Fehlermeldung (`{"error": "...", "message": "..."}`).
- [x] Fehlende oder unberechtigte Rollen resultieren in HTTP 401/403 ohne Daten offenzulegen.
- [x] Die ausgegebene Algorithmus-ID entspricht dem zentralen Katalog (HASKI-REQ-0040) und reflektiert Tutor-Overrides (HASKI-REQ-0026) sowie studentische Änderungen (HASKI-REQ-0041).

## Rationale

GitHub Issue [#83](https://github.com/HASKI-RAK/HASKI-Backend/issues/83) beschreibt, dass Studierende ihren bevorzugten Lernpfad-Algorithmus konfigurieren können und dass Tutor:innen Overrides setzen dürfen. Damit Benutzeroberflächen und Automationen diese Informationen anzeigen und synchron halten können, ist ein dedizierter Read-Endpoint nötig, der den aktuell wirksamen Algorithmus je Topic zurückliefert. So lassen sich Konflikte zwischen Tutor-Defaults und studentischen Präferenzen transparent darstellen.

## Hinweise

- Antwortschema wird von Frontend-Services `fetchStudentLpLeAlg` (bzw. `AlgorithmSettingsModal`) genutzt.
- Die Implementierung sollte serverseitig cachen oder denselben View wie die POST-Persistierung nutzen, damit unmittelbare Konsistenz gewährleistet ist.
- Die Route eignet sich als Datenquelle für Auditing/Traceability, da jede Anpassung sofort sichtbar wird.
