# Stakeholder-Bedürfnisse und Anforderungen (StRS)
für das HASKI-System nach ISO/IEC/IEEE 29148:2018 (Stakeholder Needs and Requirements)

## 1. Einleitung
### 1.1 Zweck des Stakeholder-Dokuments
Dieses Dokument identifiziert systematisch alle Stakeholder des HASKI-Systems, analysiert deren Bedürfnisse, Erwartungen und Einflussbereiche, und leitet daraus formelle Stakeholder-Anforderungen ab. Es bildet die Grundlage für die nachgelagerte Systemanforderungsspezifikation (SRS) und gewährleistet, dass alle relevanten Interessensgruppen im Entwicklungsprozess angemessen berücksichtigt werden.

### 1.2 Stakeholder-Geltungsbereich
Das HASKI-System ist eine KI-gestützte Software-Komponente zur Unterstützung adaptiven und selbstgesteuerten Lernens in Blended-Learning-Umgebungen an Hochschulen. Das System kommuniziert mit Learning Management Systemen (LMS) und erstellt mittels KI-Methoden Lernpfade und Bewertungen von Lernergebnissen. Bezug zu SRS (srs/SRS.md) und RTM (traceability/RTM.csv).

### 1.3 Überblick
Dieses Dokument identifiziert und analysiert die verschiedenen Stakeholder-Gruppen des HASKI-Systems sowie deren spezifische Bedürfnisse, Erwartungen und Anforderungen. Es definiert die Interessen und Einflussgrade aller beteiligten Parteien und leitet daraus formelle Stakeholder-Anforderungen ab, die als Grundlage für die Systemanforderungsspezifikation dienen.

### 1.4 Stakeholder-Analysemethodik
Dieses Dokument verwendet einen systematischen Ansatz zur Stakeholder-Identifikation und -Analyse:
- **Stakeholder-Identifikation**: Ermittlung aller direkt und indirekt betroffenen Gruppen
- **Interessens-Analyse**: Bewertung der spezifischen Ziele und Erwartungen jeder Gruppe
- **Einfluss-Bewertung**: Bestimmung des Einflussgrades und der Beteiligungsformen (RACI)
- **Bedürfnis-Ableitung**: Transformation von Interessen in konkrete, messbare Bedürfnisse
- **Anforderungs-Formulierung**: Entwicklung formeller Anforderungen basierend auf Stakeholder-Bedürfnissen

### 1.5 Definitionen (Stakeholder-bezogen)
- **Kern-Stakeholder**: Direkte Nutzer des Systems (Studierende, Lehrende)
- **Operative Stakeholder**: Organisationen, die das System einsetzen (Hochschulen, Projektpartner)
- **Regulatorische Stakeholder**: Instanzen mit rechtlicher/regulatorischer Autorität (BMBF, Datenschutzbeauftragte)
- **Technische Stakeholder**: Gruppen mit technischer Verantwortung (IT-Administration, Entwicklerteams)
- **Indirekte Stakeholder**: Gruppen, die vom System beeinflusst werden, aber nicht direkt nutzen (Community, Didaktikzentren)
- **RACI-Matrix**: Responsibility (Verantwortlich), Accountable (Rechenschaftspflichtig), Consulted (Konsultiert), Informed (Informiert)
### 1.6 Stakeholder-Übersicht
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
- ISO/IEC/IEEE 29148:2018
- governance/Requirements-Management-Plan.md
- srs/SRS.md
- traceability/RTM.csv
- Richtlinie zur Bund-Länder-Initiative zur Förderung der KI in der Hochschulbildung
- DSGVO

## 3. Anforderungen an das Geschäftsmanagement
### 3.1 Geschäftsumfeld
Das HASKI-System operiert im Hochschulbildungsbereich mit Fokus auf technische Studiengänge (Informatik, Software Engineering, Game Engineering). Das System soll fach- und institutsübergreifend an Hochschulen einsetzbar sein.

### 3.2 Stakeholder-Mission und -Ziele
**Mission**: Erfüllung der vielfältigen Bedürfnisse aller Stakeholder-Gruppen im Kontext adaptiver, KI-gestützter Hochschullehre
**Primäre Stakeholder-Ziele**: 
- **Studierende**: Personalisierte, selbstgesteuerte Lernunterstützung und transparentes Feedback
- **Lehrende**: Effiziente Bewertungsunterstützung und aussagekräftige Lernfortschritt-Reports
- **Hochschulen**: Qualitätssteigerung der Lehre und Effizienzgewinn
- **Datenschutzbeauftragte**: DSGVO-konforme Datenverarbeitung und Transparenz
- **IT-Administration**: Stabile Integration und wartbare Systemarchitektur

### 3.3 Geschäftsmodell
Open Science Ansatz - das System soll allen Hochschullehrenden fach- und institutsübergreifend zur Verfügung gestellt werden. Keine kommerzielle Verwertung geplant.

### 3.4 Informationsumfeld
Integration in bestehende LMS (primär Moodle), Datenaustausch über LTI-Standard, Compliance mit Datenschutzbestimmungen.

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

## 5. Stakeholder-Bedürfnisse und -Anforderungen
### 5.1 Stakeholder-Bedürfnisse (informell)

