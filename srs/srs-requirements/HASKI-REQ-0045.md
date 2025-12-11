---
id: HASKI-REQ-0045
title: Frontend Web-Vitals Logging Endpoint
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-012
merged_from: ["HASKI-REQ-0065"]
links:
  parents: ["SyRS-FUNC-012"]
  stories:
    - "HASKI-RAK/HASKI-Backend#15"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_post_frontend_logs"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_logs_by_admin_id"
---

## Beschreibung

Das Backend **shall** einen REST-Endpunkt `POST /logs/frontend` bereitstellen, an den das React-Frontend konsolidierte Google-Web-Vitals-Messwerte (z. B. FCP, CLS, LCP, INP) sendet. Jedes Log-Event **shall** die Felder `name`, `value`, `rating`, `delta`, `entries`, `id` und `navigationType` enthalten und wird serverseitig validiert. Ungültige Metriknamen, Ratings außerhalb der Spezifikation oder fehlende Pflichtfelder **shall** deterministisch mit HTTP 400 beantwortet werden, ohne Daten zu speichern. Erfolgreiche Aufrufe **shall** den eingereichten Datensatz inkl. Status `201 Created` zurückliefern und ihn für nachgelagerte Administrations-APIs (z. B. `/user/<user_id>/<lms_user_id>/admin/<admin_id>/logs`) verfügbar machen.

Ergänzend **shall** das Backend einen GET-Endpunkt `GET /user/<user_id>/<lms_user_id>/admin/<admin_id>/logs` für verifizierte Admin-Rollen bereitstellen, über den die zuvor erfassten Frontend-Web-Vitals gesammelt abgerufen werden können. Der Endpunkt **shall** die Kombination aus `user_id`, `lms_user_id` und `admin_id` validieren, bevor er Telemetriedaten liefert, und ausschließlich die strukturierte Logsammlung (`logs`) zurückgeben.

## Akzeptanzkriterien

- [ ] Der Endpunkt `POST /logs/frontend` akzeptiert nur die erlaubten Web-Vitals-Namen (`FCP`, `TTFB`, `CLS`, `LCP`, `FID`, `INP`).
- [ ] `rating` darf ausschließlich `good`, `needs-improvement` oder `poor` annehmen.
- [ ] `navigationType` wird gegen `navigate`, `reload`, `back-forward`, `back-forward-cache`, `prerender` validiert.
- [ ] Fehlende Pflichtfelder führen zu einer `MissingParameterError`-Antwort mit HTTP 400.
- [ ] Valide Nutzlasten werden mit HTTP 201 und dem gespeicherten Datensatz quittiert.
- [ ] Admin-Endpunkte können die persistierten Logs gebündelt abrufen.

### Administrations-API für Frontend-Logs

- [x] Erfolgreiche Aufrufe von `GET /user/<user_id>/<lms_user_id>/admin/<admin_id>/logs` liefern HTTP 200 und enthalten den Schlüssel `logs` mit allen aktuell gespeicherten Web-Vitals-Einträgen.
- [x] Unbekannte oder nicht autorisierte Admin-Identitäten führen zu HTTP 404 mit `{"error", "message"}`.
- [x] Die Antwort entfernt sensible Nutzerinformationen und gibt nur die protokollierten Metriken zurück.
- [x] Der Endpunkt ruft vor der Aggregation immer `get_user_by_id` auf und bricht bei Validierungsfehlern ohne Logausgabe ab.

## Rationale

Issue [GH-15](https://github.com/HASKI-RAK/HASKI-Backend/issues/15) fordert eine serverseitige Sammelstelle für Frontend-Telemetriedaten, um Performance-Regressionen analysieren zu können. Die Anforderung operationalisiert SyRS-FUNC-012, indem sie den konkreten API-Vertrag, Validierungsregeln und Error-Handling im Backend festlegt.

## Hinweise

- Telemetriedaten orientieren sich an [Chrome Web Vitals](https://web.dev/vitals/) und werden zunächst in-memory (`mocked_frontend_log`) verwaltet, bis Persistierungskonzepte folgen.
- `backend/tests/e2e/test_api.py::TestApi::test_api_post_frontend_logs` verifiziert erfolgreiche und fehlerhafte Payloads.
- Der OpenAPI-Eintrag befindet sich in `backend/entrypoints/HASKI-OAS.yaml`.
