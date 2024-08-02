Git commit hook to check for absolute paths in code

## Usage
- Copy the pre-commit file to .git/hooks folder. It will run automatically before each commit and abort commit if any absolute paths found in staged files
- Run `./pre-commit --all` to check all git tracked files

## Warning
Not much reliable as it just uses a simple regex for checking paths
