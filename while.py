import os
import time
from github import Github

# GitHub repository information
REPO_OWNER = "prabhukiran9999"
REPO_NAME = "pr-script"
PR_HEAD = "main"
PR_BASE = "dev"
PR_TITLE = "Title of the Pull Request"
PR_BODY = "Body of the Pull Request"

# GitHub personal access token with repo scope
ACCESS_TOKEN = "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"

# Create a GitHub API object
g = Github(ACCESS_TOKEN)

# Get the repository object
repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)

# Create the pull request
pr = repo.create_pull(title=PR_TITLE, body=PR_BODY, head=PR_HEAD, base=PR_BASE)

# Wait for GitHub actions to complete
while pr.get_commits().totalCount == 0:
    time.sleep(5)
    pr.update()
    print("Waiting for workflow checks to start...")

# Wait for workflow checks to complete
while True:
    checks = repo.get_commit(pr.head.sha).get_check_runs()
    success = all(check.conclusion == "success" for check in checks)
    if success:
        break
    else:
        time.sleep(5)
        print("Waiting for workflow checks to complete...")

# Merge the pull request
pr.merge()
print("Pull request merged successfully!")

# Print the added directories
print(added_dirs)