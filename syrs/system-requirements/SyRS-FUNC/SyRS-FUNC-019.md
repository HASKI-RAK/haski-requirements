---
id: SyRS-FUNC-019
title: Navigation im MainFrame bereitstellen
type: Functional
status: Implemented
stakeholder_priority: High
verification_method: Test
links:
  parents: [StRS-139]
  children: ["HASKI-REQ-0088"]
---

## Beschreibung

Das System **shall** innerhalb des MainFrame-Layouts eine Breadcrumb-Navigation anzeigen, die den aktuellen Routing-Pfad des Frontends spiegelt und anklickbare Rücksprungpunkte bis zur Startseite bietet. Jede Breadcrumb-Stufe **shall** aus den internationalisierten Seitenschlüsseln generiert werden und numerische IDs (z. B. Kurs- oder Topic-IDs) ausblenden, damit die Orientierung textbasiert erfolgt. Navigationsereignisse **shall** den React-Router verwenden, sodass alle Seiten denselben Routing-Stack nutzen und Zustand (z. B. ausgewählter Kurs) erhalten bleibt.
