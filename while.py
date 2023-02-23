import subprocess
import os
token = os.getenv("token")

# Execute the `gh auth login` command and provide your personal access token as input
subprocess.run(["gh", "auth", "login", "--with-token"], input=f"{token}\n", text=True)