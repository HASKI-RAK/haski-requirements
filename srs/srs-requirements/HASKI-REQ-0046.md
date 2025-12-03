---
id: HASKI-REQ-0046
title: Newsverwaltung und Newsbanner-Schnittstelle
type: Functional
status: Implemented
stakeholder_priority: Medium
verification_method: Test
source_id: SyRS-FUNC-013
links:
  parents: ["SyRS-FUNC-013"]
  stories:
    - "HASKI-RAK/HASKI-Backend#92"
    - "HASKI-RAK/HASKI-Backend#111"
  tests:
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_post_news"
    - path: "backend/tests/e2e/test_api.py"
      name: "TestApi::test_get_news"
    - path: "HASKI-Frontend/src/components/Newsbanner/Newsbanner.test.tsx"
      name: "Newsbanner tests"
    - path: "HASKI-Frontend/src/services/News/fetchNews.test.tsx"
      name: "Test the fetchNews functionalities"
---

## Beschreibung

Das Backend **shall** News-Einträge über den REST-Endpunkt `POST /news` persistent speichern, damit das Frontend-Newsbanner kuratierte Inhalte pro Hochschule und Sprache darstellen kann. Jeder Datensatz **shall** mindestens die Felder `university`, `language_id`, `created_at`, `news_content` und `expiration_date` enthalten. Ungültige oder unvollständige Nutzlasten **shall** abgelehnt werden. Erfolgreich angelegte News **shall** mit HTTP `201 Created` beantwortet werden und direkt über `GET /news` für das Frontend abrufbar sein.

## Akzeptanzkriterien

- [ ] `POST /news` persistiert valide News mit den oben genannten Pflichtfeldern.
- [ ] `GET /news` liefert nur nicht abgelaufene News und kann nach Universität/ Sprache gefiltert werden.
- [ ] Fehlende Pflichtfelder führen zu einer Fehlerantwort mit `{"error": ..., "message": ...}` und HTTP 400.
- [ ] Datenbankeinträge enthalten Zeitstempel `created_at` und `expiration_date`, um Auto-Ausblendungen zu ermöglichen.
- [ ] Admin- oder Service-Rollen können News aktualisieren oder löschen, ohne historische Daten zu beschädigen.
- [ ] Newsbanner-Komponenten können mehrere Meldungen geordnet abrufen (siehe Frontend-Komponente `Newsbanner`).

## Rationale

Issue [GH-92](https://github.com/HASKI-RAK/HASKI-Backend/issues/92) beschreibt das Feature, News im Backend zu speichern und an das Frontend auszuliefern. Issue [GH-111](https://github.com/HASKI-RAK/HASKI-Backend/issues/111) stellt sicher, dass Universitätszuordnungen konsistent umgesetzt werden, damit Newsbanner nur für passende Hochschulen erscheinen.

## Hinweise

- Datenmodell: Tabelle `news` mit Feldern `id`, `university`, `language_id`, `created_at`, `expiration_date`, `news_content`.
- Validierung und Serialisierung liegen in `service_layer.services` und werden durch `backend/tests/e2e/test_api.py::TestApi::test_post_news` sowie `::test_get_news` verifiziert.
- Frontend konsumiert `GET /news` asynchron; Skeleton- und Fehlerzustände sind in GH-92 dokumentiert.
