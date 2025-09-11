# Systemanforderungsspezifikation (SyRS) – HASKI

## 1. Einleitung

### 1.1 Systemzweck
HASKI ist ein KI-gestütztes Assistenzsystem, das Studierende in Blended-Learning-Umgebungen durch individuelles Feedback, Lernpfadanpassungen und Micro-Learning-Einheiten unterstützt. Lehrende erhalten Unterstützung bei der Erstellung von Kursmaterialien sowie bei der Evaluation des Lernfortschritts.

### 1.2 Systemabgrenzung (Scope)
- Integration in das bestehende Learning Management System (Moodle).  
- Einsatz im Hochschulkontext zur Unterstützung digitaler Lehr-Lern-Szenarien.  
- Fokussiert auf individualisiertes Lernen, Feedbackgenerierung und didaktische Optimierung.  
- Kein Ersatz für bestehende LMS-Funktionalitäten, sondern Erweiterung.  

### 1.3 Systemübersicht

#### 1.3.1 Systemkontext
- Eingebettet in Moodle (Zugang über Webbrowser, PC, Tablet, Smartphone).  
- Anbindung an hochschulinterne Systeme für Nutzerverwaltung und Lernmaterialien.  

#### 1.3.2 Systemfunktionen
- Analyse des Lernverhaltens und -fortschritts.  
- Generierung von Feedback und Lernempfehlungen.  
- Unterstützung bei der Erstellung und Strukturierung von Lerninhalten.  
- Automatisierte Berichte für Lehrende.  

#### 1.3.3 Nutzermerkmale
- **Studierende**: heterogene Vorkenntnisse, flexible Nutzung (orts- und zeitunabhängig).  
- **Lehrende**: Fachdidaktisches Wissen, Bedarf an Unterstützung in Content-Erstellung und Analyse.  
- **Administratoren**: Technische Betreuung, Systemintegration.  

### 1.4 Begriffsdefinitionen
- **LMS**: Learning Management System, hier Moodle.  
- **Blended Learning**: Kombination aus Präsenz- und Online-Lernen.  
- **Micro-Learning**: Kurze, flexible Lerneinheiten.  
- **KI**: Künstliche Intelligenz, insbesondere für Analyse und Feedback.  

---

## 2. Referenzen
- Projektbeschreibung HASKI  
- Teilvorhabenbeschreibung HASKI-KE  
- Arbeitsprogramm HASKI  
- ISO/IEC/IEEE 29148:2018  

---

## 3. Systemanforderungen

### 3.1 Funktionale Anforderungen
- Das System soll Lernpfade adaptiv anpassen.  
- Das System soll individuelles Feedback für Studierende bereitstellen.  
- Das System soll Lehrenden Unterstützung bei Content-Erstellung bieten.  
- Das System soll automatisierte Berichte über Lernfortschritte erzeugen.  

### 3.2 Benutzbarkeitsanforderungen (Usability)
- Intuitive Einbindung in Moodle-Oberfläche.  
- Mobile Nutzbarkeit (Responsive Design).  
- Niedrige Einstiegshürden für Studierende und Lehrende.  

### 3.3 Leistungsanforderungen (Performance)
- Verarbeitung von Lernaktivitätsdaten in nahezu Echtzeit.  
- Antwortzeiten für Feedbackgenerierung < 5 Sekunden (Richtwert).  
- Skalierbarkeit für große Nutzergruppen (>1000 Studierende pro Kurs).  

### 3.4 Schnittstellenanforderungen

#### 3.4.1 Externe Schnittstellenanforderungen
- Integration in Moodle via Plug-in/Schnittstelle.  
- Nutzung von Authentifizierungs- und Nutzerverwaltungssystemen der Hochschule.  

#### 3.4.2 Interne Schnittstellenanforderungen
- Datenbankanbindung für Lernhistorien.  
- Schnittstellen zwischen Analysekomponenten (KI) und Feedbackmodul.  

### 3.5 Systembetrieb
- Bereitstellung als Webanwendung innerhalb Moodle.  
- Zugriff durch Browser auf Endgeräten (PC, Tablet, Smartphone).  

### 3.6 Systemmodi und -zustände
- **Normalbetrieb**: Standardnutzung durch Studierende und Lehrende.  
- **Trainingsmodus**: Anpassung/Training der KI-Modelle.  
- **Wartungsmodus**: Systemupdates, Bugfixes, Anpassungen.  

### 3.8 Umgebungsbedingungen
- Betrieb auf hochschulischen Servern/Cloud-Infrastruktur.  
- Abhängigkeit von Internetzugang und LMS-Verfügbarkeit.  

### 3.9 Sicherheitsanforderungen
- Einhaltung von Datenschutzrichtlinien (DSGVO).  
- Zugriff nur über hochschulinterne Authentifizierung.  
- Verschlüsselte Datenübertragung (TLS/HTTPS).  

### 3.10 Informations- und Datenmanagementanforderungen
- Speicherung von Lernfortschrittsdaten pseudonymisiert.  
- Protokollierung von Systemnutzung für Evaluation.  
- Export von Berichten für Lehrende (z. B. PDF).  

### 3.11 Richtlinien- und Regulierungsvorgaben
- Einhaltung hochschulischer IT-Richtlinien.  
- Berücksichtigung von Datenschutz- und Urheberrechtsvorgaben.  

### 3.12 Anforderungen an die Systemnutzung im Lebenszyklus
- Regelmäßige Updates und Anpassungen an Moodle-Versionen.  
- Erweiterbarkeit für neue Module und Funktionen.  
- Support und Dokumentation für Lehrende und Admins.  

---

## 4. Verifikation
- Anforderungen werden durch Tests, Reviews und Pilotanwendungen überprüft.  
- Beispiele: Usability-Tests mit Studierenden, Integrationstests mit Moodle, Performance-Tests.  

---

## 5. Anhänge

### 5.1 Annahmen und Abhängigkeiten
- Abhängigkeit von der Verfügbarkeit und Weiterentwicklung von Moodle.  
- Abhängigkeit von hochschulischer IT-Infrastruktur (Server, Netzwerke).  
- Nutzerakzeptanz als kritischer Erfolgsfaktor.  

### 5.2 Abkürzungen und Begriffe
- LMS: Learning Management System  
- KI: Künstliche Intelligenz  
- DSGVO: Datenschutz-Grundverordnung  
