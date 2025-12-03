# Stakeholder Requirement Specification – StRS-139

## 1. Identifikation

- **Requirement ID:** StRS-139
- **Owner:** Projektteam HASKI

## 2. Bezug

- **Zugehöriges Bedürfnis (NEED):** NEED-139 – Studierende benötigen eine konsistente Orientierung innerhalb der HASKI-Weboberfläche, um zwischen Kurs-, Topic- und Supportseiten zielgerichtet zu wechseln.
- **Stakeholder:** Studierende (STK-01), Didaktik (STK-04)

## 3. Anforderung (Requirement Statement)

Das HASKI-System **shall** eine konsistente Navigationsführung mit Breadcrumbs bereitstellen, die den aktuellen Kontext (Kurs, Topic, Unterseite) sichtbar macht und schnelle Rücksprünge auf übergeordnete Ebenen ermöglicht.

## 4. Attribute

- **Priorität:** Hoch
- **Typ:** Funktional / UX
- **Risiko:** Mittel (Verwirrung über Navigationspfade führt zu Abbruch im Selbstlernprozess)
- **Schwierigkeit:** Nominal

## 5. Rationale

In Evaluationsinterviews (HASKI Eval-2, 2023-03) meldeten Studierende wiederholt Orientierungsschwierigkeiten nach dem Aufrufen tiefer Kursseiten. Eine sichtbare Breadcrumb-Navigation reduziert Suchaufwand, verringert Fehlbedienungen und unterstützt die didaktische Strukturierung der Lernräume.

## 6. Quellen

- UX-Evaluation „Eval-2“ (März 2023)
- Mockups HASKI MainFrame v0.8 (UX-Team)
- GitHub Issue [#124](https://github.com/HASKI-RAK/HASKI-Frontend/issues/124)

## 7. Verifikation

- [ ] Review (Abgleich mit UX-Richtlinien der HASKI-Oberfläche)
- [ ] Analyse (Navigationskonzept gegen Informationsarchitektur prüfen)
- [x] Test (Automatisierte UI-Tests belegen Funktion der Breadcrumbs)
- [ ] Demonstration (Usability-Session mit Studierenden bestätigt Orientierung)

## 8. Abhängigkeiten / Traceability

- [SyRS-FUNC-019](../../syrs/system-requirements/SyRS-FUNC/SyRS-FUNC-019.md) konkretisiert diese Stakeholder-Anforderung.
- [RTM](../../rtm/index.md) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## 9. Status

Implemented
