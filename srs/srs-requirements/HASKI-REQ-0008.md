---
id: HASKI-REQ-0008
title: Wahlmöglichkeit zwischen adaptiven und selbstgesteuerten Lernpfaden
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Demonstration
source_id: SyRS-FUNC-002
links:
  parents: ["SyRS-FUNC-002"]
  stories:
    [
      "HASKI-RAK/HASKI-Frontend#308",
      "HASKI-RAK/HASKI-Frontend#353",
      "HASKI-RAK/HASKI-Frontend#362",
      "HASKI-RAK/HASKI-Backend#83",
      "HASKI-RAK/HASKI-Backend#93",
      "HASKI-RAK/HASKI-Backend#24",
    ]
  tests:
    - path: "frontend/src/components/AlgorithmSettingsModal/AlgorithmSettingsModal.test.tsx"
      name: "AlgorithmSettingsModal"
---

## Beschreibung

Das HASKI-System **shall** den Studierenden die Möglichkeit bieten, zwischen einem adaptiven Lernmodus (systemgesteuerte Empfehlungen basierend auf ILS und Lernverhalten) und einem selbstgesteuerten Lernmodus (freie Wahl der Lernressourcen ohne Systemvorgaben) zu wählen. Die Wahl **shall** jederzeit vom Studierenden geändert werden können.

## Akzeptanzkriterien

### Modus-Auswahl und Konfiguration

- [x] System bietet die Wahl die vorgegebenen Lernpfade zu befolfen oder diese selbstgesteuert zu erkunden
- [x] Die Auswahl ist für Studierende leicht zugänglich (z.B. in Benutzereinstellungen oder Dashboard)
- [x] Studierende können ihr Vorgehen jederzeit ändern ohne Datenverlust

### Adaptiver Lernpad (Systemgesteuert)

- [x] System generiert automatisch Lernpfad-Empfehlungen basierend auf ILS-Ergebnissen
- [x] Lernressourcen werden nach Lernstil, Kompetenz und Fortschritt priorisiert
- [x] System zeigt empfohlene "nächste Schritte" im Lernpfad an
- [x] Adaptive Algorithmen beeinflussen die Reihenfolge und Auswahl der Lerninhalte

### Selbstgesteuerte Nutzung des Systems (Nutzerkontrolliert)

- [x] Alle verfügbaren Lernressourcen sind ohne Priorisierung zugänglich
- [x] Studierende können frei durch Topics und Learning Elements navigieren
- [x] Fortschrittsanzeige bleibt verfügbar, aber ohne prescriptive Empfehlungen

### Benutzererfahrung und Transparenz

- [x] Nutzer werden von der Möglichkeit in kenntniss gesetzt, den adaptiven Lernpfad zu befolgen oder das System selbstgesteuert zu bedienen
- [x] Hilfe-Funktion erklärt die Nutzung des Systems in kürze

### Datenintegrität und Kompatibilität

- [x] ILS-Fragebogen ergebnisse werdern für die adaptiven Lernpfade berücksichtigt
- [x] Lernfortschritt wird unabhängig vom Lernverhalten korrekt erfasst
- [x] xAPI-Statements werden unabhängig vom Lernverhalten gleichermaßen generiert
- [x] Daten sind konsistent unabhängig von der befolgung des Lernpfads (adaptiv vs selbstgesteuert)
- [x] Bereits absolvierte Inhalte bleiben markiert

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
