---
id: HASKI-REQ-0064
title: Administrations-Nutzerverzeichnis abrufen
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-015
links:
  stories: ["HASKI-RAK/HASKI-Backend#30"]
  parents: ["SyRS-FUNC-015"]
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_users_by_admin_id"
---

## Beschreibung

Das Backend **shall** einen abgesicherten GET-Endpunkt `GET /user/<user_id>/<lms_user_id>/admin/<admin_id>/user` bereitstellen, der registrierte Admin-Nutzer:innen eindeutig gegen Moodle- und HASKI-IDs verifiziert und anschließend das mandantenbezogene Nutzerverzeichnis der jeweiligen Hochschule liefert. Jeder ausgegebene Eintrag **shall** nur die notwendigen Stammdaten (z. B. Name, Rolle, Hochschule) enthalten, sensible Felder wie Passwörter, Settings oder Rollen-IDs werden entfernt. Fehlende oder inkonsistente Admin-IDs **shall** deterministisch zu aussagekräftigen Fehlermeldungen führen, damit Betriebsteams Audits und Supportfälle ohne Datenexporte bearbeiten können.

## Akzeptanzkriterien

- [x] Ein bekannter Admin erhält HTTP 200 und ein JSON-Objekt mit dem Key `users`, das ausschließlich Mitglieder der eigenen Hochschule enthält.
- [x] Jedes Nutzerelement enthält mindestens `name`, `role` und `university`; vertrauliche Felder (z. B. `settings`, `role_id`) werden nicht ausgeliefert.
- [x] Unbekannte oder nicht autorisierte Admin-IDs führen zu einer MissingUser-Fehlermeldung mit passender HTTP-Fehlernummer (404) und generischer Fehlerantwort (`error`, `message`).
- [x] Die Endpoint-Implementierung überprüft die Admin-Identität stets bevor Daten aggregiert werden und gibt bei Validierungsfehlern keine Benutzerliste zurück.

## Rationale

Primary implementation: GitHub issue GH-30 "Implement Basic Setup 2.0" for die in OAS definierte Admin-Schnittstelle. Die Anforderung leitet sich aus SyRS-FUNC-015 und StRS-137 ab, um den Betriebsteams mandantenfähige Verzeichnisabfragen zu ermöglichen.

## Hinweise

- Ausgabeformat ist kompatibel mit Operations-Tools, die die JSON-Liste direkt auswerten können.
- Fehlercodes und Meldungen folgen dem bestehenden Fehler-Framework (`MissingUserError`).
- Erweiterungen wie Filter nach Rollen oder Status können auf derselben Struktur aufbauen, solange die oben genannten Garantien bestehen bleiben.
