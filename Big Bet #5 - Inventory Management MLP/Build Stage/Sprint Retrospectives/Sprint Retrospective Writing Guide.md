# Sprint Retrospective Writing Guide

This guide provides a standardized template and best practices for documenting sprint retrospectives for the Inventory Management System (Big Bet #5) project.

## Purpose

Sprint retrospectives help teams:
- Reflect on completed work and team performance
- Identify successes to reinforce positive behaviors
- Surface challenges and improvement areas
- Define concrete action items for future sprints
- Maintain institutional knowledge of team evolution

## Document Structure

### 1. Header
```
Sprint Retro - [Date]
```

### 2. Sprint Overview
Provide context for the retrospective:
- Which sprint number/iteration this covers
- Primary feature(s) or focus area of the sprint
- Team composition changes (if any)
- Key sprint objectives

**Example:**
> This retrospective was conducted for the Sales Management team following the completion of Sprint 1, which focused on the Inventory Creation Modal feature. The team gathered to reflect on the sprint's successes, challenges, and identify actionable improvements for future iterations.

### 3. What Went Well 🎯

Document team successes and positive behaviors to reinforce.

**Categories to consider:**
- **Communication:** How did information flow within the team?
- **Collaboration:** Cross-functional teamwork examples
- **Delivery:** Features shipped, milestones reached
- **Quality:** Testing, defect detection, code reviews
- **Process:** Estimation accuracy, planning effectiveness
- **Team Development:** Onboarding, knowledge sharing
- **Adaptability:** How the team handled changes or obstacles
- **Technical Achievements:** Architecture decisions, technical wins

**Format:**
- Use bullet points with bold category headers
- Include specific examples where possible
- Focus on actionable behaviors that can be repeated

**Example:**
- **Effective Communication:** The team maintained consistent communication about problems and their impact on deadlines, ensuring transparency across all team members with detailed alignment discussions
- **Quality Focus:** Successfully caught critical defects early and resolved most issues within the sprint
- **Feature Delivery:** Shipped modals, including one of the most requested features for outside tabs

### 4. Areas for Improvement 🔧

Identify challenges and opportunities for growth without blame.

**Categories to consider:**
- **Planning:** Sprint planning, estimation, goal setting
- **Process:** Workflows, handoffs, bottlenecks
- **Technical:** Architecture, technical debt, tooling
- **Communication:** Decision tracking, documentation, stakeholder involvement
- **Quality:** Testing coverage, bug tracking
- **Collaboration:** Cross-functional coordination, domain expert involvement
- **Delivery:** Release management, dependencies

**Format:**
- Use bullet points with bold category headers
- State the problem clearly and objectively
- Avoid blaming individuals; focus on process improvements
- Include specific impacts when relevant

**Example:**
- **Sprint Planning:** Not providing a realistic completion date resulted in missing the initial sprint completion target
- **Decision Making:** Need to track decisions more effectively and involve the right stakeholders earlier (better documentation or more documentation needed)
- **Domain Expert Involvement:** Not involving domain experts early enough to help validate direction and technical feasibility

### 5. Action Items 📋

Convert improvement areas into concrete, actionable next steps.

**Action Item Criteria:**
Each action item should be:
- **Specific:** Clear and unambiguous
- **Assignable:** Has an owner or responsible party
- **Measurable:** Can determine if it's complete
- **Actionable:** Team can actually implement it
- **Time-bound:** For the next sprint or specific timeframe

**Format:**
- Numbered list for tracking
- Include owner/responsible party when known
- Link action items to improvement areas identified above
- Prioritize items that will have the biggest impact

**Example:**
1. **Tooling Enhancement:** John to try out a new Granola competitor for better meeting note-taking
2. **Sprint Planning Improvements:** Keep sprint planning realistic with goals in mind; templates should be realistic
3. **Sprint Check-ins:** Ensure PM+Design is playing with sprint more often, with frequent check-ins on sprint progress (demo state)
4. **Domain Expert Engagement:** Continue to involve domain experts in the process early (grooming, solutioning, review)

### 6. Key Takeaways

Synthesize the retrospective into 2-4 sentences capturing:
- Overall sprint performance assessment
- Primary themes from successes and challenges
- Focus areas for upcoming sprint(s)
- Team morale and momentum

**Example:**
> This sprint demonstrated the team's strong ability to deliver value while adapting to challenges. The focus on communication and quality helped deliver critical features, including highly requested functionality. Moving forward, the emphasis will be on more realistic planning, earlier stakeholder involvement, and improved documentation practices to maintain momentum while reducing friction in the development process.

## Optional Sections

### Visual Elements
Consider including:
- **Retrospective Board Screenshot:** Visual capture of sticky notes/board from retro session
- **Sprint Metrics:** Velocity, completion rate, defect counts
- **Timeline:** Key events or milestones during the sprint

### Specific Callouts
- **Shoutouts:** Recognize individual contributions
- **Experiments:** Track results of process experiments from previous sprint
- **Blockers Resolved:** Document how major blockers were overcome
- **Technical Decisions:** Record significant architectural or technical choices made

## Best Practices

### During the Retrospective Session
1. **Timebox appropriately:** 60-90 minutes for a 2-week sprint
2. **Create psychological safety:** Encourage honest feedback without fear
3. **Focus on the team:** Avoid blaming individuals; examine processes
4. **Use data:** Reference sprint metrics, not just feelings
5. **Involve everyone:** Ensure all voices are heard
6. **Prioritize action items:** Don't create a list too long to act on

### Writing the Document
1. **Write within 24 hours:** Capture insights while fresh
2. **Be specific:** Use concrete examples, not generalities
3. **Balance positive and negative:** Don't only focus on problems
4. **Make it scannable:** Use headers, bullets, formatting
5. **Link to related docs:** Reference PRDs, RFCs, tickets as needed
6. **Track action items:** Ensure action items are added to next sprint planning

### Following Up
1. **Share broadly:** Distribute to team and stakeholders
2. **Review previous action items:** Check on progress in next retro
3. **Track patterns:** Notice recurring themes across sprints
4. **Update processes:** Actually implement the improvements identified
5. **Archive properly:** Store in consistent location for easy reference

## File Naming Convention

```
Sprint Retro [Feature Name] - [Month] [Day][suffix] [Year].md
```

**Examples:**
- `Sprint Retro Inventory Creation Modal - Sept 9th 2025.md`
- `Sprint Retro Stock Transfers - Oct 15th 2025.md`
- `Sprint Retro Multi-Warehouse Management - Nov 3rd 2025.md`

## Storage Location

Save retrospectives in:
```
Big Bet #5 - Inventory Management MLP/Build Stage/Sprint Retrospectives/
```

## Confluence Publishing

After creating the sprint retrospective markdown file, publish it to Confluence:

**Location:** Software Development (SD) Space > **Retro Sales Management** folder

**Steps:**
1. Create a new page in Confluence under the "Retro Sales Management" folder
2. Use the markdown content as the page body
3. Title format: `Sprint Retro [Feature/Epic Name] - [Month] [Day][suffix] [Year]`
4. Add the visual retrospective board image to the top of the page if available
5. Ensure the page is saved under the correct parent folder (Retro Sales Management - Folder ID: 182452229)

**Example Confluence URL:**
- https://method.atlassian.net/wiki/spaces/SD/folder/182452229

**Note:** All sprint retrospectives should be centralized in the "Retro Sales Management" folder for easy team access and historical tracking.

## Template

```markdown
# Sprint Retro - [Date]

[Optional: Include visual of retrospective board]

## Sprint Overview

[Brief context: sprint number, focus area, key objectives]

## What Went Well 🎯

[Successes and positive behaviors]

- **Category:** Description with specific examples

## Areas for Improvement 🔧

[Challenges and opportunities]

- **Category:** Problem statement with impact

## Action Items 📋

[Concrete next steps]

1. **Action Title:** Description with owner
2. **Action Title:** Description with owner

## Key Takeaways

[2-4 sentence synthesis of retrospective and focus for next sprint]
```

## Related Documentation

- Product Requirements Documents (PRDs) in `Build Stage/[Feature]/`
- Feature request analysis in `Discovery/Feature Request Data/`
- User feedback in `Prototype Stage/Prototype Testing Feedback/`

---

*This guide should evolve based on team needs and retrospective learnings. Update it when discovering new effective practices.*