#### Studierende (STK-01)
- **NEED-101**: Zugang zu individuell zugeschnittenen Lernpfaden basierend auf Lernstil, Interessen und Kompetenzen
- **NEED-102**: Möglichkeit, den Lernprozess entweder adaptiv vom System oder selbstgesteuert zu gestalten
- **NEED-103**: Direkte, transparente und verständliche Rückmeldungen zu Aufgabenlösungen
- **NEED-104**: Wahrung der informationellen Selbstbestimmung bei der Datennutzung (Einwilligung, Transparenz)
- **NEED-105**: Stabile Verfügbarkeit der Plattform während Vorlesungszeiten und Prüfungsphasen
- **NEED-106**: Zugang zu hochwertigen, didaktisch aufbereiteten Lehrvideos und animierte, interaktive Lerninhalten
- **NEED-107**: Unterstützung für Micro-Learning durch atomare, kombinierbare "Wissenshappen"

#### Lehrende (STK-02)
- **NEED-108**: Unterstützung bei der Bewertung durch automatisierte Analyse von Quiz, Freitexten, Programmieraufgaben und Diagrammen
- **NEED-109**: Aussagekräftige Reports über Lernfortschritte, Schwierigkeiten und Kompetenzentwicklung der Studierenden
- **NEED-110**: Möglichkeit, Lernräume mit scaffolding-Elementen flexibel zu konfigurieren
- **NEED-111**: Frühzeitige Prototypen für Tests im realen Lehrbetrieb
- **NEED-112**: Unterstützung bei der Erstellung professionell animierter Lehrvideos
- **NEED-113**: Verfügbarkeit von technischem Equipment zur Erstellung hochwertiger, didaktisch aufbereiteter Lehrvideos
- **NEED-114**: Iterative Systemverbesserung durch 7 Entwicklungszyklen
- **NEED-115**: Unterstützung bei der Konzeption von Lernräumen für kollaborative Problemlösung

#### Hochschulleitungen (STK-03)
- **NEED-116**: Nachweisbare Verbesserung der Lehrqualität durch wissenschaftlich fundierte Evaluation
- **NEED-117**: Open Source Verfügbarkeit der Software und Lehrmaterialien für institutionelle Nutzung

#### Datenschutzbeauftragte (STK-04)
- **NEED-118**: DSGVO-konforme Erhebung, Verarbeitung und Speicherung personenbezogener Daten
- **NEED-119**: Transparente Dokumentation der Datenverwendung und Einwilligungsprozesse
- **NEED-120**: Technische Verfahren zur Anonymisierung und Pseudonymisierung der Lern- und Nutzungsdaten

#### IT-Administration (STK-05)
- **NEED-121**: Kompatibilität mit bestehenden Learning Management Systemen (vorrangig Moodle, via LTI-Schnittstellen)
- **NEED-122**: Klare technische Dokumentation zur Systemintegration und Wartung
- **NEED-123**: Zugang zu KI-Workstations mit ausreichend Prozessor- und Speicherkapazität

#### Projektförderer (STK-07)
- **NEED-124**: Termingerechte Umsetzung aller Meilensteine innerhalb der Projektlaufzeit (2022–2025)
- **NEED-125**: Nachvollziehbare Berichterstattung über Projektfortschritte und Mittelverwendung
- **NEED-126**: Nachweis der Dissemination durch Publikationen, Konferenzen und Workshops
- **NEED-127**: Konzept für nachhaltige Weiternutzung nach Ende der Förderung

#### Wissenschaftliche Mitarbeiter (STK-11)
- **NEED-128**: Zugang zu modernen KI-Entwicklungstools und -bibliotheken für die Implementierung
- **NEED-129**: Iterative Entwicklungsmöglichkeiten mit regelmäßigen Feedback-Zyklen

#### Didaktikzentren & Community (STK-06, STK-14)
- **NEED-130**: Transferierbare didaktische Konzepte, die auch außerhalb der Informatik eingesetzt werden können
- **NEED-131**: Bereitstellung von Workshops und Best-Practice-Beispielen für Lehrende
- **NEED-132**: Wissenschaftlicher Austausch über Ergebnisse, Methoden und Evaluationsdaten

### 5.2 Stakeholder-Anforderungen (formell)
Die detaillierten, formellen Stakeholder-Anforderungen werden in separaten Dokumenten spezifiziert:
- `strs/stakeholder-requirements/StRS-NNN.md` - jeweils eine spezifische Stakeholder-Anforderung
- Jede Anforderung ist eindeutig identifizierbar und auf konkrete Stakeholder-Bedürfnisse rückverfolgbar
- Alle Anforderungen sind in der Requirements Traceability Matrix (RTM) dokumentiert

**Kategorien der Stakeholder-Anforderungen:**
- **Funktionale Anforderungen**: Spezifische Funktionen für verschiedene Stakeholder-Gruppen
- **Qualitätsanforderungen**: Performance, Usability, Sicherheit aus Stakeholder-Sicht
- **Schnittstellenanforderungen**: Integration und Kompatibilität mit bestehenden Systemen
- **Compliance-Anforderungen**: Rechtliche und regulatorische Vorgaben

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
  
# 8.2 Referenzen
- ISO/IEC/IEEE 29148:2018

## 9 Traceability
- Bidirektionale Nachverfolgbarkeit Stakeholder → Anforderungen: siehe traceability/RTM.csv

## Ermittlung & Validierung
**Verwendete Methoden**: 
- Systematisches Literaturreview zu adaptiven Lernumgebungen
- Grounded-Theory-Methodologie für Evaluationen
- Befragungen und Beobachtungen der Nutzerinteraktionen

**Review-/Abnahmeprozess**: Iterative Evaluationen mit Studierenden und Lehrenden, Abstimmung mit Datenschutzbeauftragten, wissenschaftliche Begutachtung durch Projektbeirat

**Status**: In Entwicklung (Projektlaufzeit 1.1.2022-31.12.2025)