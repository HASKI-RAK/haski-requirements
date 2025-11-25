---
id: SyRS-FUNC-012
title: Frontend-Web-Vitals zentral erfassen
type: Functional
status: Proposed
stakeholder_priority: Medium
verification_method: Test
links:
  parents: [StRS-134]
  children: ["HASKI-REQ-0045"]
---

## Beschreibung
Das System **shall** einen abgesicherten Backend-Endpunkt bereitstellen, der Web-Vitals-Messwerte aus dem HASKI-Frontend entgegennimmt, validiert und für Administrationszwecke persistiert. Der Endpunkt **shall** ausschließlich bekannte Metriken (FCP, TTFB, CLS, LCP, FID, INP) akzeptieren, Eingaben strukturieren (Name, Wert, Rating, Delta, Navigationstyp, Einträge) und fehlerhafte Nutzlasten deterministisch ablehnen. Administrierende **shall** die erfassten Logs über ein dediziertes Abfrage-Interface abrufen können, um Performance-Regressionen und Vorfälle nachvollziehen zu können.
