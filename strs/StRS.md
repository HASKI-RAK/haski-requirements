# Stakeholder-Bedürfnisse und Anforderungen (StRS)
für das HASKI-System nach ISO/IEC/IEEE 29148:2018 (Stakeholder Needs and Requirements)

## 1. Einleitung
### 1.1 Zweck der Stakeholder
Dieses Dokument definiert die Stakeholder-Bedürfnisse und -Anforderungen für das HASKI-System (Hochschullehre: Adaptiv, selbstgesteuert, KI-gestützt). Es dient als Grundlage für die Systemanforderungsspezifikation und stellt sicher, dass alle relevanten Interessensgruppen und deren Bedürfnisse bei der Entwicklung berücksichtigt werden.

### 1.2 Stakeholder-Geltungsbereich
Das HASKI-System ist eine KI-gestützte Software-Komponente zur Unterstützung adaptiven und selbstgesteuerten Lernens in Blended-Learning-Umgebungen an Hochschulen. Das System kommuniziert mit Learning Management Systemen (LMS) und erstellt mittels KI-Methoden Lernpfade und Bewertungen von Lernergebnissen. Bezug zu SRS (srs/SRS.md) und RTM (traceability/RTM.csv).

### 1.3 Überblick
Das HASKI-Gesamtkonzept besteht aus drei Komponenten: Lernraum, Learning Management System (LMS) und HASKI-System. Das System verwendet ein Lernenden-Modell, ein Tutorielles Modell und ein Domänen-Modell zur personalisierten Lernunterstützung.

### 1.4 Definitionen
- **HASKI-System**: KI-gestützte Software zur adaptiven Lernunterstützung
- **Lernenden-Modell**: Kategorisierung des Lerntyps mittels Bayesscher Netzwerke
- **Tutorielles Modell**: Generierung von Lernpfaden und Feedback
- **Domänen-Modell**: Organisation des fachspezifischen Wissens
- **Blended Learning**: Kombination aus Präsenz- und Online-Lernen

### 1.5 Stakeholder
| ID     | Name/Gruppe              | Typ (Kern/indirekt/regulatorisch/technisch/operativ) | Interessen/Ziele                             | Einfluss | Beteiligung (RACI) | Ansprechpartner |
|--------|--------------------------|-------------------------------------------------------|-----------------------------------------------|---------|--------------------|-----------------|
| STK-01 | Studierende              | Kern                                                  | Adaptives Lernen, individuelles Feedback, Selbststeuerung | Hoch    | R/A                | Studienvertreter |
| STK-02 | Lehrende                 | Kern                                                  | Unterstützung bei Bewertung, Lernfortschritt-Reports, Usability | Hoch    | R/C                | Professoren der Verbundpartner |
| STK-03 | Hochschulleitungen       | Operativ                                             | Verbesserung der Lehrqualität, Effizienzsteigerung | Hoch    | C/I                | Rektorate der Partnerhochschulen |
| STK-04 | Datenschutzbeauftragte:r | Regulatorisch                                        | DSGVO-Compliance, Datensicherheit             | Hoch    | C/I                | DSB der Hochschulen |
| STK-05 | IT-Administration        | Technisch                                            | Systemintegration, Wartbarkeit, Performance   | Mittel  | R/A                | IT-Leiter der Hochschulen |
| STK-06 | Didaktikzentren          | Operativ                                             | Hochschuldidaktische Qualität, Transferierbarkeit | Mittel  | C/I                | Didaktikzentrum Bayern |
| STK-07 | Projektförderer          | Regulatorisch                                        | Zielerreichung, ordnungsgemäße Mittelverwendung | Hoch    | C/I                | BMBF |
| STK-08 | OTH Regensburg           | Operativ                                             | Gesamtprojektleitung, KI-Expertise, Ethik & Datenschutz | Hoch    | R/A                | Prof. Dr. Jürgen Mottok |
| STK-09 | TH Aschaffenburg         | Operativ                                             | Teilprojekt 1, KI-Methoden, Bayessche Netzwerke | Hoch    | R/A                | Prof. Dr.-Ing. Jörg Abke |
| STK-10 | HS Kempten               | Operativ                                             | Teilprojekt 2, Video-Produktion, Lernmaterialien | Hoch    | R/A                | Prof. Dr. Georg Hagel |
| STK-11 | Wissenschaftliche Mitarbeiter | Technisch                                      | Entwicklung, Evaluation, pädagogische Betreuung | Hoch    | R/A                | Projektteams der Hochschulen |
| STK-12 | Studentische Hilfskräfte | Technisch                                            | Unterstützung bei Lernmaterialien, Tests     | Niedrig | R                  | Projektteams |
| STK-13 | Didaktikzentrum Bayern   | Operativ                                             | Hochschuldidaktische Qualität, Workshopdurchführung | Mittel  | C/I                | Didaktikzentrum Ingolstadt |
| STK-14 | Community (ECSEE, IEEE)  | Indirekt                                             | Wissenschaftlicher Austausch, Dissemination   | Niedrig | I                  | Fachkonferenzen |

