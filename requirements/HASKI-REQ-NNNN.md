---
id: HASKI-REQ-0000 # Parser working
title: [Kurzname der Anforderung] # No parser effect
type: [Functional | Interface | NFR:Performance | NFR:Security …] # Parser working
source: [Projektbeschreibung §x, AP y, Issue #123] # No parser effect
source_id: [StRS-NNN] # Stakeholder Requirement ID, no parser effect
rationale: [Warum ist diese Anforderung nötig?] # No parser effect
owner: [Verantwortliche Person/Team] # No parser effect
stakeholder_priority: [High | Medium | Low] # No parser effect
status: [Proposed | Approved | Implemented | Verified] # No parser effect
risk: [Low | Medium | High]  # optional nach ISO 16085, no parser effect
difficulty: [Low | Medium | High]  # optional, no parser effect
verification_method: [Test | Review | Analysis | Demonstration] #  No parser effect
links: # No parser effect
  stories: [GH-#123, GH-#456]
  tests: [backend::tc_eval_001, fe:cypress::t_login_01]
  parents: [HASKI-STRS-0003]   # falls abgeleitet, System Test Requirement Specification
  children: []                 # falls weiter verfeinert
version: 1.0
---

## Beschreibung
Die Software **shall** [präzise, messbare Beschreibung der Funktion oder Eigenschaft].  (should: kann (empfohlen, nicht zwingend), may: darf (Möglichkeit, locker), will: wird in Zukunft)
| Wort       | Bedeutung im Standard                            | Verwendung für                  |
| ---------- | ------------------------------------------------ | ------------------------------- |
| **shall**  | zwingend, bindend, verifiziert (Anforderung)     | Pflicht-Anforderungen           |
| **should** | Wunsch, Ziel (empfohlen, aber nicht zwingend)    | Ziele, nicht bindende Vorgaben  |
| **will**   | Tatsache, Zukunftsaussage, Zweck (nicht bindend) | Kontexte, Fakten, Absicht       |
| **may**    | Möglichkeit, Erlaubnis (locker)                  | Optionen, erlaubte Spielräume   |

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
