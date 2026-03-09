# Sprint Retro - Nov 25, 2025

![Retro Visual](Retro%20Visual.png)

## Sprint Overview

This retrospective was conducted for the Sales Management team following the completion of MLM Epic 1 Infrastructure sprint. This was the team's first sprint focused on building the foundational infrastructure for Multi-Location Management (MLM) as part of the Inventory Management System (Big Bet #5).

## What Went Well 🎯

- **Ticket Breakdown:** Tickets were broken down effectively at the minimal deployable unit level, which enabled developers to work in parallel and maintain development velocity
- **Team Communication:** The team maintained consistent communication about problems and their impact on deadlines, ensuring transparency across all team members with detailed alignment discussions
- **Weekly Sprint Check-ins:** The weekly sprint check-in meetings proved effective and impactful, providing regular touchpoints for progress updates and problem-solving
- **Realistic Sprint Planning:** Despite external factors, the team set what was internally considered a realistic sprint completion date based on controlled variables
- **Smooth Onboarding:** New team member (Saleh) experienced straightforward onboarding mid-sprint, benefiting from strong documentation and team support

## Areas for Improvement 🔧

- **Figma Design Scope Management:** Figma designs included screens and features beyond the current sprint scope, causing confusion about what needed to be implemented. Development team built screens thinking they were in scope, only to discover later they weren't planned for the sprint
- **Decision Documentation:** Critical conversations about flows, triggers, and implementation decisions were often communicated only verbally, leading to confusion during testing. QA discovered changed behaviors that weren't documented, requiring multiple meetings to clarify decisions
- **Early Product Stakeholder Involvement:** Product stakeholders weren't involved early enough in reviewing completed screens to validate alignment with Figma designs and catch defects sooner. Most review happened during QA testing rather than during development
- **Experimental Tools in Sprint:** The team experimented with new approaches during the sprint (Nicholas tool, App Publisher for migrations) which resulted in failures and sprint blockages. These experiments should happen outside sprint timeframes
- **Production-Only Errors:** Some errors were only caught in production environments and not in staging/warehouse environments, creating challenges in proactive defect detection
- **Sprint Planning & Estimation:** While the team set realistic internal goals, external dependencies (deployment, releases, migration issues) were outside team control and impacted the sprint completion target
- **Meeting Structure:** Meetings lacked strict, agenda-oriented structure and sometimes ran over time. Weekly check-ins spent disproportionate time discussing missed deadlines rather than focusing on demos and progress
- **Communication Channels:** Lack of dedicated time and space for QA to communicate feedback during the sprint. Team members felt there wasn't an appropriate forum for sharing concerns until the retrospective
- **Outdated Requirements:** Some requirements in the epic and PRD were outdated or changed mid-sprint, but documentation wasn't updated synchronously
- **Inter-Team Release Coordination:** Managing releases when multiple teams are pushing work simultaneously created queues and bottlenecks. The migration service issue mid-sprint (owned by another team) had to be fixed by this team, disrupting sprint work

## Action Items 📋

1. **Decision Log Implementation:** Create a decision log on Confluence to track all decisions made, with Slack canvas feature as the immediate capture tool before transferring to Confluence for permanent documentation
2. **Bi-Weekly Sprint Retrospectives:** Establish bi-weekly sprint retrospectives as the company minimum standard to provide regular feedback loops
3. **Weekly Check-in Meeting Improvements:** Make weekly check-in meetings required for all team members (Dev, QA, Design, PM) to ensure alignment. Structure meetings with strict agendas and timeboxes, reducing emphasis on deadline justification and increasing focus on demos and visual progress
4. **30-Minute Weekly Decision Meeting:** Create a separate weekly 30-minute decision-oriented meeting (distinct from grooming) to discuss and document changes, requirements updates, and implementation decisions
5. **Figma Design Finalization:** Ensure Figma designs reflect only what's being built for the current sprint before sprint starts. Designer to dedicate time to clean up and finalize designs, removing out-of-scope elements. Consider making Figma non-editable once sprint begins to prevent accidental changes
6. **Proactive Design Demos:** Incorporate visual demos during weekly sprint check-ins even if features aren't fully complete, enabling early product stakeholder feedback and reducing testing time at sprint end
7. **Done Dev Milestone Tracking:** Estimate and track against "Done Dev" deadline as a milestone the team can control, separate from production release dates which are outside team control
8. **Experimental Work Outside Sprints:** Test experimental tools and new approaches outside of sprint timeframes to prevent failures and blockages during active sprints
9. **Vertical vs Horizontal Breakdown Consideration:** For future sprints, consider implications of vertical (by transaction) versus horizontal (by workflow) ticket breakdown from both testing and deployment perspectives, especially for large screens with multiple new features
10. **Documentation Alignment:** Ensure PRD and epic documentation stays aligned with current sprint scope and decisions. Update documentation when scope changes are discovered
11. **Post-Deployment Verification:** Continue checking app publish functionality after deployment to catch production-specific issues early
12. **Migration Documentation Updates:** Update migration and tooling documentation with learnings from issues encountered, sharing knowledge with other teams

## Key Takeaways

This sprint demonstrated the team's strong ability to break down work effectively and maintain transparent communication, enabling parallel development and smooth onboarding. The focus on realistic planning based on prior sprint learnings shows continuous improvement in estimation practices. However, the sprint also revealed critical gaps in decision documentation, early product involvement, and meeting structure that impacted efficiency.

Moving forward, the emphasis will be on implementing structured decision logging (via Slack canvas and Confluence), establishing bi-weekly retrospectives, and creating time-boxed agenda-driven meetings to improve communication flow. The team will also focus on finalizing Figma designs before sprint start and incorporating proactive demos during check-ins to catch issues earlier. By tracking "Done Dev" as a controllable milestone and coordinating better with cross-team releases, the team aims to improve predictability while maintaining the quality-first approach that prevented production issues during this foundational sprint.
