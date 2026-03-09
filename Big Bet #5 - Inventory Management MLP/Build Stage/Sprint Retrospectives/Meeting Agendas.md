# Sprint Meeting Agendas

This document defines the standard meeting structures for the Inventory Management System sprint team.

---

## 1. Weekly Sprint Check-in (30 minutes)

**Purpose:** Track sprint progress, share demos, and identify blockers

**Attendees:** Required for all (Dev, QA, Design, PM)

**Frequency:** Weekly

### Agenda with Timeboxes

| Time | Topic | Description |
|------|-------|-------------|
| 0-5 min | Round-robin Progress Updates | Each team member shares: what's completed, what's in progress, Done Dev status |
| 5-20 min | Live Demos & Visual Walkthroughs | Show work completed even if not fully complete. Focus on visual progress, alignment with Figma designs |
| 20-25 min | Blockers & Dependencies | Identify blockers, dependencies on other teams, deployment/release concerns |
| 25-28 min | Next Week Look-ahead | Quick preview of upcoming priorities and work distribution |
| 28-30 min | Feedback Capture | Note any items for retrospective or decision meeting |

### Meeting Rules
- **Strict timebox enforcement** - designated timekeeper rotates each meeting
- **Focus on visual progress** - demos over status updates
- **No deadline justification discussions** - quality over timeline explanations
- **Decisions get deferred** - capture for Decision Meeting, don't solve in real-time
- **Cameras on** for engagement
- **Agenda sent 24 hours in advance** with specific demo topics

### Success Criteria
- All team members see visual progress of sprint work
- Blockers are identified and next steps assigned
- Team has shared understanding of sprint health
- Meeting ends on time

---

## 2. Weekly Decision Meeting (30 minutes)

**Purpose:** Document and align on technical and product decisions made during the sprint to ensure shared understanding and prevent testing/implementation confusion

**Attendees:** Required for all (Dev, QA, Design, PM)

**Frequency:** Weekly

### Why This Meeting Exists
Based on Sprint Retro feedback, this meeting addresses:
- Critical conversations about flows and triggers were only communicated verbally
- QA discovered changed behaviors during testing that weren't documented
- Team needed "meetings on meetings" to explain why things work a certain way
- PRD/requirements changed mid-sprint without documentation updates

### Agenda with Timeboxes

| Time | Topic | Description |
|------|-------|-------------|
| 0-3 min | Review Decision Log | Quick scan of Slack canvas for decisions needing discussion |
| 3-25 min | Decision Discussion & Alignment | Timebox 5-7 min per decision. Cover: What decision? Options? Impact on sprint/testing/deployment? Final decision + rationale |
| 25-30 min | Update and Document Decisions | Real-time documentation of any new decisions made during meeting in Slack canvas with template format |

### Decision Documentation Template
For each decision, capture:
```
**Date:** [Date]
**Decision:** [What was decided]
**Context:** [Why this decision was needed]
**Options Considered:** [Alternatives discussed]
**Final Decision:** [What we're doing]
**Rationale:** [Why we chose this]
**Impact:** [How this affects testing/deployment/other work]
**Owner:** [Who implements/owns this]
```

### What Gets Discussed
1. **Technical decisions** - implementation approaches, architecture choices, workarounds
2. **Flow/trigger changes** - any behavior changes from original requirements
3. **Requirement clarifications** - scope changes, PRD updates, feature adjustments
4. **Design deviations** - when implementation differs from Figma
5. **Testing implications** - how decisions affect QA test plans

### Meeting Rules
- **Pre-populate Slack canvas** - no ad-hoc topics, items must be added before meeting
- **One decision at a time** - complete documentation before moving to next
- **Park complex topics** - if decision needs >7 min, schedule separate deep-dive
- **All decisions documented** - no verbal-only agreements
- **Transfer to Confluence weekly** - permanent record maintained

### Success Criteria
- All sprint decisions captured with rationale
- QA knows about behavior changes before testing
- Team has shared understanding of "why things work this way"
- PRD/documentation updates identified when requirements change

