---
id: HASKI-REQ-0047
title: Nutzer Logbuffer API
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-014
links:
  parents: ["SyRS-FUNC-014"]
  stories:
    - "HASKI-RAK/HASKI-Backend#104"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_logbuffer"
---

## Beschreibung

Das Backend **shall** einen REST-Endpunkt `POST /user/<user_id>/logbuffer` bereitstellen, der authentifizierten Nutzenden erlaubt, frei formulierte Diagnoseeinträge (`content`) inklusive Zeitstempel (`date`) pro Nutzerkonto zu persistieren. Vor dem Speichern **shall** das System prüfen, dass die Parameter `user_id`, `content` und `date` vorhanden und syntaktisch valide sind. Erfolgreiche Anfragen **shall** mit HTTP `201 Created` beantwortet und mit der erzeugten `logbuffer`-Repräsentation (`id`, `user_id`, `content`, `date`) quittiert werden, damit Supportprozesse die Einträge unmittelbar nachverfolgen können.

## Akzeptanzkriterien

- [ ] `POST /user/<user_id>/logbuffer` legt bei gültiger Nutzlast einen Logbuffer-Datensatz mit den Feldern `id`, `user_id`, `content`, `date` an und liefert diese Werte in der Antwort.
- [ ] Fehlende Pflichtfelder oder leere Inhalte führen zu einer Fehlerantwort mit HTTP 400 und werden nicht gespeichert.
- [ ] Jede gespeicherte Nachricht ist der aufrufenden Nutzer-ID zugeordnet und kann später wieder abgerufen oder gelöscht werden.

## Rationale

Issue [GH-104](https://github.com/HASKI-RAK/HASKI-Backend/issues/104) beschreibt die Notwendigkeit, Logbuffer-Einträge serverseitig zu speichern, um Support-Informationen direkt aus dem Lernsystem zu gewinnen. Das Requirement operationalisiert SyRS-FUNC-014, indem es die konkreten Felder, Validierungen und Antwortformate für das Backend festlegt.

## Hinweise

- Persistenz erfolgt über die Tabelle `logbuffer` (siehe `backend/db_setup.py`).
- Service-Implementierung befindet sich in `backend/service_layer/services.py::create_logbuffer` und wird durch `backend/tests/e2e/test_api.py::TestApi::test_post_logbuffer` abgedeckt.
- Zugriffskontrollen re-using `services.get_user_by_id` stellen sicher, dass nur bekannte Nutzer schreiben können.
