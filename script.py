import time
from git import Repo
num = None
file_name = None
repo_path = '/Users/mkg/Downloads/leetcode'
repo = Repo(repo_path)
while True:
    s = input()
    if s.lower() == 'done':
        repo.index.add([file_name])
        repo.index.commit(f"added {num}")
        # repo.remotes[0].push()
        current_branch = repo.active_branch.name
        repo.remotes.origin.push(refspec=f"HEAD:refs/heads/{current_branch}")
    else:
        arr = s.split()
        arr[0] = arr[0][:-1]
        num = arr[0]
        time.sleep(0.05)
        file_name = "_".join(arr) + ".py"
        print(file_name)