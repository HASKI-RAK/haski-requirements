# HASKI Requirements — Tailoring
Standards: ISO/IEC/IEEE 29148 (SRS), 29119-3 (Tests), 15289 (Info Items)
Abweichungen: [kurz]
ID-Schema: HASKI-REQ-####; Klassen: SYS, SW, NFR, IF
Attribute: id, title, rationale, source, verification_method, priority, status, owner
GitHub-Konventionen:
- Story-Issues: label=story, field `satisfies: [HASKI-REQ-0001,…]`
- Tests: tag `verifies=HASKI-REQ-0001`
RTM: script `traceability/build.py` erzeugt RTM.csv aus Markdown/YAML+Repo-Metadaten
