---
name: git-worktrees
description: Master git worktrees for parallel development, efficient context-switching, and AI agent sandboxes with 2-3x efficiency gains in 2025.
---

# Git Worktrees Best Practices Skill

## Why Worktrees (October 2025 Context)
Git worktrees "truly excel in 2025" particularly with AI-assisted development where:
- Each AI agent gets its own sandbox
- Reduces cognitive overhead
- Makes review and integration easier
- 2-3x efficiency gain vs traditional branching
- Perfect for Claude Code workflows

## Core Concepts

### Traditional Git:
```
repo/
├── .git/
└── [files from current branch]

# Switch branches:
git checkout feature → overwrites working directory
```

### With Worktrees:
```
repo-main/           (main branch)
├── .git/            (shared by all worktrees)
└── [main files]

repo-wt-feature1/    (feature1 branch)
└── [feature1 files]

repo-wt-hotfix/      (hotfix branch)
└── [hotfix files]

# No switching needed - each directory is its own branch!
```

## Best Practices (Sept/Oct 2025)

### 1. Naming Convention ✅
**Format**: `{project}-wt-{purpose}`

**Examples**:
```bash
seekapa-content-wt-blog-automation/
seekapa-content-wt-youtube-integration/
seekapa-content-wt-hotfix-typo/
axia-chatbot-wt-azure-copilot/
axia-chatbot-wt-whatsapp-integration/
```

**Why**:
- Quickly identify purpose
- Easy to find in terminal
- Clear in file managers
- Consistent across projects

### 2. Organization Structure 📁
**Recommended Layout**:
```
~/projects/
├── seekapa-content/              # Main repository
│   ├── .git/                     # Shared git directory
│   └── [main branch files]
├── seekapa-content-wt-feature1/  # Worktree 1
├── seekapa-content-wt-feature2/  # Worktree 2
└── seekapa-content-wt-claude/    # AI agent sandbox
```

### 3. Active Worktree Limits 🎯
**Rule**: Keep ≤ 3 active worktrees per project

**Why**:
- Prevents workspace clutter
- Reduces cognitive load
- Easier to track what's where
- Saves disk space

**When You're Done**:
```bash
# Remove completed worktree
git worktree remove seekapa-content-wt-feature1

# Or if you're in the worktree directory:
cd ..
git worktree remove seekapa-content-wt-feature1
```

### 4. AI Agent Sandboxes 🤖
**Use Case**: Give Claude Code its own workspace

**Setup**:
```bash
# In main repo
git worktree add ../project-wt-claude-sandbox -b claude-sandbox

# Claude Code works here without affecting main
cd ../project-wt-claude-sandbox
# ... Claude makes changes, tests, experiments ...

# Review changes
cd ../project-main
git diff claude-sandbox

# Merge if good
git merge claude-sandbox

# Remove sandbox
git worktree remove ../project-wt-claude-sandbox
git branch -d claude-sandbox
```

### 5. Parallel Development 🔀
**Scenario**: Work on main + feature + hotfix simultaneously

```bash
# Terminal Tab 1: Main branch (production monitoring)
cd ~/seekapa-content

# Terminal Tab 2: Feature development
cd ~/seekapa-content-wt-blog-automation

# Terminal Tab 3: Emergency hotfix
cd ~/seekapa-content-wt-hotfix-urgent
```

**Benefit**: No context switching, everything stays in its state!

## Common Worktree Commands

### Create Worktree
```bash
# Create new worktree with new branch
git worktree add ../project-wt-feature1 -b feature1

# Create worktree from existing branch
git worktree add ../project-wt-feature2 feature2

# Create worktree at specific commit
git worktree add ../project-wt-hotfix abc1234
```

### List Worktrees
```bash
git worktree list

# Output:
# /home/user/project-main     abc1234 [main]
# /home/user/project-wt-feat  def5678 [feature1]
# /home/user/project-wt-fix   ghi9012 [hotfix]
```

