# Stakeholder Requirement Specification – StRS-134

## 1. Identifikation
- **Requirement ID:** StRS-134
- **Owner:** Projektteam HASKI

## 2. Bezug
- **Zugehöriges Bedürfnis (NEED):** NEED-134 – Proaktive Überwachung der Nutzererfahrung über Web-Vitals
- **Stakeholder:** IT-Administration & Betrieb (STK-05)

## 3. Anforderung (Requirement Statement)
Das HASKI-System **shall** Telemetriedaten zur wahrgenommenen Frontend-Performance (z. B. Google Web Vitals) zentral erfassen, damit das Betriebsteam Fehlerbilder und Performance-Regressionen zeitnah identifizieren kann.

## 4. Attribute
- **Priorität:** Mittel
- **Typ:** Betrieb / Monitoring
- **Risiko:** Mittel (fehlende Telemetrie erschwert Incident Response)
- **Schwierigkeit:** Nominal

## 5. Rationale
Ohne objektive Web-Vitals-Daten bleiben Performance-Probleme oft unentdeckt, bis sich Beschwerden häufen. Eine einheitliche Erfassung im Backend erlaubt Trendanalysen, erleichtert Root-Cause-Analysen und liefert Nachweise für Fördermittelgebende zur Systemstabilität.

## 6. Quellen
- Post-Mortem-Notizen zu Performanceproblemen (WS 2024/25)
- Betriebshandbuch HASKI, Kapitel "Monitoring & Observability"

## 7. Verifikation
- [x] Review (Abgleich des Telemetrie-Konzepts mit Monitoring-Guidelines)
- [x] Analyse (Überprüfung der erfassten Metriken und Pflichtfelder)
- [x] Test (Senden repräsentativer Web-Vitals-Datenströme an das Backend)
- [x] Demonstration (Live-Abruf der gesammelten Logs für Admins)

## 8. Abhängigkeiten / Traceability
- [SyRS-FUNC-012](../../syrs/system-requirements/SyRS-FUNC/SyRS-FUNC-012.md) referenziert diese StRS.
- [RTM](../../rtm/index.md) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## 9. Status
Proposed
