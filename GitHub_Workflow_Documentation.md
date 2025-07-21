# Git & GitHub Workflow Detailed Documentation

## Overview
This document provides step-by-step instructions and the actual commands used to learn Git and GitHub, covering repository creation, managing changes, collaborating via branches and pull requests, and finalizing merges.

---

## Initial Setup

### Configure User Identity
```bash
git config --global user.name "SaikrishnaNanduri"
git config --global user.email "nanduri174@gmail.com"
```

### Initialize a New Repository
```bash
mkdir git-learning-demo && cd git-learning-demo
git init
```
---

## Basic Git Operations

### Create Files
- README.md
- hello.py

#### Command
```bash
touch README.md hello.py
```

### Check Repository Status
```bash
git status
```

### Stage Files
```bash
git add .
```

### Commit Changes
```bash
git commit -m "Initial commit: Add README and hello.py"
```
---

## Branching & Merging

### Create Feature Branch
```bash
git checkout -b feature/add-math-functions
```

### Develop New Feature
- math_utils.py

#### Command
```bash
touch math_utils.py
```

### Commit Feature
```bash
git add math_utils.py
git commit -m "Add math utilities module"
```

### Merge Branch
```bash
git checkout master
git merge feature/add-math-functions
```
---

## GitHub Workflow

### Authenticate GitHub
```bash
gh auth login
```

### Create Repository on GitHub
```bash
gh repo create git-learning-demo --public --source . --push
```

### Create Pull Request
```bash
gh pr create --title "Add Advanced Calculator" --body "..."
```

### Merge Pull Request
```bash
gh pr merge 1 --squash --delete-branch
```

---

## Summary
- **Repository**: Initialized and configured
- **Feature Branch**: Implemented and merged
- **GitHub**: Connected and collaborated

This document serves as a comprehensive guide encompassing the practical commands executed during the learning journey with Git and GitHub. Each section outlines specific tasks, descriptions, and exact commands to replicate the workflow.
