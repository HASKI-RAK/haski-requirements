---
id: HASKI-REQ-0069
title: Nutzerstammdaten per LMS-ID abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-INT-003
links:
  parents: ["SyRS-INT-003"]
  stories: ["HASKI-RAK/HASKI-Backend#30", "HASKI-RAK/HASKI-Backend#81"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_user_by_id"
---

## Beschreibung

Das Backend **shall** einen abgesicherten GET-Endpunkt `GET /user/<user_id>/<lms_user_id>` bereitstellen, der die kanonischen Stammdaten eines HASKI-Nutzers anhand der Kombination aus lokaler User-ID und zugehöriger Moodle-ID zurückliefert. Die Antwort **shall** mindestens `id`, `name`, `university`, `role`, `lms_user_id` sowie den aktuellen `settings`-Block enthalten, damit Frontend- und Service-Komponenten dieselben Profilinformationen verwenden können. Fehlende oder nicht zueinander passende IDs **shall** eine deterministische Fehlermeldung (`{"error": "...", "message": "..."}`) erzeugen, ohne weitere Daten preiszugeben.

## Akzeptanzkriterien

- [x] Erfolgreiche Aufrufe liefern HTTP 200 und geben exakt den in GH-30 beschriebenen Payload (inkl. `settings`) für den adressierten Nutzer zurück.
- [x] Ungültige oder nicht verknüpfte Kombinationen aus `user_id` und `lms_user_id` resultieren in HTTP 404 mit der beschriebenen Fehlstruktur, ohne interne Details zu offenbaren.
- [x] Der Endpunkt akzeptiert ausschließlich authentifizierte Nutzer (z. B. aus einer bestehenden Session) und stellt sicher, dass nur berechtigte Rollen eigene oder delegierte Profile lesen können.
- [x] Alle gelieferten Attribute spiegeln die von GH-81 initialisierten Stammdaten wider; Änderungen an Einstellungen werden unmittelbar reflektiert.
- [x] Antwortschema bleibt OAS-konform, sodass Frontend-Komponenten keine zusätzlichen Mappings implementieren müssen.

## Rationale

GitHub Issue [#30](https://github.com/HASKI-RAK/HASKI-Backend/issues/30) definiert im Basic-Setup-OAS sämtliche Nutzerendpunkte. Damit die Moodle-LTI-Integration (SyRS-INT-003) konsistent auf Nutzerprofile zugreifen kann, benötigt HASKI einen deterministischen Lookup über die gekoppelte LMS-ID. Issue [#81](https://github.com/HASKI-RAK/HASKI-Backend/issues/81) stellt sicher, dass bei der ersten Anmeldung vollständige Stammdaten und Settings vorliegen, die dieser Endpunkt unmittelbar zurückliefert.

## Hinweise

- Die Antwort enthält bewusst keine sensiblen Felder wie Passwörter oder interne Role-IDs; diese werden serverseitig gefiltert.
- Validierungsfehler sollen klar zwischen „MissingUser" und allgemeinen Autorisierungsproblemen unterscheiden, damit Supportfälle schneller eingegrenzt werden können.
- E2E-Verifikation: `backend/tests/e2e/test_api.py::TestApi::test_get_user_by_id`.
