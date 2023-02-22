import subprocess
import os
import requests
import logging
import json
from subprocess import call
import sys
import time
import git
from git import Repo
pk_repo_path = "./"
ATH_OF_GIT_REPO = r'.\.git' 
repo = Repo(pk_repo_path)
subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)
gh_version = call(["gh", "--version"])
logging.info("authenticating to github with token" )
#Logging into GitHub using Token
# GH_TOKEN = os.environ['GH_TOKEN']
# username = 'prabhukiran9999'
# github_login = requests.get('https://api.github.com/user', auth=(username,GH_TOKEN))
# if github_login.status_code == 200:
#     print ('logged into github successfully!')
# else:
#     print ('logged into github failed')

# Execute project cteation script

try :
    subprocess.call(['./project_set_admin.sh'])
except subprocess.CalledProcessError as e:
    print(e)

project_Set_info = subprocess.Popen(["git", "ls-files", "--others", "--directory", "--exclude-standard"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip()
checkout_branch_name = project_Set_info.strip("/")
print(checkout_branch_name)
#Create a new branch
checkout_branch = repo.git.branch(checkout_branch_name)
# Push the branch
repo.git.push("origin", checkout_branch_name)
#To do Get the Folder info the script created
# PATH_OF_GIT_REPO = r'./.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    # To do add a section to creaate a branch and checkout to new branch
    branch = checkout_branch_name
    repo = Repo('.')
    repo.git.add(all=True)
    repo.index.commit(COMMIT_MESSAGE)
    repo.git.push('origin', branch)
    

git_push()

create_pr = subprocess.Popen(["gh", "pr", "create", "-t created a new project set", "-b created a new project set using provisonor script", "-rsvalmiki1102"],stdout=subprocess.PIPE).communicate()[0] 
pr_url = create_pr.decode("utf-8").rstrip() 
# pr_url = create_pr.strip("b'") 
# print(creaate_pr)
print ('Pull_request created successfully')
#Sleep for 5 sec after pull request is created so the actions will register
time.sleep(5) #Sleep for 5 secs
print(type(create_pr))
print(pr_url)

# Check for pull request actions to complete

# check_pr = subprocess.Popen(["gh", "pr", "checks", pr_url, "--watch"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip()
check_pr = json.loads(subprocess.Popen(["gh", "pr", "view", pr_url, "--json", "statusCheckRollup"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip())
print(check_pr)
workflow_id = str(json.loads(subprocess.Popen(["gh", "run", "list", "-b", "ProjectSet-Automation", "-L", "1", "--json", "databaseId"],stdout=subprocess.PIPE).communicate()[0])[0]['databaseId'])
def pr_workflow_status(workflow_id,pr_url):
    # workflow_id = str(json.loads(subprocess.Popen(["gh", "run", "list", "-b", "dev", "-L", "1", "--json", "databaseId"],stdout=subprocess.PIPE).communicate()[0])[0]['databaseId'])
    workflow_status = ""
    while workflow_status != "completed":
        workflow_status = json.loads(subprocess.Popen(["gh", "run", "view", workflow_id, "--json", "status"],stdout=subprocess.PIPE).communicate()[0])['status']
        print(workflow_status)
        if workflow_status =='queued':
            print(workflow_status)
            # workflow_status = json.loads(subprocess.Popen(["gh", "pr", "view", pr_url, "--json", "statusCheckRollup"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip())["statusCheckRollup"][0]['status']
            continue
        elif workflow_status == " ":
            # workflow_status = json.loads(subprocess.Popen(["gh", "pr", "view", pr_url, "--json", "statusCheckRollup"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip())["statusCheckRollup"][0]['status']
            print(workflow_status)
            continue
        elif workflow_status == "completed":
            print(workflow_status)
            merge_pr = subprocess.call(["gh", "pr", "merge", pr_url, "--admin", "-m"])
            if merge_pr == 0:
                print(f"Pull request,{pr_url} merged successfully")
                time.sleep(5)
            else:
                print(f"problem merging a PR,{pr_url}")
            break
        elif workflow_status =="failed":
            print("Push workflow failed")
            break

def push_workflow_status(push_workflow_id):
    push_workflow_status = ""
    while push_workflow_status != "completed":
        push_workflow_status = json.loads(subprocess.Popen(["gh", "run", "view", push_workflow_id, "--json", "status"],stdout=subprocess.PIPE).communicate()[0])['status']
        print(push_workflow_status)
        if push_workflow_status =='queued':
            print(push_workflow_status)
            # workflow_status = json.loads(subprocess.Popen(["gh", "pr", "view", pr_url, "--json", "statusCheckRollup"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip())["statusCheckRollup"][0]['status']
            continue
        elif push_workflow_status == "in_progress":
            # workflow_status = json.loads(subprocess.Popen(["gh", "pr", "view", pr_url, "--json", "statusCheckRollup"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip())["statusCheckRollup"][0]['status']
            print(push_workflow_status)
            continue
        elif push_workflow_status == "completed":
            print(push_workflow_status)
            return push_workflow_status
        elif workflow_status =="failed":
            print("Push workflow failed")
            return push_workflow_status

pr_workflow_status(workflow_id,pr_url)
time.sleep(5)

push_workflow_id = str(json.loads(subprocess.Popen(["gh", "run", "list", "-b", "main", "-L", "1", "--json", "databaseId"],stdout=subprocess.PIPE).communicate()[0])[0]['databaseId'])

push_status = push_workflow_status(push_workflow_id)
print(push_status)

if push_status == "completed":
    try :
        layer_creation = subprocess.call(['./project_set_admin.sh'])
        if layer_creation == 0:
            print("layers created seccussfully") 
        else:
            print(f"problem creating pull request for layers")
    except subprocess.CalledProcessError as e:
        print(e)
else:
    print("Push workflow for accounts failed")

git_push()

layer_pr = subprocess.Popen(["gh", "pr", "create", "-t created a new project set", "-b created a new project set using provisonor script", "-rsvalmiki1102"],stdout=subprocess.PIPE).communicate()[0] 
pr_url = layer_pr.decode("utf-8").rstrip() 
# print(layer_pr_url)
print ('Pull_request for layers created successfully')
# #Sleep for 5 sec after pull request is created so the actions will register
time.sleep(5) #Sleep for 5 secs
# print(type(layer_pr))
print(pr_url)

workflow_id = str(json.loads(subprocess.Popen(["gh", "run", "list", "-b", "ProjectSet-Automation", "-L", "1", "--json", "databaseId"],stdout=subprocess.PIPE).communicate()[0])[0]['databaseId'])
pr_workflow_status(workflow_id,pr_url)
time.sleep(5)
push_workflow_id = str(json.loads(subprocess.Popen(["gh", "run", "list", "-b", "main", "-L", "1", "--json", "databaseId"],stdout=subprocess.PIPE).communicate()[0])[0]['databaseId'])

push_status = push_workflow_status(push_workflow_id)
print(push_status)