---
id: HASKI-REQ-0030
title: System Availability During Lecture and Exam Periods
type: NFR:Performance
status: Approved
source_id: SyRS-PERF-001
verification_method: Analysis
links:
  parents: [SyRS-PERF-001]
---

## Beschreibung

The HASKI system **shall** maintain a minimum availability of 99% during lecture and exam periods.

## Akzeptanzkriterien

- [ ] System uptime is monitored and logged continuously
- [ ] Availability metrics are calculated and reported for lecture periods
- [ ] Availability metrics are calculated and reported for exam periods
- [ ] System achieves ≥ 99% availability during defined lecture periods
- [ ] System achieves ≥ 99% availability during defined exam periods
- [ ] Planned maintenance is scheduled outside of lecture and exam periods
- [ ] Incident response procedures are in place to minimize downtime
- [ ] System health checks are automated and monitored
- [ ] Alerting mechanisms are configured for availability issues
- [ ] Availability reports are generated and reviewed after each period

## Rationale

Derived from system requirement SyRS-PERF-001 and stakeholder requirement StRS-105.

High availability is critical for student acceptance and learning continuity, especially during exam periods. System interruptions would disrupt learning processes and undermine trust in the platform. This requirement ensures that the infrastructure, deployment practices, and operational procedures support reliable access to the HASKI learning system during the most critical academic periods.

## Hinweise

- This is a system-level non-functional requirement addressing operational reliability
- Implementation involves infrastructure configuration, deployment practices, monitoring, and incident management
- Lecture and exam periods should be defined based on the academic calendar of participating institutions
- Availability calculation excludes planned maintenance windows that are scheduled outside critical periods
- Related infrastructure considerations: Docker deployment, health checks, load balancing, backup systems
- Verification through operational monitoring and reporting during pilot and production phases
