---
id: HASKI-REQ-XXXX
title: [Kurzname der Anforderung]
type: [Functional | Interface | NFR:Performance | NFR:Security …]
source: [Projektbeschreibung §x, AP y, Issue #123]
rationale: [Warum ist diese Anforderung nötig?]
owner: [Verantwortliche Person/Team]
priority: [High | Medium | Low]
status: [Proposed | Approved | Implemented | Verified]
risk: [Low | Medium | High]  # optional nach ISO 16085
verification_method: [Test | Review | Analysis | Demonstration]
links:
  stories: [GH-#123, GH-#456]
  tests: [backend::tc_eval_001, fe:cypress::t_login_01]
  parents: [HASKI-STRS-0003]   # falls abgeleitet
  children: []                 # falls weiter verfeinert
version: 1.0
---

## Beschreibung
Die Software **shall** [präzise, messbare Beschreibung der Funktion oder Eigenschaft].  
[Keine vagen Begriffe, kein „wie“, nur „was“ – ISO/IEC/IEEE 29148 §5.2.4–5.2.7:contentReference[oaicite:0]{index=0}]

## Bedingungen / Constraints
- [Messbare Bedingung 1]  
- [Randbedingung, gesetzlich/technisch]

## Akzeptanzkriterien
- [objektiv prüfbares Kriterium 1]  
- [objektiv prüfbares Kriterium 2]

## Notizen
- Annahmen: …  
- Abhängigkeiten: …
