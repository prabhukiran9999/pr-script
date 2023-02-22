import subprocess
# import json
# # review_decession = ""
# # workflow_status=gh pr view https://github.com/prabhukiran9999/pr-script/pull/31 --json statusCheckRollup | jq '.statusCheckRollup[0]["status"]'
# # workflow_status = json.loads(subprocess.Popen(["gh", "pr", "view", "https://github.com/prabhukiran9999/pr-script/pull/31", "--json", "statusCheckRollup"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip())
# # status_check = json.loads(workflow_status)
# # print(workflow_status["statusCheckRollup"][0]['status'])
# # print(type(workflow_status))

# # merge_pr = subprocess.Popen(["gh", "pr", "merge", "https://github.com/prabhukiran9999/pr-script/pull/47", "--admin", "-m"],stdout=subprocess.PIPE).communicate()[0]
# # print(merge_pr.decode("utf-8").rstrip())

# push_worflow_status = json.loads(subprocess.Popen(["gh", "run", "view",  "4128925841", "--json", "status"],stdout=subprocess.PIPE).communicate()[0])['status']
# print(push_worflow_status)

# x = 2
# x = 4
# print(x)
x = subprocess.Popen(["git", "ls-files", "--others", "--directory", "--exclude-standard"],stdout=subprocess.PIPE).communicate()[0].decode("utf-8").rstrip()
# x ="get/category/".strip("/")"
branch = x.strip("/")
print(branch)
# subprocess.Popen(["gh", "pr", "create", "-t created a new project set", "-b created a new project set using provisonor script", "-rsvalmiki1102"],stdout=subprocess.PIPE).communicate()[0] 