# Project Plan – HASKI

## 1 Zweck und Geltungsbereich
Dieser Projektplan beschreibt Vorgehen, Organisation und Tailoring des SDLC für das Projekt **HASKI** im Rahmen des Verbundprojekts *Hochschullehre: Adaptiv, selbstgesteuert, KI-gestützt (HASKI)*.  
Er richtet sich an Fördergeber, Projektleitung und Entwicklerteams.  

## 2 Referenzen
- HASKI Projektbeschreibung (BMBF, 2021)  
- HASKI-KE Teilvorhabenbeschreibung  
- HASKI-KE Arbeitsprogramm, Arbeitspakete (AP 1–7) und Meilensteine
- ISO/IEC/IEEE 29148:2018 (Requirements)  
- ISO/IEC/IEEE 15289:2019 (Documentation) //TODO: Naming und Jahreszahlen prüfen
- ISO/IEC/IEEE 12207:2017 (Software Life Cycle Processes)  

## 3 Projektziele
- Entwicklung und Erprobung des HASKI-Systems mit adaptiven, KI-gestützten Lernfunktionen.  
- Integration in Moodle und Lernräume an Hochschulen.  
- Datenschutz- und Sicherheitskonzept (Meilenstein 17).  
- Evaluation der Wirksamkeit und Dissemination (AP 6, AP 7).  

## 4 Tailoring und Conformance-Matrix
Das Projekt folgt ISO/IEC/IEEE 15289 als Dokumentationsrahmen.
Volle IEEE-Konformität wird nicht beansprucht; stattdessen Tailoring gemäß Projektbedarf.
Information Items aus 15289 §10 werden nur wenn für das Projekt relevant in der Tabelle aufgeführt. Begründung: Die meisten Items sind durch den Projektantrag und das Arbeitsprogramm bereits abgedeckt.

//TODO: Up to date halten
| Normabschnitt (29148)                | Umsetzung im Projekt                | Status | Bemerkung               |
|-----------------------------------------|-------------------------------------|--------| ------------------------|
| 8.2 Business Requirements Specification     | nicht umgesetzt                     | nicht geplant |  Durch das BMBF auf Basis eines genehmigten Projektantrags bewilligt.BRS-Dokument nicht erforderlich. Grundlegenden Ziele, Rahmenbedingungen und Anforderungen bereits im Projektantrag beschrieben, von der Förderinstitution geprüft und akzeptiert.
8.4 System Requirements Specification | nicht umgesetzt | nicht geplant | 
| 9.4 Stakeholder Requirements Spec.        | `strs/StRS.md` + `strs/stakeholder-requirements/` | erstellt | vollständig |
| 9.6 System/Software Requirements Spec.      | `srs/SRS.md` + `requirements/`      | erstellt | vollständig |
|-----------------------------------------------|-------------------------------------|---------| ------------------------|
| Information Item (15289)                      | Umsetzung im Projekt                | Status  | Bemerkung               |
|-----------------------------------------------|-------------------------------------|---------| ------------------------|
| 10.60 System Architecture Description         | `architecture/System-AD.md`         | geplant | Noch unklar |
| 10.61 Test Plan / Specs / Report              | `tests/`                            | geplant | |
| 10.52 Risk Management Plan                    | `governance/Risk-Management-Plan.md`| geplant | |
| 10.9 Configuration Management Plan            | `governance/CM-Plan.md`             | geplant | |
| 10.24 Information Security Plan               | `governance/Info-Security-Plan.md`  | geplant | |
| 10.69 + 10.71 / 10.72 + 10.74 Validation / Verification Plans+Reports | `vnv/`      | geplant | |
| 10.41 Progress Reports                        | GitHub Issues / Milestones          | laufend | In den [Ressourcen](#8-Ressourcen) aufgeführt |


## 5 Arbeitspakete und Bezug
- **AP 1**: Modelle entwickeln (Lernenden-, Tutorielles-, Domänenmodell)  
- **AP 2**: Abbildung der Modelle in HASKI, automatische Antwortbewertung, Berichte für Lehrende  
- **AP 3**: Lerninhalte, Lernpfade, Feedback, Moodle-Kommunikation  
- **AP 4**: Datenschutz- und Datensicherheitskonzept (Meilenstein 17)  
- **AP 5**: Lehrveranstaltungen Software Engineering (Einbindung Studierende)  
- **AP 6**: Evaluation und Reflexion, inkl. Eye-Tracking-Experimente  
- **AP 7**: Dissemination (Workshops, ECSEE Konferenz):contentReference[oaicite:4]{index=4}

## 6 Zeitplan / Meilensteine
- **MS 1–8**: Modelle erstellt (jeweils 14.03. und 30.09. pro Jahr)  
- **MS 9–12**: Inkrement-Versionen HASKI-System (30.09. jährlich)  
- **MS 13–16**: Inkrement-Versionen Moodle-Anbindung (30.09. jährlich)  
- **MS 17**: Datenschutzkonzept abgeschlossen (30.09.2023)  
- **MS 18–24**: Evaluation/Reflexion abgeschlossen (31.05. / 31.10. jährlich)  
- **MS 25–26**: Projektkonferenzen ECSEE (31.07.2023, 31.07.2025)  
- **MS 27**: Dissemination abgeschlossen (30.11.2025)

## 7 Rollen und Verantwortlichkeiten
- **Projektleitung HASKI:** OTH Regensburg
- **Verbundspartner:** OTH Regensburg
- **Verbundspartner:** TH Aschaffenburg 
- **Verbundpartner:** Hochschule Kempten
- **Dev-Team:** Frontend, Backend, AI/ML (NodeGrade)
- **QA/CM:** Verantwortlich für Reviews, Baselines, RTM  
- **Datenschutz:** Beauftragte für Meilenstein 17

## 8 Ressourcen
- GitHub-Organisation *HASKI* (Repos:  
    - [HASKI-Frontend](https://github.com/HASKI-RAK/HASKI-Frontend)  
    - [HASKI-Backend](https://github.com/HASKI-RAK/HASKI-Backend)  
    - [NodeGrade](https://github.com/HASKI-RAK/NodeGrade)  
    - [HASKI-Requirements](https://github.com/HASKI-RAK/haski-requirements)  
)  
- Infrastruktur: Hochschulserver, Moodle-Instanzen, Eye-Tracking-Lab OTH R  
- Budget gemäß Förderbescheid

## 9 Risiko und Qualitätssicherung (Kurzüberblick)
- Risiken: technologische Reife KI-Bewertung, Datenschutz, Interoperabilität Moodle.  
- Maßnahmen: eigenes `Risk-Management-Plan.md`.  
- Qualität: SQA nach IEEE 730, Dokumentations-Tailoring nach 15289.

## 10 Review und Reporting
- Projektinterne Reviews aller Requirements und Pläne.
- RTM-Generierung automatisiert. //TODO: Beschreiben wie genau
---

*Version 2.2*
