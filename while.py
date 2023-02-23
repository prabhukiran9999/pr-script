import git

repo = git.Repo('.')

# Get the commit diff between the current and previous commit
diff = repo.git.diff('HEAD~1', 'HEAD', name_status=True)

# Filter the added directories
added_dirs = set()
for line in diff.split('\n'):
    status, path = line.split('\t')
    if status == 'A' and path.endswith('/'):
        added_dirs.add(path)

# Print the added directories
print(added_dirs)