---

## 3. Bi-Weekly Sprint Retrospective (60 minutes)

**Purpose:** Reflect on sprint performance and identify improvements

**Attendees:** Required for all (Dev, QA, Design, PM)

**Frequency:** Every 2 weeks (company minimum standard)

### Agenda with Timeboxes

| Time | Topic | Description |
|------|-------|-------------|
| 0-5 min | Retro Intro & Previous Action Items Review | Review status of action items from previous retro - what was completed, what's in progress |
| 5-10 min | Silent Individual Brainstorming | Each person adds sticky notes to retro board: What Went Well, To Improve |
| 10-55 min | Discuss All Tickets & Generate/Prioritize Action Items | Group similar items, discuss What Went Well and To Improve together. Identify challenges without blame, generate 5-7 actionable improvements, assign owners and success criteria |
| 55-60 min | Key Takeaways Summary & Meeting Close | Synthesize retrospective themes and focus for next sprint |

### Action Item Format (SMART)
Each action item must include:
- **Specific:** Clear description of what needs to be done
- **Measurable:** How we'll know it's complete
- **Assignable:** Named owner responsible
- **Realistic:** Achievable within timeframe
- **Time-bound:** Due date or sprint deadline

Example:
```
Action: Create decision log on Confluence
Owner: John
Success Criteria: Confluence page created with template, team trained on usage
Due Date: Before next sprint starts
Status: In Progress
```

### Meeting Rules
- **Use collaborative tool** - Miro, FigJam, or similar for sticky notes
- **Psychological safety** - no blame, focus on processes not people
- **Timebox discussions** - move lengthy topics to separate follow-ups
- **Limit action items** - max 5-7 actionable items (quality over quantity)
- **Document within 24 hours** - retro writeup shared with team next day
- **Track action items** - review progress in next retro for accountability

### Retro Documentation
Following the Sprint Retrospective Writing Guide, document:
1. Sprint Overview - context, team composition, key objectives
2. What Went Well - successes with specific examples
3. Areas for Improvement - challenges with impacts
4. Action Items - SMART items with owners
5. Key Takeaways - 2-4 sentence synthesis

### Success Criteria
- Team feels heard and able to share feedback openly
- Root causes of issues identified, not just symptoms
- Actionable improvements defined with clear owners
- Previous action items reviewed for accountability
- Retro documentation published within 24 hours

---

## General Meeting Guidelines

### For All Meetings

1. **Clear agenda sent 24 hours in advance** with specific topics and timeboxes
2. **Designated timekeeper** rotates each meeting to enforce timeboxes
3. **Parking lot** maintained for off-topic items that arise during discussion
4. **Action items captured live** with owner and due date
5. **Hard stop at scheduled end time** - incomplete items get scheduled separately
6. **Meeting notes** documented using standardized templates

### Meeting Hygiene

- **Start on time, end on time** - respect everyone's calendar
- **One conversation at a time** - no side discussions
- **Cameras on** for engagement and connection
- **Mute when not speaking** to reduce background noise
- **Come prepared** - review materials/agenda beforehand
- **No multitasking** - full attention on meeting

### Escalation Process

If a meeting consistently:
- Runs over time
- Lacks clear outcomes
- Has low attendance
- Doesn't follow agenda

**Action:** Raise in next retrospective for team to address collectively.

---

## Meeting Calendar Template

### Recommended Weekly Cadence

| Day | Meeting | Duration | Purpose |
|-----|---------|----------|---------|
| Monday | Sprint Check-in | 30 min | Progress, demos, blockers |
| Wednesday | Decision Meeting | 30 min | Document decisions, align on changes |
| Every 2 weeks (Friday) | Sprint Retrospective | 60-90 min | Reflect and improve |

*Adjust days based on team availability and sprint schedule*

---

**Document Owner:** Product Management
**Last Updated:** Nov 25, 2025
**Next Review:** After 3 sprint cycles to assess effectiveness