## 2. Referenzen
| STK-09 | TH Aschaffenburg         | Operativ                                             | Teilprojekt 1, KI-Methoden, Bayessche Netzwerke | Hoch    | R/A                | Prof. Dr.-Ing. Jörg Abke |
| STK-10 | HS Kempten               | Operativ                                             | Teilprojekt 2, Video-Produktion, Lernmaterialien | Hoch    | R/A                | Prof. Dr. Georg Hagel |
| STK-11 | Wissenschaftliche Mitarbeiter | Technisch                                      | Entwicklung, Evaluation, pädagogische Betreuung | Hoch    | R/A                | Projektteams der Hochschulen |
| STK-12 | Studentische Hilfskräfte | Technisch                                            | Unterstützung bei Lernmaterialien, Tests     | Niedrig | R                  | Projektteams |
| STK-13 | Didaktikzentrum Bayern   | Operativ                                             | Hochschuldidaktische Qualität, Workshopdurchführung | Mittel  | C/I                | Didaktikzentrum Ingolstadt |

## 2. Referenzen
- ISO/IEC/IEEE 29148:2018
- governance/Requirements-Management-Plan.md
- srs/SRS.md
- traceability/RTM.csv
- Richtlinie zur Bund-Länder-Initiative zur Förderung der KI in der Hochschulbildung
- DSGVO

## 3. Anforderungen an das Geschäftsmanagement
### 3.1 Geschäftsumfeld
Das HASKI-System operiert im Hochschulbildungsbereich mit Fokus auf technische Studiengänge (Informatik, Software Engineering, Game Engineering). Das System soll fach- und institutsübergreifend an Hochschulen einsetzbar sein.

### 3.2 Mission, Ziele und Zweck
**Mission**: Verbesserung der Hochschullehre durch adaptives, selbstgesteuertes und KI-gestütztes Lernen
**Ziele**: 
- Individualisierte Lernunterstützung für Studierende
- Entlastung der Lehrenden durch automatisierte Bewertung und Reporting
- Förderung selbstgesteuerten und lebenslangen Lernens

### 3.3 Geschäftsmodell
Open Science Ansatz - das System soll allen Hochschullehrenden fach- und institutsübergreifend zur Verfügung gestellt werden. Keine kommerzielle Verwertung geplant.

### 3.4 Informationsumfeld
Integration in bestehende LMS (primär Moodle), Datenaustausch über LTI-Standard, Eye-Tracking-Daten für Forschungszwecke, Compliance mit Datenschutzbestimmungen.

## 4. Anforderungen an den Systembetrieb
### 4.1 Systemprozesse
- Kontinuierliche Analyse von Lernverhalten und Anpassung der Lernpfade
- Automatische Bewertung verschiedener Aufgabentypen (Quiz, Freitext, Code, Diagramme)
- Generierung von Feedback für Lernende und Reports für Lehrende
- Integration mit LMS über standardisierte Schnittstellen

### 4.2 Systembetriebsrichtlinien und -regeln
- 24/7 Verfügbarkeit während Vorlesungszeiten
- Einhaltung der DSGVO und hochschulspezifischer Datenschutzrichtlinien
- Backup und Disaster Recovery Prozeduren
- Regelmäßige Updates und Wartung

### 4.3 Systembetriebliche Einschränkungen
- Abhängigkeit von LMS-Verfügbarkeit
- Rechenintensive KI-Operationen erfordern entsprechende Hardware
- Datenschutzrechtliche Beschränkungen bei der Datenverarbeitung

### 4.4 Systembetriebsmodi und -zustände
- Adaptiver Modus: System passt Lernpfade automatisch an
- Selbstgesteuerter Modus: Lernende wählen Lernpfade selbst
- Wartungsmodus: Temporäre Einschränkung der Funktionalität

