# Sprint Retro - Jan 13th 2026

![Retro Visual Jan 13 2026](Retro%20Visual%20Jan%2013%202026.png)

## Sprint Overview

This retrospective was conducted for the Sales Management team following the completion of the MLM Epic 2 bi-weekly sprint, which focused on continuing the Multi-Location Management (MLM) implementation. The sprint experienced a significant shift in release strategy, moving from a phased alpha rollout to a full General Availability (GA) launch scheduled for January 21st, 2026. The team navigated this pivot while maintaining progress on core functionality including UI components, validation logic, and underlying infrastructure improvements. A key technical decision emerged during this sprint regarding the adoption of a Data Access Layer (DAL) approach to address technical debt and enable better event-driven architecture.

## What Went Well 🎯

- **Adaptability to Change:** The team adapted exceptionally well to the new January 21st GA date, pivoting from the originally planned phased rollout. Leadership's clear communication helped reinforce the new direction, and the team responded without panic despite the change coming almost out of nowhere.

- **Independent Building Block Architecture:** Work was structured in independent "building blocks" that didn't create dependencies or blockages between team members. This architectural approach significantly reduced wasted time and allowed parallel progress across multiple workstreams.

- **Quality Improvements:** Fewer tickets were sent back during this sprint, indicating improved quality of deliverables. The current release cadence (releasing every Monday and Wednesday) enabled the team to catch and fix errors within the same week, creating a faster feedback loop.

- **Documentation Quality:** Tickets are being well-documented with clear acceptance criteria and context, making it easier for team members to understand requirements and for future reference.

- **Team Composure:** The team maintained composure and didn't panic when significant changes were introduced, demonstrating growing maturity in handling uncertainty and shifting priorities.

## Areas for Improvement 🔧

- **Decision-Making for Release Plan Changes:** When the release strategy shifted from alpha to GA, the team should have immediately discussed the necessary subsequent changes and requested time needed to implement them, rather than trying to maintain the original alpha timeline. This required creating new estimates based on the work needed to transition from the alpha plan to full GA readiness.

- **Infrastructure Documentation:** New infrastructure components (EDA validations, flint validators) need comprehensive documentation so other team members have context when they use or modify these systems. While documentation during active architectural changes is challenging, establishing a process for post-sprint technical documentation runs is necessary.

- **Screen App Change Documentation:** Screen app flow changes should be documented to help the Professional Services (PS) support team understand why certain flows were added and to aid future bug investigations. The challenge is capturing these while changes are made on the fly, but version comparison tools could help document before/after differences.

- **Underlying Tool Readiness:** Ensuring underlying tools, particularly the EDA databases, are fully tested and ready for GA is critical to avoid performance or configuration issues when releasing inventory features to all users. Leadership needs visibility into the readiness of foundational infrastructure, not just feature-level functionality.

- **Sprint Investigation Timing:** Investigating and planning the next sprint's implementation while the current architectural approach (DAL vs. direct EDA queries) is in flux may result in wasted effort if fundamental solution patterns change.

## Action Items 📋

1. **Continue Proper Scoping and Planning:** Maintain proper scoping, planning and not panicking when changes come in

2. **Continue Planning Breakdowns:** Continue planning breakdowns and execution of epics ticket wise

3. **Document Environment Changes:** Continue documenting changes between prod/stage and their environments

4. **Investigate DAL Implementation:** Investigate and understand changes between prod/stage and DAL implementation of the changes noted and why

5. **Continue Clarifying User Needs:** Continue clarifying User needs items

## Key Takeaways

This sprint demonstrated the team's growing resilience and adaptability in responding to significant strategic shifts without losing momentum. The architectural decision to structure work as independent building blocks proved valuable, enabling parallel progress and reducing bottlenecks. The pivot from alpha to GA highlighted the need for more proactive communication about implementation timelines when plans change, ensuring leadership understands the downstream impacts. The emergence of the Data Access Layer implementation as a critical path item underscores the importance of addressing technical debt strategically to enable future scalability. Moving forward, the team will balance shipping the current implementation to production while simultaneously upgrading to a more sustainable architectural foundation, all while maintaining the January 21st GA commitment.
