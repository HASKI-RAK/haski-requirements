---
id: HASKI-REQ-0045
title: Frontend Web-Vitals Logging Endpoint
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-012
links:
  parents: ["SyRS-FUNC-012"]
  stories:
    - "HASKI-RAK/HASKI-Backend#15"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_api_post_frontend_logs"
---

## Beschreibung

Das Backend **shall** einen REST-Endpunkt `POST /logs/frontend` bereitstellen, an den das React-Frontend konsolidierte Google-Web-Vitals-Messwerte (z. B. FCP, CLS, LCP, INP) sendet. Jedes Log-Event **shall** die Felder `name`, `value`, `rating`, `delta`, `entries`, `id` und `navigationType` enthalten und wird serverseitig validiert. Ungültige Metriknamen, Ratings außerhalb der Spezifikation oder fehlende Pflichtfelder **shall** deterministisch mit HTTP 400 beantwortet werden, ohne Daten zu speichern. Erfolgreiche Aufrufe **shall** den eingereichten Datensatz inkl. Status `201 Created` zurückliefern und ihn für nachgelagerte Administrations-APIs (z. B. `/user/<user_id>/<lms_user_id>/admin/<admin_id>/logs`) verfügbar machen.

## Akzeptanzkriterien

- [ ] Der Endpunkt `POST /logs/frontend` akzeptiert nur die erlaubten Web-Vitals-Namen (`FCP`, `TTFB`, `CLS`, `LCP`, `FID`, `INP`).
- [ ] `rating` darf ausschließlich `good`, `needs-improvement` oder `poor` annehmen.
- [ ] `navigationType` wird gegen `navigate`, `reload`, `back-forward`, `back-forward-cache`, `prerender` validiert.
- [ ] Fehlende Pflichtfelder führen zu einer `MissingParameterError`-Antwort mit HTTP 400.
- [ ] Valide Nutzlasten werden mit HTTP 201 und dem gespeicherten Datensatz quittiert.
- [ ] Admin-Endpunkte können die persistierten Logs gebündelt abrufen.

## Rationale

Issue [GH-15](https://github.com/HASKI-RAK/HASKI-Backend/issues/15) fordert eine serverseitige Sammelstelle für Frontend-Telemetriedaten, um Performance-Regressionen analysieren zu können. Die Anforderung operationalisiert SyRS-FUNC-012, indem sie den konkreten API-Vertrag, Validierungsregeln und Error-Handling im Backend festlegt.

## Hinweise

- Telemetriedaten orientieren sich an [Chrome Web Vitals](https://web.dev/vitals/) und werden zunächst in-memory (`mocked_frontend_log`) verwaltet, bis Persistierungskonzepte folgen.
- `backend/tests/e2e/test_api.py::TestApi::test_api_post_frontend_logs` verifiziert erfolgreiche und fehlerhafte Payloads.
- Der OpenAPI-Eintrag befindet sich in `backend/entrypoints/HASKI-OAS.yaml`.
