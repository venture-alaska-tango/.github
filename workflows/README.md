# Organization-wide Workflow Templates

This directory contains GitHub Actions workflow templates for organization-wide deployment across all repositories in the Tango GitHub organization.

## Files

- `devin-pr-review.yml` - Automated Devin PR review workflow template

## Devin PR Review Workflow

### Overview
Automatically triggers Devin reviews when the "devin-review" label is added to PRs across all repositories in the organization.

### Features
- **Label-based Triggering**: Only runs when "devin-review" label is added to PRs
- **Organization-wide Deployment**: Designed for deployment via GitHub organization rulesets
- **Comprehensive Review Process**: 8-step workflow with detailed GitHub API integration
- **Safety Guardrails**: Pre-push hooks and explicit no-commit rules for Devin
- **Error Handling**: Complete API response validation and session management
- **Comment System**: Detailed inline comments with embedded code using GitHub REST API
- **Suggested Changes Support**: Uses GitHub's suggestion markdown for actionable feedback
- **Auto-approval**: Automatically approves PRs when no issues are found
- **Adjustable Comment Limits**: Default 3 comments per PR (easily customizable)

### Tango-specific Requirements
- **JIRA Ticket Validation**: Ensures TNGO-XXX format in PR titles and descriptions
- **Commit Message Format**: Validates `feat: TNGO-XXX description` format (not parentheses)
- **Semantic Versioning**: Compliance checks where applicable
- **Organization Standards**: Code quality and adherence to Tango coding standards

### Authentication
Uses the existing `DEVIN_API_KEY` organization-level secret for Devin API authentication.

### Deployment
This workflow template will be deployed organization-wide via GitHub rulesets, automatically applying to all current and future repositories in the Tango organization.

### Implementation Details
Based on the proven implementation pattern from Cognition's blog post "Devin 101: Automatic PR Reviews with the Devin API", including:
- Complete error handling for API requests
- Detailed instructions for inline code comments
- Comment consolidation and deduplication logic
- Proper permissions (contents: read, pull-requests: write, issues: read)
- JSON escaping and session management

### Customizations
1. **Label-based Triggering**: Add "devin-review" label to trigger automated review
2. **Comment Limits**: Maximum 3 comments per PR (adjustable in workflow prompt)
3. **Suggested Changes**: Uses GitHub's ```suggestion markdown for actionable feedback
4. **Auto-approval**: Automatically approves PRs when no issues are detected
