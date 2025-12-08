---
id: HASKI-REQ-0100
title: Bereitstellung eines Impressums
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-INT-001
links:
  stories: ["HASKI-RAK/HASKI-Frontend#127"]
  parents: ["SyRS-INT-001"]
  tests:
    - path: "frontend/src/pages/Imprint/Imprint.test.tsx"
      name: "Imprint Component"
---

## Beschreibung

Das System **shall** ein Impressum bereitstellen, das die gesetzlich vorgeschriebenen Informationen (Anbieterkennzeichnung, Kontakt, Haftungsausschluss) enthält.

## Akzeptanzkriterien

- [x] Die Seite zeigt die Adresse der Hochschule.
- [x] Die Seite zeigt Kontaktinformationen (E-Mail, Telefon).
- [x] Die Seite enthält einen Haftungsausschluss (Disclaimer).
- [x] Die Seite nennt den Vertretungsberechtigten.
- [x] Die Seite ist über den Footer erreichbar.

## Rationale

Erfüllung gesetzlicher Informationspflichten (TMG).

## Hinweise

- Issue #127: Create Imprint page.
