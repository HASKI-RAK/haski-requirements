---
id: HASKI-REQ-0090
title: React SPA-Architektur mit Provider-Hierarchie und Routing
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
source_id: SyRS-FUNC-001
links:
  stories: []
  parents: ["SyRS-FUNC-001"]
  tests:
    - path: "frontend/src/pages/App/App.test.tsx"
      name: "App tests"
    - path: "frontend/src/pages/PageNotFound/PageNotFound.test.tsx"
      name: "PageNotFound"
    - path: "frontend/src/services/BufferContent/postBufferContent.test.tsx"
      name: "postBufferContent has expected behaviour"
    - path: "frontend/src/services/RoleContext/RoleContext.test.tsx"
      name: "Test Rolecontext"
    - path: "frontend/src/services/SnackbarContext/SnackbarContext.test.tsx"
      name: "Test SnackbarContext"
    - path: "frontend/src/services/SnackbarProvider/SnackbarProvider.test.tsx"
      name: "Test SnackbarProvider"
    - path: "frontend/src/services/ThemeContext/ThemeContext.test.tsx"
      name: "ThemeContext"
    - path: "frontend/src/services/ThemeProvider/ThemeProvider.test.tsx"
      name: "ThemeProvider"
    - path: "frontend/src/services/Viewport/Viewport.test.tsx"
      name: "Viewport hook tests"
    - path: "frontend/src/shared/internationalization.test.tsx"
      name: "i18n test"
    - path: "frontend/src/shared/logBuffer.config.test.tsx"
      name: "Test the demo component"
    - path: "frontend/src/shared/RingBuffer.test.tsx"
      name: "Test the RingBuffer class"
    - path: "frontend/src/store/Slices/RemoteTopicSlice.test.tsx"
      name: "RemoteTopicSlice "
    - path: "HASKI-Frontend/src/shared/config.test.ts"
      name: "setConfig"
    - path: "HASKI-Frontend/src/services/RequestResponse.test.ts"
      name: "RequestResponse"
  merged_from: ["HASKI-REQ-0099"]
---

## Beschreibung

Das Frontend **shall** als Single-Page Application (SPA) auf Basis von React und React Router implementiert werden, wobei die zentrale `App`-Komponente als Einstiegspunkt nach dem Laden der Umgebungskonfiguration fungiert. Die `App`-Komponente **shall** eine geschachtelte Provider-Hierarchie aufbauen, die Theme-Kontext, React Flow-Kontext, Snackbar-Kontext, Routing-Kontext, Authentifizierungs-Kontext, Rollen-Kontext und xAPI-Kontext in konsistenter Reihenfolge bereitstellt, sodass alle untergeordneten Seiten und Komponenten über `useContext` auf diese Dienste zugreifen können.

Das Routing **shall** alle funktionalen Seiten (Home, Course, Topic, Login, Imprint, PrivacyPolicy, AboutUs, Glossary, ProjectDescription, LearnerCharacteristics, Contact, Rating) sowie eine Wildcard-Route (`path="*"`) für nicht existierende Pfade umfassen. Die Wildcard-Route **shall** die `PageNotFound`-Komponente rendern, die eine interaktive ReactFlow-Darstellung (404-Fehlerbaum) anzeigt und den Nutzenden eine Navigation zurück zur Startseite ermöglicht.

## Akzeptanzkriterien

### Provider-Hierarchie und Initialisierung

- [x] Die `App`-Komponente rendert fehlerfrei und initialisiert die Provider-Hierarchie: `ThemeProvider` → `ReactFlowProvider` → `SnackbarProvider` → `Router` → `AuthProvider` → `RoleProvider` → `XAPIProvider` (verifiziert durch "App tests::renders correctly").
- [x] Der `useApp`-Hook lädt bei Initialisierung den User über `getUser()`, setzt die LMS-User-ID und konfiguriert das xAPI-Objekt mit Projekt-URL, Versionsnummer, Repositories und Fehler-Callback (verifiziert durch "App tests::useApp hook").
- [x] Schlägt `getUser()` fehl, wird der Fehler geloggt, aber die App bleibt lauffähig, und das xAPI-Objekt wird mit Platzhalter-Werten initialisiert (verifiziert durch "App tests::useApp hook with getUser failed").

