# Git Rebase Practice Setup

## Current Repository Structure

```
* 2594887 (HEAD -> main) Improve add function with logging
|
| * 7f57b67 (feature/advanced-calc) Add divide, power, and sqrt functions
|/
|
| * c3ac4ad (feature/math-operations) Add subtract and multiply functions
|/
|
* 8be6607 (base commit for both branches)
```

## Your Three Branches Explained

### 1. **main** (current)
- Updated `add()` function with logging
- File: [calculator.py with print statement]
- Latest commit: `2594887`

### 2. **feature/math-operations**
- Added: `subtract()`, `multiply()` functions
- File: [calculator.py with math functions]
- Commit: `c3ac4ad`
- **Conflict Area**: Changes to `add()` function

### 3. **feature/advanced-calc**
- Added: `divide()`, `power()`, `sqrt()` functions
- Imported `math` module
- File: [calculator.py with advanced functions]
- Commit: `7f57b67`
- **Conflict Area**: Changes to `add()` function and imports

## Learning Path: Conflicts & Rebase

### Step 1: Try Rebasing feature/math-operations onto main
```bash
git checkout feature/math-operations
git rebase main
```

**Expected**: CONFLICT! Because main changed the `add()` function.

**Why**: Both branches modified the same `add()` function but in different ways.

### Step 2: Resolve the Conflict Manually
When you hit a conflict, you'll see:
```
<<<<<<< HEAD
def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b
=======
def add(a, b):
    """Add two numbers and return result"""
    print("Performing addition...")
    return a + b
>>>>>>> main
```

**Options to resolve**:
1. Keep feature branch version (use theirs)
2. Keep main version (use theirs)
3. Manually merge both changes

**Recommended for learning**: Combine both!
```python
def add(a, b):
    """Add two numbers and return result"""
    print("Performing addition...")
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b
```

### Step 3: Continue the Rebase
```bash
# After editing the conflicted file
git add calculator.py
git rebase --continue
```

### Step 4: Try Rebasing feature/advanced-calc
```bash
git checkout feature/advanced-calc
git rebase main
```

**Expected**: CONFLICT! Same issue - main changed `add()`.

**Additional conflict**: The `import math` statement might conflict too.

### Step 5: View Conflicts Better
```bash
# See what conflicts exist
git diff --name-only --diff-filter=U

# Open file to see conflict markers
code calculator.py
```

## Common Commands for Rebase Learning

| Command | Purpose |
|---------|---------|
| `git rebase main` | Rebase current branch onto main |
| `git status` | See rebase progress and conflicts |
| `git diff` | See exact conflicts |
| `git add .` | Mark conflicts as resolved |
| `git rebase --continue` | Continue after resolving |
| `git rebase --abort` | Cancel rebase and go back |
| `git log --oneline --all --graph` | View all branches |
| `git checkout --theirs calculator.py` | Use remote version |
| `git checkout --ours calculator.py` | Use local version |

## Hands-On Exercises

### Exercise 1: Rebase with Conflict Resolution
```bash
git checkout feature/math-operations
git rebase main
# Resolve conflict by combining both changes
git add calculator.py
git rebase --continue
```

### Exercise 2: Force Push After Rebase
```bash
git push origin feature/math-operations -f
```

⚠️ **Note**: `-f` (force push) is needed because rebase rewrites history. Only safe on your own branches!

### Exercise 3: Abort and Try Again
```bash
git rebase --abort  # Go back to before rebase
git rebase main     # Try again
```

### Exercise 4: Rebase feature/advanced-calc
```bash
git checkout feature/advanced-calc
git rebase main
# This has more conflicts - imports + add function
# Resolve all conflicts
git add calculator.py
git rebase --continue
git push origin feature/advanced-calc -f
```

### Exercise 5: Interactive Rebase
```bash
git checkout feature/math-operations
git rebase -i main
# Edit commits, combine them, reword messages
```

## What You'll Learn

✅ **Rebase Basics**: Moving commits from one branch to another
✅ **Conflict Resolution**: Handling overlapping changes
✅ **Rebase vs Merge**: Linear history vs merge commits
✅ **Force Push**: Why it's needed after rebase
✅ **Recovery**: Using `--abort` to undo
✅ **Interactive Rebase**: Editing and combining commits

## Visual Before & After

**Before Rebase:**
```
main:                    2594887 (Improve add function)
                         /
feature/math-operations: c3ac4ad (Add subtract/multiply)
```

**After Rebase:**
```
main:                    2594887 (Improve add function)
                         /
feature/math-operations: c3ac4ad' (Add subtract/multiply - rebased)
```

## Tips for Success

1. **Always rebase to main first**: Keep your branch up to date
2. **Resolve one conflict at a time**: Use `git status` to see what's left
3. **Use `git diff` to understand**: See exactly what changed
4. **Test after rebase**: Run your code to ensure it works
5. **Force push only on your branch**: Never force push to main!
6. **Ask before rebasing shared branches**: Respect your team

## Next Steps

1. Start with Exercise 1 - rebase feature/math-operations
2. Resolve the conflicts you'll encounter
3. Try feature/advanced-calc - it has more complexity
4. Use interactive rebase to combine commits
5. Practice force pushing changes

Good luck! This is the best way to learn git rebase.
