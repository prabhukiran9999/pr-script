import subprocess
import os
import requests
import logging
from subprocess import call
import sys
from git import Repo
pk_repo_path = "./"
repo = Repo(pk_repo_path)
subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
gh_version = call(["gh", "--version"])
logging.info("authenticating to github with token" )
#Logging into GitHub using Token
GH_TOKEN = os.environ['GH_TOKEN']
username = 'prabhukiran9999'
github_login = requests.get('https://api.github.com/user', auth=(username,GH_TOKEN))
if github_login.status_code == 200:
    print ('logged into github successfully!')
else:
    print ('logged into github failed')

# Execute project cteation script

try :
    subprocess.call(['./project_set_admin.sh'])
except subprocess.CalledProcessError as e:
    print(e)
finally:
    status = repo.git.status()
    print(status)
  