## 5. Benutzeranforderungen
### Stakeholder-Bedürfnisse (informell)
- **NEED-001**: Studierende benötigen individuell angepasste Lernpfade basierend auf ihrem Kenntnisstand und Lernstil
- **NEED-002**: Studierende benötigen sofortiges, spezifisches Feedback zu ihren Lösungen
- **NEED-003**: Studierende benötigen die Möglichkeit zur Selbststeuerung ihres Lernprozesses
- **NEED-004**: Lehrende benötigen aussagekräftige Reports über den Lernfortschritt ihrer Studierenden
- **NEED-005**: Lehrende benötigen Unterstützung bei der automatisierten Bewertung von Aufgaben
- **NEED-006**: System muss mit vorhandenem LMS (Moodle) integrierbar sein
- **NEED-007**: Datenschutz und Datensicherheit müssen gewährleistet sein

### Stakeholder-Anforderungen (formell)
> Hinweis: in `strs/stakeholder-requirements/StRS-NNN.md` jeweils eine Stakeholder-Anforderung.

## 6. Detaillierte Lebenszyklus-Konzepte des vorgeschlagenen Systems
### 6.1 Betriebskonzept
Blended-Learning-Umgebung mit Integration in bestehende Hochschul-IT-Infrastruktur. Betrieb erfolgt dezentral an den Partnerhochschulen mit zentraler Koordination.

### 6.2 Betriebsszenarien
- Regulärer Lehrbetrieb in verschiedenen Informatik-Modulen
- Evaluations- und Testbetrieb mit wissenschaftlicher Begleitung
- Wartungs- und Update-Szenarien

### 6.3 Beschaffungskonzept
Entwicklung im Projektrahmen, Open Source Komponenten wo möglich, spezielle KI-Software:
- HUGIN Researcher für Bayessche Netzwerke (TH Aschaffenburg)
- Vyond Premium Lizenz für Animationsvideos (HS Kempten)
- Serverhardware und KI-Rechner für maschinelles Lernen
- Eye-Tracking-Labor (20 Arbeitsplätze an OTH Regensburg)

### 6.4 Einführungskonzept
Iterative Einführung über Projektverlauf (48 Monate), Start mit Pilotveranstaltungen, schrittweise Ausweitung auf weitere Module und Hochschulen.

### 6.5 Betreuungskonzept
Wissenschaftliche Mitarbeiter für technische Betreuung, pädagogische Mitarbeiter für didaktische Unterstützung, zentrale Projektkoordination.

### 6.6 Außerbetriebnahmekonzept
Nach Projektende: Überführung in regulären Hochschulbetrieb oder Open Source Community, Datenmigration und -archivierung nach rechtlichen Vorgaben.

## 7. Projektbeschränkungen
- **Zeitliche Beschränkung**: Projektlaufzeit 48 Monate (1.1.2022-31.12.2025)
- **Finanzielle Beschränkung**: Förderrahmen des BMBF
- **Technische Beschränkung**: Integration nur mit Moodle-LMS
- **Fachliche Beschränkung**: Fokus auf Informatik-Domänen
- **Rechtliche Beschränkung**: DSGVO-Compliance erforderlich
- **Geografische Beschränkung**: Beschränkung auf deutsche Hochschulen

## 8. Anhang
### 8.1 Abkürzungen und Begriffe
- **BMBF**: Bundesministerium für Bildung und Forschung
- **DSGVO**: Datenschutz-Grundverordnung
- **HKE**: Hochschule Kempten (Hochschule für angewandte Wissenschaften Kempten)
- **LMS**: Learning Management System
- **LTI**: Learning Tools Interoperability
- **OTH R**: Ostbayerische Technische Hochschule Regensburg
- **RCAI**: Regensburg Center for Artificial Intelligence
- **SECAT**: Software Engineering Competency Assessment Tool
- **THAB**: Technische Hochschule Aschaffenburg

## 9 Traceability
- Bidirektionale Nachverfolgbarkeit Stakeholder → Anforderungen: siehe traceability/RTM.csv

## Ermittlung & Validierung
**Verwendete Methoden**: 
- Systematisches Literaturreview zu adaptiven Lernumgebungen
- Grounded-Theory-Methodologie für Evaluationen
- Eye-Tracking-Studien für Nutzungsanalysen
- Befragungen und Beobachtungen der Nutzerinteraktionen

**Review-/Abnahmeprozess**: Iterative Evaluationen mit Studierenden und Lehrenden, Abstimmung mit Datenschutzbeauftragten, wissenschaftliche Begutachtung durch Projektbeirat

**Status**: In Entwicklung (Projektlaufzeit 1.1.2022-31.12.2025)