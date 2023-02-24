import subprocess
from git import Repo
import os

def push_to_github(repo_path, commit_message, access_token, new_branch_name):
    # Create a GitPython Repo object for the specified repository path
    repo = Repo(repo_path)

    # Create a new branch and switch to it
    repo.create_head(new_branch_name)
    repo.heads[new_branch_name].checkout()

    # Add all changes to the staging area
    repo.index.add("*")

    # Create a new commit with the specified commit message
    repo.index.commit(commit_message)

    # Push changes to the remote repository using the provided personal access token
    remote_origin = repo.remote(name="origin")
    remote_url = remote_origin.url
    remote_url_with_token = remote_url.replace("https://", f"https://{access_token}@")
    remote_origin.set_url(remote_url_with_token)
    remote_origin.push(refspec=f"refs/heads/{new_branch_name}")


repo_path = "."
commit_message = "Commit message"
access_token = os.getenv("token")
new_branch_name = "new-branch-name"

push_to_github(repo_path, commit_message, access_token, new_branch_name)

