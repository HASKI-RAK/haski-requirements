# Stakeholder Requirement Specification – StRS-136

## 1. Identifikation

- **Requirement ID:** StRS-136
- **Owner:** Projektteam HASKI

## 2. Bezug

- **Zugehöriges Bedürfnis (NEED):** NEED-136 – Betriebsnahes Troubleshooting ohne externe Tools
- **Stakeholder:** Betrieb & Support (STK-05), Studierende (STK-01)

## 3. Anforderung (Requirement Statement)

Das HASKI-System **shall** einen integrierten Kanal bereitstellen, über den authentifizierte Nutzende während des Lernbetriebs spontane Diagnose- oder Fehlerbeschreibungen erfassen können, sodass der Betrieb strukturierte Log-Informationen je Nutzerkonto erhält, ohne dass separate Support-Portale oder E-Mail-Ketten notwendig sind.

## 4. Attribute

- **Priorität:** Medium
- **Typ:** Betrieb / Supportability
- **Risiko:** Mittel (fehlende Diagnoseinformationen verlängern Störungen)
- **Schwierigkeit:** Nominal

## 5. Rationale

Pilotbetriebe zeigten, dass bei technischen Problemen oft wesentliche Kontextinformationen fehlen oder nur manuell gesammelt werden. Ein eingebetteter Logbuffer pro Nutzer ermöglicht schnellere Ursachenanalyse und verkürzt Ausfallzeiten.

## 6. Quellen

- Operations-Retrospektive WiSe 2024/25
- Support-Tickets "Unvollständige Fehlerbeschreibung" (ServiceNow #SN-822)

## 7. Verifikation

- [x] Review (Abgleich mit Supportprozessen)
- [x] Analyse (Bewertung der bereitgestellten Felder und Zugriffskontrollen)
- [x] Test (Funktionsprüfung der Logbuffer-API im Staging)
- [x] Demonstration (Live-Durchlauf eines Incident-Playbooks)

## 8. Abhängigkeiten / Traceability

- [SyRS-FUNC-014](../../syrs/system-requirements/SyRS-FUNC/SyRS-FUNC-014.md) implementiert diese Stakeholder-Anforderung.
- [RTM](../../rtm/index.md) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## 9. Status

Proposed
