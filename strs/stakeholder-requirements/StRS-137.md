# Stakeholder Requirement Specification – StRS-137

## 1. Identifikation

- **Requirement ID:** StRS-137
- **Owner:** Projektteam HASKI

## 2. Bezug

- **Zugehöriges Bedürfnis (NEED):** NEED-137 – Betrieb benötigt einen aktuellen Überblick über alle HASKI-Nutzerkonten und deren Rollenstatus
- **Stakeholder:** IT-Administration & Betrieb (STK-05)

## 3. Anforderung (Requirement Statement)

Das HASKI-System **shall** dem Betriebsteam ein zentrales, mandantenfähiges Nutzerverzeichnis bereitstellen, das alle angelegten Konten inklusive Rolle, Zugehörigkeit zur Hochschule und Betriebsstatus nachvollziehbar ausweist, sodass Administrierende Audits, Supportfälle und Compliance-Prüfungen ohne Datenexporte durchführen können.

## 4. Attribute

- **Priorität:** Mittel
- **Typ:** Betrieb / Compliance
- **Risiko:** Mittel (fehlende Transparenz über aktive Konten erschwert Incident Response und Datenschutz-Audits)
- **Schwierigkeit:** Nominal

## 5. Rationale

Pilotbetriebe meldeten wiederholt Support-Tickets (z. B. ITSM-284 "Unbekannter Nutzer führt Aktionen aus"), weil kein einheitlicher Überblick über aktive Rollen und Zugehörigkeiten vorlag. Ein integriertes Nutzerverzeichnis verkürzt die Bearbeitungszeit für Incident- und Berechtigungsprüfungen und liefert revisionssichere Nachweise für Fördermittelgebende.

## 6. Quellen

- Betriebshandbuch HASKI, Kapitel "Identity & Access Management"
- ServiceNow Ticket ITSM-284 (04/2025)
- Abstimmung mit IT-Administration TH-AB (Workshop 2025-05-12)

## 7. Verifikation

- [ ] Review (Abgleich des Nutzerverzeichniskonzepts mit Betriebsteam)
- [ ] Analyse (Prüfung der gelieferten Attribute auf Vollständigkeit und Mandantenfähigkeit)
- [ ] Test (Abruftests mit echten und fehlerhaften Admin-IDs)
- [ ] Demonstration (Live-Audit im Pilotbetrieb)

## 8. Abhängigkeiten / Traceability

- [SyRS-FUNC-015](../../syrs/system-requirements/SyRS-FUNC/SyRS-FUNC-015.md) konkretisiert diese StRS.
- [RTM](../../rtm/index.md) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## 9. Status

Proposed
