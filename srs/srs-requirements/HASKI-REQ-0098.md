---
id: HASKI-REQ-0098
title: Bereitstellung von Projektinformationen (About Us)
type: Functional
status: Implemented
stakeholder_priority: Low
verification_method: Test
source_id: SyRS-INT-001
links:
  stories: ["HASKI-RAK/HASKI-Frontend#256"]
  parents: ["SyRS-INT-001"]
  tests:
    - path: "frontend/src/pages/AboutUs/AboutUs.test.tsx"
      name: "AboutUs"
---

## Beschreibung

Das System **shall** eine "Über uns" (About Us) Seite bereitstellen, die Informationen über das HASKI-Projekt, die beteiligten Hochschulen und das Entwicklungsteam darstellt.

## Akzeptanzkriterien

- [x] Die Seite zeigt Informationen zum Projektziel und Hintergrund.
- [x] Die Seite listet die beteiligten Teammitglieder auf.
- [x] Die Seite ist über die Navigation (z.B. Footer) erreichbar.
- [x] Das Layout ist responsiv und entspricht dem Corporate Design.

## Rationale

Transparenz über das Projekt und die Beteiligten schafft Vertrauen bei den Nutzern und erfüllt Informationspflichten.

## Hinweise

- Issue #256: Refactor "About us" Page.
