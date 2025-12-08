---
id: HASKI-REQ-0089
title: Globale Navigationsmenüs, Footer und Impressum
type: Interface
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-019
links:
  parents: ["SyRS-FUNC-019", "SyRS-INT-001"]
  stories: ["HASKI-RAK/HASKI-Frontend#124", "HASKI-RAK/HASKI-Frontend#127"]
  tests:
    - path: "HASKI-Frontend/src/components/GlobalNav/CourseMenu/CourseMenu.test.tsx"
      name: "CourseMenu tests"
    - path: "HASKI-Frontend/src/components/GlobalNav/FurtherInfoMenu/FurtherInfoMenu.test.tsx"
      name: "FurtherInfoMenu tests"
    - path: "HASKI-Frontend/src/components/GlobalNav/GlobalNavMenu/GlobalNavMenu.test.tsx"
      name: "GlobalNavMenu tests"
    - path: "HASKI-Frontend/src/components/GlobalNav/StatisticsMenu/StatisticsMenu.test.tsx"
      name: "StatisticsMenu tests"
    - path: "HASKI-Frontend/src/components/LocalNav/LocalNavBar/LocalNavBar.test.tsx"
      name: "LocalNavBar tests"
    - path: "HASKI-Frontend/src/components/LocalNav/LocalNavItem/LocalNavItem.test.tsx"
      name: "LocalNavItem tests"
    - path: "HASKI-Frontend/src/components/Footer/Footer.test.tsx"
      name: "Footer"
    - path: "HASKI-Frontend/src/pages/MainFrame/MainFrame.test.tsx"
      name: "MainFrame tests"
    - path: "frontend/src/pages/Imprint/Imprint.test.tsx"
      name: "Imprint Component"
---

## Beschreibung

Das Frontend **shall** im MainFrame-Layout persistente Navigationsmenüs bereitstellen, die kontextabhängig Kurs-, Statistik- und Servicefunktionen zugänglich machen. Die globale Navigation **shall** in einem einheitlichen Menüsystem Zugang zu Kursen (`CourseMenu`), Statistiken (`StatisticsMenu`) und weiterführenden Informationen (`FurtherInfoMenu`) bieten, während die lokale Navigation (`LocalNavBar`, `LocalNavItem`) kontextspezifische Untermenüs für Topic- und Aktivitätsnavigation bereitstellt. Der Footer **shall** Links zu Impressum, Datenschutz und Projektinformationen enthalten und in allen Ansichten verfügbar sein.

## Akzeptanzkriterien

### Globale Navigationsmenüs

- [x] `CourseMenu` rendert die Liste verfügbarer Kurse und ermöglicht Navigation zu Kursseiten, wenn der Benutzer authentifiziert ist (verifiziert durch "CourseMenu tests").
- [x] `StatisticsMenu` zeigt verfügbare Statistikansichten (Ratings, Learning Analytics) und navigiert zur entsprechenden Dashboard-Seite.
- [x] `FurtherInfoMenu` bietet Zugang zu Über-uns-Seite, Glossar und weiteren Servicefunktionen.
- [x] `GlobalNavMenu` rendert generische Menüstrukturen mit konfigurierbaren Inhalten, unterstützt Ladeanimationen und disabled-States für nicht verfügbare Optionen (verifiziert durch "GlobalNavMenu tests").

### Lokale Navigation

- [x] `LocalNavBar` rendert eine horizontale Navigationsleiste für Topic- oder seitenspezifische Optionen (verifiziert durch "LocalNavBar tests").
- [x] `LocalNavItem` stellt einzelne anklickbare Navigationselemente mit Icons und Labels bereit (verifiziert durch "LocalNavItem tests").

### Footer

- [x] `Footer` rendert persistent am unteren Seitenrand und enthält Links zu Impressum, Datenschutz und Projektinformationen (verifiziert durch "Footer").
- [x] Alle Footer-Links navigieren korrekt zu den entsprechenden Seiten ohne Fehler.

### Impressum

- [x] Die Impressum-Seite zeigt die Adresse der Hochschule.
- [x] Die Seite zeigt Kontaktinformationen (E-Mail, Telefon).
- [x] Die Seite enthält einen Haftungsausschluss (Disclaimer).
- [x] Die Seite nennt den Vertretungsberechtigten.
- [x] Die Seite ist über den Footer erreichbar.

### Integration und Konsistenz

- [x] Alle Navigationskomponenten arbeiten mit React Router und nutzen `useNavigate` für Seitenübergänge.
- [x] Menüs respektieren Authentifizierungszustände und zeigen nur verfügbare Optionen an.
- [x] Die Komponenten rendern fehlerfrei innerhalb des `MemoryRouter`-Kontexts für Testzwecke.

## Rationale

Issue [#124](https://github.com/HASKI-RAK/HASKI-Frontend/issues/124) führte das MainFrame-Layout ein, das eine konsistente Navigationsstruktur über alle Seiten hinweg erfordert. Die globalen Navigationsmenüs ermöglichen schnellen Zugriff auf Hauptfunktionen, während die lokale Navigation kontextspezifische Aktionen bereitstellt. Der Footer erfüllt rechtliche Anforderungen und unterstützt die Projektkommunikation. Issue [#127](https://github.com/HASKI-RAK/HASKI-Frontend/issues/127) implementiert das Impressum zur Erfüllung gesetzlicher Informationspflichten (TMG).

## Hinweise

- Die Navigationskomponenten sind Teil des MainFrame-Layouts und werden global geladen; Performance-Optimierungen sollten Lazy Loading für Menüinhalte berücksichtigen.
- Änderungen an der Navigationsstruktur müssen mit der i18n-Lokalisierung abgestimmt werden.
- Die Menüs nutzen Material-UI-Komponenten und folgen dem Theme-System für konsistentes Styling.
