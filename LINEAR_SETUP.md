# 🔗 Linear Integration Setup Guide

This document provides detailed instructions for integrating this repository with Linear for enhanced project management.

## What is Linear?

Linear is a modern project management and issue tracking tool designed for software teams. It offers a streamlined workflow for managing tasks, bugs, and feature requests with deep GitHub integration.

## Prerequisites

1. A Linear account (sign up at [linear.app](https://linear.app))
2. Admin access to this GitHub repository
3. Admin or member access to a Linear workspace

## Setup Instructions

### Step 1: Install Linear GitHub App

1. Go to your Linear workspace
2. Click on your workspace name in the bottom left
3. Select **Settings** → **Integrations**
4. Find **GitHub** in the list of integrations
5. Click **Add GitHub integration**
6. Follow the OAuth flow to authorize Linear to access your GitHub account

### Step 2: Connect This Repository

1. In Linear, go to **Settings** → **Integrations** → **GitHub**
2. Click **Add repositories**
3. Select `HawkEyeTheRapper/EverLight_Restore_Page`
4. Click **Install** or **Save**

### Step 3: Configure Team and Project

1. In Linear, note your team key (e.g., "EVER" or "EL")
   - You can find this in your team settings or in the URL when viewing your team
2. Create a project for this repository (optional but recommended)
   - Go to your team and click **Projects**
   - Create a new project (e.g., "EverLight Restore")
   - Note the project key
3. Update `.github/linear.yml` in this repository:
   ```yaml
   teamKey: "YOUR_TEAM_KEY"
   projectKey: "YOUR_PROJECT_KEY"  # Optional
   ```

### Step 4: Test the Integration

1. Create a test GitHub issue in this repository
2. Check that it appears in Linear within a few seconds
3. Make a comment on the Linear issue
4. Verify the comment syncs back to GitHub

## How It Works

### Issue Synchronization

- **GitHub → Linear**: When you create an issue in GitHub, it's automatically created in Linear
- **Linear → GitHub**: When you create an issue in Linear and associate it with this repo, it syncs to GitHub
- **Bi-directional updates**: Changes to title, description, status, and labels sync both ways

### Pull Request Tracking

- When you create a PR and reference a Linear issue (e.g., "Fixes EL-123"), the PR is linked in Linear
- PR status (draft, ready for review, merged, closed) is reflected in Linear
- You can see all related PRs directly in the Linear issue

### Comment Sync

- Comments on GitHub issues sync to Linear
- Comments on Linear issues sync to GitHub
- Maintains attribution so you know who said what

### Status Management

- When a PR that fixes a Linear issue is merged, the Linear issue is automatically closed
- You can customize status mappings in `.github/linear.yml`

## Common Workflows

### Creating a New Feature

1. Create an issue in Linear with type "Feature"
2. The issue syncs to GitHub automatically
3. Create a branch and PR referencing the Linear issue ID (e.g., "EL-123")
4. Linear shows the PR status in the issue view
5. When the PR is merged, Linear automatically closes the issue

### Bug Tracking

1. Report a bug as a GitHub issue
2. The issue appears in Linear
3. Assign it to a team member in Linear
4. Team member creates a fix and references the issue in the PR
5. Bug is automatically closed when PR is merged

### Roadmap Planning

1. Use Linear's roadmap view to plan releases
2. Associate issues with milestones
3. Track progress as PRs are merged
4. GitHub and Linear stay in sync throughout

## Customization Options

Edit `.github/linear.yml` to customize:

- **Label Mapping**: Map GitHub labels to Linear labels
- **Status Mapping**: Define how GitHub states map to Linear states
- **Auto-close Behavior**: Control when issues close automatically
- **Comment Sync**: Enable/disable comment synchronization

## Benefits

✅ **Single Source of Truth**: All project information in one place
✅ **Better Planning**: Use Linear's roadmap and cycle planning features
✅ **Faster Workflows**: Quick keyboard shortcuts and smart issue creation
✅ **Team Collaboration**: Better visibility into who's working on what
✅ **GitHub Integration**: Keep using GitHub while gaining Linear's power

## Troubleshooting

### Issues Not Syncing

- Check that the Linear GitHub App has access to this repository
- Verify your team and project keys are correct in `.github/linear.yml`
- Check Linear's integration logs in Settings → Integrations → GitHub

### Duplicate Issues

- Ensure you're not creating issues in both places at the same time
- Use one tool as the primary source and let it sync to the other

### Permission Errors

- Verify you have admin access to both the GitHub repo and Linear workspace
- Re-authorize the GitHub integration if needed

## Resources

- [Linear Documentation](https://linear.app/docs)
- [Linear GitHub Integration Guide](https://linear.app/docs/github)
- [Linear API](https://developers.linear.app/)

## Support

For issues with this integration:
1. Check Linear's integration status page
2. Review GitHub webhook logs (Settings → Webhooks)
3. Contact Linear support at support@linear.app
4. File an issue in this repository

---

**Note**: This integration requires the repository to be connected to a Linear workspace. Make sure to complete all setup steps before expecting full functionality.
