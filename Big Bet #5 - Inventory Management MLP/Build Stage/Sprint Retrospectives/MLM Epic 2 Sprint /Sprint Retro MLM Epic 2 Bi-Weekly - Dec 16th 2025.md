# Sprint Retro - Dec 16, 2025

![Retro Visual Dec 16 2025](Retro%20Visual%20Dec%2016%202025.png)

## Sprint Overview

This retrospective was conducted for the Sales Management team following the completion of the MLM Epic 2 bi-weekly sprint, which focused on advancing the Multi-Location Management (MLM) feature set. The team continued building on the infrastructure established in Epic 1, with emphasis on improving code quality, streamlining release processes, and maintaining cross-functional collaboration between development, design, and QA.

## What Went Well 🎯

- **Quality Focus:** Far fewer tickets were sent back to "In Dev" from "In Test" compared to the previous sprint. The development team (Fareen, Kanishka) delivered higher quality work upfront, attributed to detailed analysis, clear instructions, and comprehensive testing angles documented in tickets. This meant QA did not need to request re-fixes from developers.

- **Communication:** Good communication and frequent updates were maintained throughout the sprint. The team kept stakeholders informed about progress, blockers, and technical decisions, ensuring transparency across all team members.

- **Decision Log Adoption:** The decision log saw active use and consistent updates from team members (Fareen and Kanishka), creating a reliable record of technical and product decisions that can be referenced by the broader team.

- **Proactive Problem-Solving:** The "see something, say something" approach proved effective, with QA (Saleh) proactively reporting breakages in beta environments. This helped the team cover more edge cases and prevent issues from reaching production.

- **Code Documentation:** Consistent labeling of actions and components with comments improved navigation and debugging efficiency. This practice, implemented as a response to previous feedback, significantly reduced time spent understanding code context during reviews and testing.

## Areas for Improvement 🔧

- **Release Process:** The release workflow needs further streamlining to reduce friction during deployment windows. While a more structured release procedure was implemented during this sprint (tested on trial days), there's opportunity to formalize and optimize the process further.

- **Merge Conflict Management:** Merge conflicts during release merges were missed due to inconsistent pre-merge checks. This created last-minute friction during critical release windows when speed and accuracy are essential.

- **No-Code Environment Contention:** Increasing requests from the No-Code team to use the app builder environment on beta are trending upward. While not actively blocking sprints yet, the pace of requests suggests this could become a blocker if the team's output increases without alternative testing environments for No-Code.

- **Status Tracking Automation:** Manual updates to the Excel sheet for ticket status changes remain necessary until automation is implemented. This creates risk of status drift between actual progress and documented progress, impacting visibility for stakeholders.

## Action Items 📋

1. **Merge Conflict Prevention:** Be proactive to check work more often to avoid merge conflicts during release merges. Implement a checklist or automated check before initiating release processes.

2. **Maintain Quality Standards:** Continue with the great quality of output and clear instructions for testing. This practice has proven effective in reducing rework cycles.

3. **Environment Contention Planning:** Set clear expectations with QA Manager John Jones that No-Code's requests for the beta app builder environment are not a blocker currently, but will eventually impact the team's ability to test and release in a timely manner as output increases. Encourage exploration of alternative environments for No-Code testing.

4. **Automate Status Tracking:** Add automation to the Excel dev tracker to eliminate manual status update requirements and ensure real-time visibility into ticket progress.

5. **Continue Communication Cadence:** Continue frequent commits, updates, and communication to maintain transparency and team alignment.

6. **Formalize Release Procedures:** Document and refine the more streamlined and structured release procedures tested during this sprint to establish a repeatable, reliable process.

7. **Maintain Code Documentation:** Continue keeping actions and components labeled with comments to support efficient debugging and onboarding.

## Key Takeaways

This sprint demonstrated measurable improvements in code quality and team collaboration, resulting in significantly fewer defects requiring rework. The decision log and proactive communication practices established strong foundations for cross-functional alignment. Moving forward, the team should prioritize formalizing the release process, implementing merge conflict prevention checks, and proactively addressing the emerging environment contention issue before it becomes a sprint blocker. Team momentum remains strong with clear visibility into both successes and improvement opportunities.
