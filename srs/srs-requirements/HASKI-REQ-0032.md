---
id: HASKI-REQ-0032
title: Implementierung von Anonymisierungs- und Pseudonymisierungsverfahren für Nutzungsdaten
type: NFR:Security
status: Proposed
source_id: SyRS-SEC-001
links:
  stories: []
  parents: ["SyRS-SEC-001"]
---

## Beschreibung

Das HASKI-System **shall** technische Verfahren zur Anonymisierung und Pseudonymisierung von Lern- und Nutzungsdaten implementieren, um die Identifizierbarkeit einzelner Personen zu verhindern und die DSGVO-Anforderungen gemäß Art. 25 und 32 zu erfüllen.

Das System **shall** folgende Funktionen bereitstellen:
- Pseudonymisierung von Nutzerdaten bei der Speicherung in der Datenbank
- Anonymisierung von Daten für wissenschaftliche Auswertungen und Analysen
- Trennung von identifizierenden Merkmalen und Nutzungsdaten
- Verschlüsselte Speicherung von Zuordnungstabellen zwischen Pseudonymen und realen Identitäten

## Akzeptanzkriterien

- [ ] Personenbezogene Daten werden bei der Speicherung automatisch pseudonymisiert
- [ ] Wissenschaftliche Auswertungen arbeiten ausschließlich mit anonymisierten Datensätzen
- [ ] Pseudonyme sind nicht ohne Zugriff auf die verschlüsselte Zuordnungstabelle rückführbar
- [ ] Das System implementiert eine klare Trennung zwischen identifizierenden Daten (Name, E-Mail, Matrikelnummer) und Nutzungsdaten (Lernfortschritt, Interaktionen)
- [ ] Zuordnungstabellen zwischen Pseudonymen und Identitäten sind verschlüsselt gespeichert
- [ ] Zugriffsrechte auf Pseudonymisierungsschlüssel sind streng limitiert und protokolliert
- [ ] Das System unterstützt vollständige Anonymisierung für Forschungsdaten (irreversible Entfernung aller identifizierenden Merkmale)
- [ ] Datenschutzbeauftragte und IT-Sicherheitsexpert:innen haben die Verfahren geprüft und freigegeben
- [ ] Penetrationstests zeigen, dass eine Rückführbarkeit anonymisierter Daten nicht möglich ist

## Rationale

Derived from system requirement SyRS-SEC-001 and stakeholder requirement StRS-120.

Die DSGVO (EU-Verordnung 2016/679, Art. 25, 32) fordert die Minimierung personenbezogener Daten und den Einsatz geeigneter technischer und organisatorischer Maßnahmen zum Schutz der Vertraulichkeit. Durch Anonymisierung und Pseudonymisierung kann die Vertraulichkeit der Studierenden gewahrt und gleichzeitig die wissenschaftliche Auswertung von Lernverhalten ermöglicht werden.

Diese Anforderung adressiert ein hohes Rechtsrisiko bei unzureichender Umsetzung und ist essentiell für das Vertrauen der Nutzer:innen in das System.

## Hinweise

- Keine direkte GitHub Issue gefunden - diese Anforderung basiert auf DSGVO-Compliance-Vorgaben
- Verwandte Stakeholder-Anforderung: [StRS-120](../../strs/stakeholder-requirements/StRS-120.md)
- Verifizierung erfolgt durch Review (Datenschutzbeauftragte), Analyse der Verfahren, Tests (Angriffsszenarien) und Demonstration im Pilotbetrieb
- Die Implementierung sollte kryptografische Best Practices für die Verschlüsselung von Zuordnungstabellen verwenden
- Es ist ein Konzept zur sicheren Verwaltung von Pseudonymisierungsschlüsseln erforderlich
- Berücksichtigung der Anforderungen aus der Projektbeschreibung HASKI (Teil A, Kapitel 6: Ethische und rechtliche Rahmenbedingungen)
