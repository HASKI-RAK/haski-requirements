---
id: HASKI-REQ-0001
title: Datenschutzerklärung-Einwilligung vor Login
type: Functional
status: Implemented
source_id: SyRS-COMP-001
merged_from: ["HASKI-REQ-0032"]
links:
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#195",
      "HASKI-RAK/HASKI-Frontend#226",
      "HASKI-RAK/HASKI-Frontend#229",
    ]
  parents: ["SyRS-COMP-001", "SyRS-SEC-001"]
  tests:
    - path: "frontend/src/components/PrivacyModal/PrivacyModal.test.tsx"
      name: "Test PrivacyModal"
---

## Beschreibung

Das System **shall** vor dem ersten Login oder bei nicht erteilter Einwilligung einen Modal-Dialog anzeigen, der die Studierenden zur Akzeptanz der Datenschutzerklärung auffordert. Die Einwilligung **shall** in localStorage gespeichert werden und bei jedem Login überprüft werden. Falls die Einwilligung nicht erteilt wurde (localStorage["consent"] = false oder nicht gesetzt), **shall** der Modal-Dialog erneut angezeigt werden.

Das System **shall** Studierenden, die die funktionalen Cookies ablehnen, auf eine dedizierte Seite weiterleiten, die erklärt, dass das System ohne Cookies nicht nutzbar ist. Diese Seite **shall** eine Option bieten, die Cookie-Richtlinien erneut zu öffnen und die Entscheidung zu überdenken.

Ergänzend **shall** das HASKI-System technische Verfahren zur Anonymisierung und Pseudonymisierung von Lern- und Nutzungsdaten implementieren, um die Identifizierbarkeit einzelner Personen zu verhindern und die DSGVO-Anforderungen gemäß Art. 25 und 32 zu erfüllen. Personenbezogene Identifikatoren **shall** von Nutzungsdaten getrennt, pseudonymisiert und nur über verschlüsselte Zuordnungstabellen verknüpft werden, damit Einwilligungs- und Datenschutzniveau auch bei Auswertungen gewahrt bleibt.

## Akzeptanzkriterien

- [x] Nach Klick auf den Login-Button öffnet sich ein Modal, das den Benutzer fragt, ob er die Datenschutzerklärung akzeptiert
- [x] Der Modal öffnet sich jedes Mal, wenn localStorage["consent"] = false oder nicht gesetzt ist
- [x] Wenn der Benutzer die funktionalen Cookies nicht zulässt, wird er auf eine Seite weitergeleitet, die ihn darüber informiert, dass er das System ohne Cookies nicht nutzen kann
- [x] Auf dieser Seite kann der Benutzer seine Cookie-Richtlinien erneut öffnen und seine Entscheidung überdenken
- [x] Die Einwilligung wird persistent in localStorage gespeichert
- [x] Unit test coverage > 90%
- [x] Technische Dokumentation im GitHub Wiki erstellt

### Anonymisierung und Pseudonymisierung von Nutzungsdaten

- [ ] Personenbezogene Daten werden bei der Speicherung automatisch pseudonymisiert.
- [ ] Wissenschaftliche Auswertungen arbeiten ausschließlich mit anonymisierten Datensätzen.
- [ ] Pseudonyme sind nicht ohne Zugriff auf die verschlüsselte Zuordnungstabelle rückführbar.
- [ ] Das System implementiert eine klare Trennung zwischen identifizierenden Daten (Name, E-Mail, Matrikelnummer) und Nutzungsdaten (Lernfortschritt, Interaktionen).
- [ ] Zuordnungstabellen zwischen Pseudonymen und Identitäten sind verschlüsselt gespeichert.
- [ ] Zugriffsrechte auf Pseudonymisierungsschlüssel sind streng limitiert und protokolliert.
- [ ] Das System unterstützt vollständige Anonymisierung für Forschungsdaten (irreversible Entfernung aller identifizierenden Merkmale).
- [ ] Datenschutzbeauftragte und IT-Sicherheitsexpert:innen haben die Verfahren geprüft und freigegeben.
- [ ] Penetrationstests zeigen, dass eine Rückführbarkeit anonymisierter Daten nicht möglich ist.

## Rationale

Primary implementation: GitHub issue GH-195: "User has to accept Privacy Policy before he logs in"

Related work:

- GH-226: "Set up HASKI account the first time a user enters" - Erweitert das Konzept auf einen umfassenden Onboarding-Prozess, der neben der Datenschutzerklärung auch Cookies, Nutzungsbedingungen und Fragebögen einschließt

Derived from system requirement SyRS-COMP-001, which implements stakeholder requirement StRS-104 ensuring compliance with DSGVO requirements for informed consent and data protection.

Ergänzend derived from system requirement SyRS-SEC-001 and stakeholder requirement StRS-120, die technische und organisatorische Maßnahmen zur Anonymisierung und Pseudonymisierung von Lern- und Nutzungsdaten fordern. Dadurch kann die Vertraulichkeit der Studierenden gewahrt und gleichzeitig die wissenschaftliche Auswertung von Lernverhalten ermöglicht werden.

## Hinweise

- Primary issue: https://github.com/HASKI-RAK/HASKI-Frontend/issues/195
- Related issue: https://github.com/HASKI-RAK/HASKI-Frontend/issues/226
- Implementation uses localStorage for consent tracking (key: "consent")
- Modal-based UI pattern for user interaction
- Fallback page shown when functional cookies are declined
- Consent must be obtained before any personal data processing occurs
