# Organization-wide GitHub Actions Workflows

This directory contains GitHub Actions workflows for organization-wide deployment across all repositories in the Tango GitHub organization.

## Files

- `devin-pr-review.yml` - Automated Devin PR review workflow template

## Devin PR Review Workflow

### Overview
Automatically triggers Devin reviews on PR opened, synchronized, and reopened events across all repositories in the organization. Also supports manual triggering via workflow_dispatch.

### Features
- **Automatic PR Reviews**: Triggers Devin reviews on PR opened, synchronized, and reopened events
- **Manual Triggering**: Supports manual workflow execution via workflow_dispatch
- **Organization-wide Deployment**: Designed for deployment via GitHub organization rulesets
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
This workflow template will be deployed organization-wide via GitHub rulesets, automatically applying to all current and future repositories in the Tango organization.

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

### Repository Dispatch Usage
The workflow can be triggered from other repositories using the `repository_dispatch` event. This enables organization-wide PR reviews from a centralized workflow.

#### Example API Call
```bash
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $(gh auth token)" \
  https://api.github.com/repos/venture-alaska-tango/.github/dispatches \
  -d '{"event_type":"devin-pr-review","client_payload":{"repo":"venture-alaska-tango/target-repo","pr_number":123}}'
```

#### Parameters
- `event_type`: Must be `devin-pr-review` to trigger this workflow
- `client_payload.repo`: Target repository in `owner/repo` format
- `client_payload.pr_number`: Pull request number to review
