# Stakeholder Requirement Specification – StRS-138

## 1. Identifikation

- **Requirement ID:** StRS-138
- **Owner:** Projektteam HASKI

## 2. Bezug

- **Zugehöriges Bedürfnis (NEED):** NEED-138 – Analytics-Team benötigt einheitliche Nutzungsdaten über alle UI-Komponenten
- **Stakeholder:** Didaktik & Analytics (STK-07)

## 3. Anforderung (Requirement Statement)

Das HASKI-System **shall** sämtliche Benutzerinteraktionen mit den Standard-UI-Komponenten konsistent erfassen und als xAPI-konforme Lernaktivitäten bereitstellen, sodass das Analytics-Team Nutzungsdaten ohne manuelle Instrumentierung einzelner Ansichten auswerten kann.

## 4. Attribute

- **Priorität:** Hoch
- **Typ:** Analytics / Berichtswesen
- **Risiko:** Mittel (fragmentierte Instrumentierung verhindert aussagekräftige Lernanalysen und erschwert Evaluationsberichte)
- **Schwierigkeit:** Nominal

## 5. Rationale

Im Evaluationslauf Eval-4 meldeten Fachdidaktik und Projektleitung (Workshops 2025-04-09/16), dass fehlende oder uneinheitliche xAPI-Ereignisse eine Zusammenführung der Nutzungsmetriken erschweren. Durch eine zentral geregelte Instrumentierung aller Standard-UI-Komponenten wird gewährleistet, dass jede Nutzeraktion mit Quelle, Typ und Kontext protokolliert wird und damit für Learning-Analytics-Berichte und Wirknachweise zur Verfügung steht.

## 6. Quellen

- Workshop-Protokolle Eval-4 (Analytics-Track), April 2025
- GitHub Issue [#285](https://github.com/HASKI-RAK/HASKI-Frontend/issues/285)
- Tracking-Konzept "Learning Analytics Consolidation" v1.3

## 7. Verifikation

- [ ] Review (Abgleich des Instrumentierungskonzepts mit Analytics-Team)
- [ ] Analyse (Stichproben der erzeugten xAPI-Statements auf Vollständigkeit)
- [ ] Test (automatisierte UI-Tests prüfen, dass Standardkomponenten Ereignisse ohne Laufzeitfehler protokollieren)
- [ ] Demonstration (Dashboard zeigt aggregierte Nutzungsdaten aus Standardkomponenten)

## 8. Abhängigkeiten / Traceability

- [SyRS-FUNC-018](../../syrs/system-requirements/SyRS-FUNC/SyRS-FUNC-018.md) konkretisiert diese StRS.
- [RTM](../../rtm/index.md) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## 9. Status

Implemented