### Benutzersitzung initialisieren

- [x] Beim Start wird der aktuelle Benutzer vom Backend abgerufen (`fetchUser`).
- [x] Wenn der Benutzer erfolgreich geladen wurde, wird der xAPI-Service mit der User-ID initialisiert.
- [x] Wenn das Laden fehlschlägt, wird der Fehler behandelt (z.B. Logging, Fehleranzeige).
- [x] Die Anwendung stellt den Benutzerkontext global bereit.

### Routing und 404-Handling

- [x] Alle definierten Routen (`/`, `/course/:courseId`, `/topic/:topicId`, `/login`, `/contact`, `/privacypolicy`, `/projectdescription`, `/glossary`, `/aboutus`, `/imprint`, `/learnercharacteristics`, `/rating`) sind in der `Routes`-Konfiguration registriert und rendern die zugehörigen Seitenkomponenten.
- [x] Die Wildcard-Route `path="*"` ist sowohl innerhalb als auch außerhalb des `MainFrame`-Layouts definiert und rendert die `PageNotFound`-Komponente für nicht existierende Pfade.
- [x] Die `PageNotFound`-Komponente zeigt eine ReactFlow-basierte Entscheidungsbaumvisualisierung mit Nodes ("404", "Do you know how you got here?", "Try to fix it", "Back home") und animierten Edges, die deterministisch dargestellt werden (verifiziert durch "PageNotFound::renders all nodes and edges").
- [x] Ein Klick auf den "Back home"-Node navigiert die Anwendung zur Startseite `/` (verifiziert durch "PageNotFound::navigates to home page when 'Back home' node is clicked").

### Integration und Konsistenz

- [x] Die Provider-Reihenfolge ist so gewählt, dass ThemeProvider Material-UI-Themes global verfügbar macht, bevor Komponenten gerendert werden, und AuthProvider vor RoleProvider ausgeführt wird, damit Rollenentscheidungen auf authentifizierten Nutzerdaten basieren.
- [x] Die `XAPIProvider` erhält die vom `useApp`-Hook bereitgestellten xAPI-Konfiguration, sodass alle Komponenten konsistente Tracking-Daten senden können.
- [x] Die `MainFrame`-Komponente umschließt die meisten Routen und stellt MenuBar, Breadcrumbs, LocalNavBar und Footer bereit; Login und statische Seiten können außerhalb des Frames gerendert werden, falls erforderlich.

## Rationale

SyRS-FUNC-001 fordert ein webbasiertes, responsives Frontend, das Nutzerinnen und Nutzer ohne Installation verwenden können. Die Implementierung als React SPA mit zentraler Provider-Hierarchie erfüllt diese Anforderung, indem sie eine konsistente Laufzeitumgebung für Theme-Anpassungen, Authentifizierung, Rollenverwaltung, Fehlerbehandlung (Snackbars) und Interaktionsverfolgung (xAPI) bereitstellt. Die Wildcard-Route mit der interaktiven 404-Seite verbessert die Nutzererfahrung, indem sie klar kommuniziert, dass ein Pfad nicht existiert, und eine einfache Rückkehrm

öglichkeit bietet.

## Hinweise

- Die Konfiguration wird in `index.tsx` aus `/config/env.<NODE_ENV>.json` geladen, bevor die App gerendert wird; Fehler beim Laden führen zu einem Alert und verhindern das Rendern.
- Die Provider-Reihenfolge ist kritisch: Änderungen können Kontextabhängigkeiten brechen (z. B. benötigt RoleProvider Zugriff auf AuthContext).
- Die `PageNotFound`-Komponente nutzt `reactflow` und erfordert, dass `ReactFlowProvider` in der Hierarchie vorhanden ist.
- Zukünftige Routen müssen in der `Routes`-Konfiguration registriert werden; andernfalls werden sie auf die 404-Seite geleitet.
