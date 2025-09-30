# Stakeholder Requirement Specification – StRS-120

## 1. Identifikation
- **Requirement ID:** StRS-120
- **Owner:** Projektteam HASKI

## 2. Bezug
- **Zugehöriges Bedürfnis (NEED):** NEED-120 – Technische Verfahren zur Anonymisierung und Pseudonymisierung der Lern- und Nutzungsdaten
- **Stakeholder:** Datenschutzbeauftragte (STK-04)

## 3. Anforderung (Requirement Statement)
Das HASKI-System **shall** technische Verfahren zur Anonymisierung und Pseudonymisierung sämtlicher Lern- und Nutzungsdaten implementieren, um die Identifizierbarkeit einzelner Personen zu verhindern.

## 4. Attribute
- **Priorität:** Hoch
- **Typ:** Compliance / Sicherheit
- **Risiko:** Hoch (Rechtsrisiko bei unzureichender Anonymisierung, Verlust des Vertrauens der Nutzer:innen)
- **Schwierigkeit:** Schwer

## 5. Rationale
Die DSGVO fordert die Minimierung personenbezogener Daten. Durch Anonymisierung und Pseudonymisierung kann die Vertraulichkeit der Studierenden gewahrt und gleichzeitig die wissenschaftliche Auswertung ermöglicht werden.

## 6. Quellen
- DSGVO (EU-Verordnung 2016/679, Art. 25, 32)
- Projektbeschreibung HASKI (Teil A, Kapitel 6: Ethische und rechtliche Rahmenbedingungen)

## 7. Verifikation
- [x] Review (Prüfung durch Datenschutzbeauftragte und IT-Sicherheitsexpert:innen)
- [x] Analyse (Bewertung der eingesetzten Anonymisierungs- und Pseudonymisierungsverfahren)
- [x] Test (Simulation von Angriffsszenarien zur Rückführbarkeit)
- [x] Demonstration (Nachweis der Verfahren im Pilotbetrieb)

## 8. Abhängigkeiten / Traceability
- [SRS-requirements](../../requirements/HASKI-REQ-NNNN.md) und SyRS referenzieren einzelne StRS.
- [RTM](../../rtm/RTM.csv) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## 9. Status
Verifiziert
