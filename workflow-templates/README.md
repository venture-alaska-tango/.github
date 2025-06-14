# Organization-wide Workflow Templates

This directory contains GitHub Actions workflow templates for organization-wide deployment across all repositories in the Tango GitHub organization.

## Files

- `devin-pr-review.yml` - Automated Devin PR review workflow template
- `devin-pr-review.properties.json` - Metadata file for the Devin PR review workflow template

## Devin PR Review Workflow

### Overview
Automatically triggers Devin reviews on PR opened, synchronized, and reopened events across all repositories in the organization. Also supports manual triggering via workflow_dispatch.

### Features
- **Automatic PR Reviews**: Triggers Devin reviews on PR opened, synchronized, and reopened events
- **Manual Triggering**: Supports manual workflow execution via workflow_dispatch
- **Organization-wide Deployment**: Deployed via GitHub workflow templates in `.github` repository
- **Comprehensive Review Process**: 8-step workflow with detailed GitHub API integration
- **Safety Guardrails**: Pre-push hooks and explicit no-commit rules for Devin
- **Error Handling**: Complete API response validation and session management
- **Comment System**: Detailed inline comments with embedded code using GitHub REST API
- **Suggested Changes Support**: Uses GitHub's suggestion markdown for actionable feedback
- **Auto-approval**: Automatically approves PRs when no issues are found
- **Adjustable Comment Limits**: Default 20 comments per PR (easily customizable)

### Tango-specific Requirements
- **JIRA Ticket Validation**: Ensures TNGO-XXX format in PR titles and descriptions
- **Commit Message Format**: Validates `feat: TNGO-XXX description` format (not parentheses)
- **Semantic Versioning**: Compliance checks where applicable
- **Organization Standards**: Code quality and adherence to Tango coding standards

### Authentication
Uses the existing `DEVIN_API_KEY` organization-level secret for Devin API authentication.

### Deployment
This workflow template is deployed organization-wide via GitHub's workflow template system, automatically making it available to all current and future repositories in the Tango organization.

### Implementation Details
Based on the proven implementation pattern from Cognition's blog post "Devin 101: Automatic PR Reviews with the Devin API", including:
- Complete error handling for API requests
- Detailed instructions for inline code comments
- Comment consolidation and deduplication logic
- Proper permissions (contents: read, pull-requests: write, issues: read)
- JSON escaping and session management

### Customizations
1. **Adjustable Comment Limits**: Maximum 20 comments per PR (easily customizable in workflow prompt)
2. **Suggested Changes Support**: Uses GitHub's ```suggestion markdown for actionable feedback
3. **Auto-approval**: Automatically approves PRs when no issues are detected
