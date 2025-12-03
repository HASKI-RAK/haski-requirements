---
id: HASKI-REQ-0088
title: Navigation für Frontend-Routen
type: Interface
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-019
links:
  parents: ["SyRS-FUNC-019"]
  stories: ["HASKI-RAK/HASKI-Frontend#124"]
  tests:
    - path: "frontend/src/components/BreadcrumbsContainer/BreadcrumbsContainer.test.tsx"
      name: "BreadcrumbsContainer tests"
---

## Beschreibung

Das Frontend **shall** im `BreadcrumbsContainer` oberhalb des Seiteninhalts den aktuellen Routing-Pfad ausgeben, sodass Nutzende jederzeit ihren Kontext erkennen und zu übergeordneten Ansichten zurückspringen können. Für jede Pfadstufe **shall** ein lokalisierter Text angezeigt werden, der auf den entsprechenden Zwischenpfad zurücknavigiert. Numerische Segmente (z. B. Kurs- oder Topic-IDs) **shall** unterdrückt bzw. durch den vorangegangenen Textknoten ersetzt werden, damit die Navigation semantisch bleibt. Der erste Eintrag **shall** stets einen Link zur Startseite (`/`) darstellen.

## Akzeptanzkriterien

- [x] Beim Root-Pfad `/` wird ausschließlich ein „Home“-Eintrag angezeigt, dessen Klick den Router auf `/` navigiert (verifiziert durch „BreadcrumbsContainer tests“).
- [x] Mehrstufige Pfade erzeugen für jeden Textknoten eine anklickbare Breadcrumb-Stufe, die beim Klicken den korrekten Zwischennavigationspfad aufruft.
- [x] Pfadsegmente, die vollständig numerisch sind, tauchen in der Anzeige nicht auf; stattdessen bleibt die zuvor benannte Stufe sichtbar.
- [x] Der `BreadcrumbsContainer` arbeitet innerhalb eines React-Routers (MemoryRouter) ohne Fehler und respektiert i18n-Schlüssel aus `pages.*`.

## Rationale

Issue [#124](https://github.com/HASKI-RAK/HASKI-Frontend/issues/124) führte das MainFrame-Layout ein, das eine persistente Breadcrumb-Navigation benötigt, um Nutzenden den Kontextwechsel zwischen Kurs-, Topic- und Service-Seiten zu erleichtern. Die Automatisierung der Pfadgenerierung verhindert divergierende Breadcrumb-Darstellungen und reduziert Navigationsfehler.

## Hinweise

- Die Komponente nutzt `useNavigate` / `useLocation` aus `react-router-dom`; Änderungen an der Routing-Struktur müssen die Breadcrumb-Generierung berücksichtigen.
- Bei neuen Seiten ist sicherzustellen, dass ein entsprechender Übersetzungsschlüssel unter `pages.*` vorhanden ist, damit die Breadcrumbs lokalisiert bleiben.
