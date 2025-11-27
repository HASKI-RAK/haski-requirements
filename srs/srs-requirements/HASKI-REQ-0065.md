---
id: HASKI-REQ-0065
title: Administrations-API für Frontend-Logs
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-012
links:
  stories: ["HASKI-RAK/HASKI-Backend#15"]
  parents: ["SyRS-FUNC-012"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_logs_by_admin_id"
---

## Beschreibung

Das Backend **shall** einen GET-Endpunkt `GET /user/<user_id>/<lms_user_id>/admin/<admin_id>/logs` für verifizierte Admin-Rollen bereitstellen, über den die zuvor erfassten Frontend-Web-Vitals gesammelt abgerufen werden können. Der Endpunkt **shall** die Kombination aus `user_id`, `lms_user_id` und `admin_id` validieren, bevor er Telemetriedaten liefert, und ausschließlich die strukturierte Logsammlung (`logs`) zurückgeben. Fehlerhafte oder nicht autorisierte Anfragen **shall** deterministisch mit einer passenden Fehlermeldung (z. B. `MissingUser`) beantwortet werden, ohne Logdaten offenzulegen.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und enthalten den Schlüssel `logs` mit allen aktuell gespeicherten Web-Vitals-Einträgen.
- [x] Unbekannte oder nicht autorisierte Admin-Identitäten führen zu HTTP 404 mit `{"error", "message"}`.
- [x] Die Antwort entfernt sensible Nutzerinformationen und gibt nur die protokollierten Metriken zurück.
- [x] Der Endpunkt ruft vor der Aggregation immer `get_user_by_id` auf und bricht bei Validierungsfehlern ohne Logausgabe ab.

## Rationale

Primary implementation: GitHub issue GH-15 "API Endpoint for Frontend Logs" stellte die Grundlage für die Web-Vitals-Telemetrie bereit. Diese Anforderung ergänzt den bestehenden POST-Endpunkt (HASKI-REQ-0045) um das notwendige Administrations-Interface, damit Betriebsteams die gespeicherten Logs einsehen können und SyRS-FUNC-012 vollständig erfüllt wird.

## Hinweise

- Die Logdaten werden derzeit aus `mocked_frontend_log` geliefert; spätere Persistenzänderungen dürfen das API-Schema nicht brechen.
- Authentifizierung und Autorisierung folgen denselben Patterns wie andere Admin-Endpunkte (`get_users_by_admin`).
- Die Ausgabe kann direkt in Monitoring- oder Incident-Response-Workflows eingespeist werden.
