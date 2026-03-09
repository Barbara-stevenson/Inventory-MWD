# Jira Story: Add Selectable Modal Sizes to Open Screen as Pop-up Action

**Issue Type:** Story
**Project:** PL (Platform)
**Epic Link:** PL-56600 - Multi-Location MVP
**Priority:** TBD
**Labels:** modal, action-editor, ps-requested, flexibility-enhancement

---

## Summary
Add Selectable Modal Sizes to Open Screen as Pop-up Action

---

## Overview

Add the ability for users to select from three predefined modal sizes (Small, Medium, Large) when configuring the 'Open Screen as Pop-up' action in the Action Editor. This feature was requested by the Professional Services team to unlock more flexibility and enable more valuable customizations and workflows.

---

## Business Context

Based on feedback from 4 PS team members (Matt Shade, Charvi Anand, Cole Arnett, Brandon Saltzman), this feature addresses several pain points:

- **Eliminates HTML break workarounds:** PS team currently uses HTML break hacks to achieve larger modal sizes
- **Unlocks daily operational workflows:** Current workflows primarily serve specific, infrequent business needs rather than daily operations
- **Provides more flexibility:** All PS team members confirmed this enables more unique customizations and workflows
- **Described as "game changer"** by PS team members

### Key Quotes from PS Feedback:
- *"We've been using html breaks for reproducing the above sizes when needed... So definitely, we won't have to use that anymore"* - Charvi Anand
- *"Even having the option of different sizes is game changer!"* - Cole Arnett
- *"I most likely to use the bigger options for sure depending on what I am doing"* - Matt Shade
- *"It definitely helps to have that flexibility"* - Brandon Saltzman

---

## Proposed Modal Sizes

- **Small (current state):** 480px width × 586px height
- **Medium:** 640px width × 586px height
- **Large:** 900px width × 508px height

---

## User Story

**As a** Method user customizing workflows,
**I want** to select from predefined modal sizes when configuring pop-up screens,
**So that** I can create more flexible and valuable workflows without using workarounds like HTML breaks.

---

## Acceptance Criteria

### AC1: Size Selector UI
- [ ] A size selector (dropdown or radio buttons) is added to the 'Open Screen as Pop-up' action configuration in the Action Editor
- [ ] Three options are available: Small, Medium, Large
- [ ] Small is set as the default to maintain backward compatibility with existing pop-ups
- [ ] The selector is clearly labeled and intuitive to use

### AC2: Modal Rendering
- [ ] When a modal is opened at runtime, it displays at the selected size:
  - Small: 480px × 586px
  - Medium: 640px × 586px
  - Large: 900px × 508px
- [ ] Modal contents resize to fit within the selected dimensions
- [ ] Modal is centered on screen regardless of size selected

### AC3: Scroll Bar Behavior
- [ ] If modal content exceeds the selected size, scroll bars appear automatically (maintaining current behavior)
- [ ] Scroll bars function identically to current implementation
- [ ] Both horizontal and vertical scroll bars appear as needed

### AC4: Dynamic Resizing
- [ ] If a user changes the size selection in the Action Editor and saves, the modal resizes accordingly when opened at runtime
- [ ] Modal content reflows appropriately to the new dimensions
- [ ] No visual glitches or layout breaks when switching between sizes

### AC5: Backward Compatibility
- [ ] All existing pop-up modals default to 'Small' size and continue to function without changes
- [ ] No breaking changes to existing workflows
- [ ] Users can open and edit existing pop-up actions without being forced to select a size

### AC6: Save and Load Behavior
- [ ] Selected modal size is saved with the action configuration
- [ ] Selected modal size persists when action is edited later
- [ ] Selected modal size displays correctly in the Action Editor when reopened

---

## Technical Notes

### Implementation Details
- **Location:** Action Editor → 'Open Screen as Pop-up' action configuration
- **UI Control:** Dropdown or radio button selector (UX to determine best option based on design system)
- **No custom sizing capability:** Only predefined Small/Medium/Large options available
- **Responsive behavior:** Maintains current modal functionality for scroll bars and content overflow

### Data Storage
- Size selection must be stored in action configuration data
- Default value: "small" for backward compatibility
- Acceptable values: "small", "medium", "large"

### UI/UX Considerations
- Size selector should be placed prominently in the action configuration panel
- Consider showing preview dimensions (e.g., "Small (480 × 586)")
- Ensure the selector doesn't disrupt existing action configuration workflow

---

## Future Enhancements (Out of Scope)

Based on PS feedback, these were mentioned but not required for initial release:
- Extra-large or full-screen modal option (requested by Cole Arnett and Brandon Saltzman)
- Mobile-optimized small size that matches phone screen dimensions (requested by Matt Shade)
- Custom size input fields (requested by Charvi Anand)

---

## References

- **PS Team Feedback:** `Big Bet #5 - Inventory Management MLP/Build Stage/Modal/Feedback/Modal Selectable Sizes Feedback.pdf`
- **Visual References:**
  - Small Modal: `Small Modal Size (current state).png`
  - Medium Modal: `Medium Modal Size.png`
  - Large Modal: `Large Modal Size.png`
- **Related Epic:** PL-56600 - Multi-Location MVP

---

## Definition of Done

- [ ] Code complete and peer reviewed
- [ ] Unit tests written and passing
- [ ] QA testing complete (all ACs verified)
- [ ] Design review approved
- [ ] Documentation updated (if applicable)
- [ ] Feature deployed to production
- [ ] PS team notified of availability

---

## Questions for Product/Design

1. Should the size selector be a dropdown or radio buttons?
2. Should we show dimension hints in the selector (e.g., "Small (480 × 586)")?
3. Do we need to support responsive sizing for different screen resolutions, or are fixed pixel sizes sufficient?
4. Should there be any visual preview of the modal size in the Action Editor?
