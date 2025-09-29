# Verification Plan
## Konformität
Dieses Dokument orientiert sich nach ISO/IEC/IEEE 29148 (Anforderungen & Verifikation) und sekundär an ISO/IEC/IEEE 15289. Es erhebt keine Ansprüche auf Vollständigkeit.

## Scope und Geltungsbereich
In Scope sind alle `shall`-Anforderungen aus den Dokumenten [SyRS](../syrs/SyRS.md) und [StRS](../strs/StRS.md). Out of Scope sind optionale Wünsche oder Ideen.

## Referenzen
- [SyRS](../syrs/SyRS.md)
- [StRS](../strs/StRS.md)
- [Risikomanagement Plan](../governance/Risk-Management-Plan.md)
- [Projektplan](../governance/Project-Plan.md)
- 
## Zielbild
- Wozu? Nachweisen, dass jede Anforderung aus den Dokumenten [SyRS](../syrs/SyRS.md) und [StRS](../strs/StRS.md) erfüllt ist.
- Wie? Jedem Requirement ist mind. eine Verifikationsmethode zugeordnet: Inspektion/Review, Analyse, Demonstration, Test.
- 
## Verifikationsmethoden
- **Inspektion/Review**: Dokumentation, Konfiguration, Pläne, Diagramme.
- **Analyse**: Statische Analysen (SonarCloud), Architektur-Nachweise, Performance-Berechnungen.
- **Demonstration**: Einsetzbare, isolierte Software-Artefakte auf GitHub.
- **Test**: Reproduzierbare, messbare Tests mit klaren Akzeptanzkriterien.
- 
## Verifikationsergebnisse und Reportung
Alle Testergebnisse werden in CI/CD-Artefakten (GitHub Actions) dokumentiert und sind öffentlich einsehbar (siehe [GitHub](https://github.com/HASKI-RAK)). Wir verzichten deshalb auf einen separaten Verifikationsbericht.

## Testebenen und -arten
Ebenen: Unit, Komponenten, Integration, End-To-End, Abnahmetests im Rahmen der Evaluationen.
Arten: Funktional, Nicht-funktional (Performance, Sicherheit, Usability).

## Rollen und Unabhängigkeit
Tests werden in der Regel von Entwicklern geschrieben, welche das zugehörige Feature implementiert haben. Wir garantieren Unabhängigkeit durch Peer-Reviews und automatisierte Testausführung in CI/CD-Pipelines.
> **Anmerkung**: Seit der Einführung von AI auf GitHub, werden unsere Reviews zudem von AI-Tools wie Copilot unterstützt.

## Testumgebung
Tests werden in isolierten Umgebungen ausgeführt. Unit-Tests und Integrationstests laufen einerseits lokal, andererseits in CI/CD-Pipelines. Durch Docker stellen wir eine konsistente Umgebung sicher. Statische Analysen werden durch SonarCloud auf GitHub durchgeführt. Lokale Erweiterungen (SonarCube) in den Entwicklungsumgebungen unterstützen Entwickler zusätzlich.

## Traceability
- [RTM](../rtm/RTM.csv) verknüpft Anforderungen mit Überprüfungen. Automatisch generiert.

## Akzeptanzkriterien
<!-- //TODO: Quoten für Testabdeckung, Anzahl bestandener Tests, etc. -->

## Werkzeuge und Automatisierung
- **Test-Frameworks**: Jest, React Testing Library, Pytest.
- **CI/CD**: GitHub Actions.
- **Statische Analyse**: SonarCloud.
- **Containerisierung**: Docker.
- **Metriken-Export**: Traceability [Script](../traceability/build.py), Konfiguration in der `package.json`, pytest konfiguration und toml.