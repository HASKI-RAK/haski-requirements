---
id: HASKI-REQ-0009
title: Wahlmöglichkeit zwischen adaptiven und selbstgesteuerten Lernpfaden
type: Functional
status: Proposed
stakeholder_priority: High
verification_method: Demonstration
source_id: SyRS-FUNC-002
links:
  parents: [SyRS-FUNC-002]
  stories: [GH-308, GH-353, GH-362, GH-83, GH-93, GH-24]
---

## Beschreibung

Das HASKI-System **shall** den Studierenden die Möglichkeit bieten, zwischen einem adaptiven Lernmodus (systemgesteuerte Empfehlungen basierend auf ILS und Lernverhalten) und einem selbstgesteuerten Lernmodus (freie Wahl der Lernressourcen ohne Systemvorgaben) zu wählen. Die Wahl **shall** jederzeit vom Studierenden geändert werden können.

## Akzeptanzkriterien

### Modus-Auswahl und Konfiguration
- [ ] System bietet eine Einstellung zur Wahl zwischen "Adaptiver Modus" und "Selbstgesteuerter Modus"
- [ ] Die Auswahl ist für Studierende leicht zugänglich (z.B. in Benutzereinstellungen oder Dashboard)
- [ ] Die Modus-Auswahl ist persistent gespeichert und bleibt über Sessions hinweg erhalten
- [ ] Studierende können den Modus jederzeit wechseln ohne Datenverlust
- [ ] Bei Moduswechsel wird der Studierende über die Konsequenzen informiert

### Adaptiver Modus (Systemgesteuert)
- [ ] System generiert automatisch Lernpfad-Empfehlungen basierend auf ILS-Ergebnissen
- [ ] Lernressourcen werden nach Lernstil, Kompetenz und Fortschritt priorisiert
- [ ] System zeigt empfohlene "nächste Schritte" im Lernpfad an
- [ ] Adaptive Algorithmen beeinflussen die Reihenfolge und Auswahl der Lerninhalte
- [ ] Studierende sehen Hinweise, warum bestimmte Inhalte empfohlen werden

### Selbstgesteuerter Modus (Nutzerkontrolliert)
- [ ] Alle verfügbaren Lernressourcen sind ohne Priorisierung zugänglich
- [ ] Keine systemgenerierten Empfehlungen oder "nächste Schritte" werden angezeigt
- [ ] Studierende können frei durch Topics und Learning Elements navigieren
- [ ] Suchfunktion und Filter ermöglichen eigenständiges Auffinden von Inhalten
- [ ] Fortschrittsanzeige bleibt verfügbar, aber ohne prescriptive Empfehlungen

### Benutzererfahrung und Transparenz
- [ ] Beim ersten Login wird der Unterschied zwischen den Modi klar erklärt
- [ ] System zeigt an, welcher Modus aktuell aktiv ist
- [ ] Hilfe-Funktion erklärt die Vor- und Nachteile beider Modi
- [ ] UI passt sich an den gewählten Modus an (z.B. Hervorhebung von Empfehlungen im adaptiven Modus)
- [ ] Wechsel zwischen Modi ist intuitiv und mit maximal 2 Klicks möglich

### Datenintegrität und Kompatibilität
- [ ] ILS-Fragebogen wird in beiden Modi erfasst (optional im selbstgesteuerten Modus)
- [ ] Lernfortschritt wird unabhängig vom Modus korrekt erfasst
- [ ] xAPI-Statements werden in beiden Modi gleichermaßen generiert
- [ ] Wechsel zwischen Modi führt nicht zu inkonsistenten Daten
- [ ] Bereits absolvierte Inhalte bleiben markiert, unabhängig vom Modus

## Rationale

Basierend auf Stakeholder-Anforderung StRS-102 benötigen Studierende die Wahlfreiheit zwischen adaptivem und selbstgesteuertem Lernen, um:
- Unterschiedliche Lernstile und Präferenzen zu unterstützen
- Die Autonomie und Selbstbestimmung der Studierenden zu stärken
- Die Akzeptanz des Systems zu erhöhen (nicht alle Studierenden bevorzugen systemgesteuerte Empfehlungen)
- Überforderung im selbstgesteuerten Modus durch optionale Systemunterstützung zu vermeiden
- Flexibilität je nach Lernkontext zu ermöglichen (z.B. strukturierte Unterstützung bei neuen Themen, freie Erkundung bei bekannten Inhalten)

Die Implementierung dieses Features ist essentiell, da:
- Forschung zeigt, dass verschiedene Lernende unterschiedliche Grade an Leitungsunterstützung bevorzugen
- Erzwungene Systemsteuerung kann zu Reaktanz und reduzierter Motivation führen
- Selbstgesteuerte Optionen die wahrgenommene Kontrolle und intrinsische Motivation erhöhen
- Die Kombination beider Modi maximale Flexibilität bietet

## Hinweise

- **Status**: Keine implementierenden GitHub Issues gefunden - dieses Feature scheint noch nicht umgesetzt zu sein
- **Implementierungsempfehlungen**:
  - Modus-Einstellung sollte im User-Profil/Settings gespeichert werden
  - UI-Komponenten sollten conditional rendering basierend auf Modus verwenden
  - Backend-API sollte Modus-Parameter bei Lernpfad-Requests berücksichtigen
  - Empfohlener Standardmodus: Adaptiv (mit klarer Option zum Wechsel)
  - Consider A/B-Testing zur Optimierung der Modus-Auswahl-UI
- **Verwandte Anforderungen**:
  - HASKI-REQ-0007: Automatische Lernpfad-Anpassung (wird im adaptiven Modus genutzt)
  - Zukünftige Anforderungen könnten "Hybrid-Modus" spezifizieren (adaptive Empfehlungen + manuelle Override-Möglichkeit)
- **UX-Überlegungen**:
  - Klare Visualisierung des aktiven Modus (z.B. Toggle-Switch, Mode-Indicator)
  - Onboarding sollte Vorteile beider Modi erklären
  - Analytics sollten Modus-Nutzung tracken für zukünftige Optimierungen
- **Technische Abhängigkeiten**:
  - User Settings Management System
  - Conditional UI rendering framework
  - Lernpfad-Algorithmus muss Modus-Parameter unterstützen
