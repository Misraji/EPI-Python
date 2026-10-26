# Upload to your private GitHub repository

These instructions assume you have an account on GitHub and Git installed on your computer. **The original EPI PDF is deliberately not included** in this repository. The extracted text is copyrighted and should remain in your private personal-study repository rather than being published openly.

## First-time local setup

Unzip `epi-python-repository.zip`. Open a shell in the extracted `epi-python/` folder:

```bash
git init
git add .
git diff --cached --stat
git commit -m "Initialize EPI Python learning repository"
```

On GitHub, create a **private** empty repository named `epi-python` (don't initialize it with README or license if the local repository already has those files). GitHub will show the HTTPS or SSH remote URL.

```bash
# Substitute the real URL shown by GitHub (not this placeholder):
git remote add origin <YOUR_PRIVATE_REPOSITORY_URL>
git branch -M main
git push -u origin main
```

`git status` should show no unstaged work when everything is committed. Visit the **Actions** tab in your private GitHub repository: the included workflow installs the package and runs pytest on pushes and pull requests.

## Keeping up with changes

```bash
git status
git diff
python -m pytest -v
git add .
git commit -m "Annotate more EPI exercises"
git push
```

Read [PYTHON_DEVELOPMENT_GUIDE.md](PYTHON_DEVELOPMENT_GUIDE.md) for what Git, commits, branches, `.gitignore`, and CI mean.