### Remove Worktree
```bash
# From main repo
git worktree remove ../project-wt-feature1

# If worktree directory deleted manually
git worktree prune
```

### Move Worktree
```bash
# Move directory, then update git
mv project-wt-old project-wt-new
git worktree repair
```

## Workflow Examples

### Example 1: Feature Development
```bash
# Start new feature
cd ~/seekapa-content
git worktree add ../seekapa-content-wt-multilang -b feature/multilang

# Work on feature
cd ../seekapa-content-wt-multilang
# ... make changes, commit ...

# Test in isolation
npm test

# When ready, merge from main repo
cd ~/seekapa-content
git merge feature/multilang

# Clean up
git worktree remove ../seekapa-content-wt-multilang
git branch -d feature/multilang
```

### Example 2: Emergency Hotfix
```bash
# Main is on feature branch, need urgent fix
cd ~/seekapa-content
# (currently on develop branch with uncommitted changes)

# Create hotfix worktree from main
git worktree add ../seekapa-content-wt-hotfix main

# Fix in hotfix worktree
cd ../seekapa-content-wt-hotfix
# ... make fix, test, commit ...
git push origin main

# Back to feature work (unchanged!)
cd ~/seekapa-content
# ... continue where you left off ...

# Later, remove hotfix worktree
git worktree remove ../seekapa-content-wt-hotfix
```

### Example 3: Claude Code Assisted Development
```bash
# Create sandbox for Claude experiments
git worktree add ../project-wt-claude -b claude-experiment

# Give Claude access to this directory
# Claude makes changes, tests, refactors

# Review Claude's work
git diff main claude-experiment

# If good, merge
git checkout main
git merge claude-experiment

# If not good, just delete
git worktree remove ../project-wt-claude
git branch -D claude-experiment  # Force delete
```

## Integration with Claude Code

### Hook: Auto-Suggest Worktree
When Claude Code detects branch switch needs:
```
Claude: "I notice you want to work on feature X while keeping
current work. Should I create a git worktree instead?"

Options:
1. Create worktree for feature X
2. Stash and switch (traditional)
3. Continue in current branch
```

### Hook: Worktree Cleanup Reminder
```
Claude: "You have 5 active worktrees. Want me to show which
ones can be cleaned up?"

Shows:
- Last commit date
- Branch status (merged/unmerged)
- Disk space used
- Suggests which to remove
```

## Common Issues & Solutions

### Issue: "fatal: 'X' is already checked out"
**Cause**: Branch can only be checked out in one worktree at a time
**Solution**:
```bash
# List where branch is checked out
git worktree list | grep branch-name

# Remove that worktree first
git worktree remove /path/to/worktree
```

### Issue: Worktree directory deleted manually
**Cause**: Removed folder without `git worktree remove`
**Solution**:
```bash
git worktree prune
```

### Issue: Can't remove worktree (uncommitted changes)
**Solution**:
```bash
# Force remove
git worktree remove --force /path/to/worktree
```

## Advanced Techniques

### Bare Repository + All Worktrees
```bash
# Clone as bare repo
git clone --bare https://github.com/user/repo.git repo.git

# All branches as worktrees
cd repo.git
git worktree add ../repo-main main
git worktree add ../repo-develop develop
git worktree add ../repo-feature1 feature1

# No "main" directory, everything is a worktree!
```

## Quick Reference Card

```
# Create
git worktree add <path> [-b <branch>]

# List
git worktree list

# Remove
git worktree remove <path>

# Clean up deleted worktrees
git worktree prune

# Move (after moving directory)
git worktree repair

# Lock (prevent accidental removal)
git worktree lock <path>

# Unlock
git worktree unlock <path>
```

## Notes
- Worktrees share the same .git directory (saves space)
- Each worktree can be on different branch
- Perfect for AI-assisted development in 2025
- 2-3x efficiency gain for complex projects
- Clean up regularly to avoid clutter
- Use meaningful naming conventions
- Limit active worktrees to ≤ 3 per project
