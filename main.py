# pyGithub demo
# Jan 2021
# By Santiago Moneta
# The goal is to demonstrate how to login, create files and updates files in github

from github import Github
import string
import re

# Login to github
# g = Github('username','password')
g = Github('e9ab6bdaXXXXXXXXXXXXXXXXX5e2dc7d2db0')
print('--> Logged in')

# Get User from the token used to login
user = g.get_user()
print('--> Loaded username from token')

# Load all user's repos for in memory

repos = g.get_user(user.login).get_repos()
print('--> Loaded user repos')

# Print all the user's repo names

print('--> Print all repos:')
for repo in repos:
    print(repo.name)

# create a new repo named "sandbox"

repo = user.create_repo("sandbox")
print('--> Repository "sandbox" created.')

# Create a new file in the sandbox repo / master branch
# since the repo is new, there is no branches so master will be "created" as well.

repo = g.get_repo(user.login+"/sandbox")
body = '''
Line 1: Message
Line 2: Sample Text
Line 3: yet another line
'''
repo.create_file("test.txt", "commit message", body , branch="master")
print('--> File test.txt (master branch) created.')

# create a developer branch from master

sb = repo.get_branch('master')
repo.create_git_ref(ref='refs/heads/' + 'developer', sha=sb.commit.sha)
print('--> New branch "developer" created.')

# Replace text from line 2 in test.txt from developer branch

file = repo.get_contents("test.txt", ref="developer")
filePath = file.path
newFile = ((file.decoded_content).decode('utf-8')).replace("Sample Text","A way better and improved sample Text")
repo.update_file(filePath, "FileUpdated", newFile, file.sha, branch="developer")
print('--> File test.txt (developer branch) updated.')


# Create pull request to merge the developer branch with the master branch
body = '''
SUMMARY
Change HTTP library used to send requests

TESTS
 - [x] Send 'GET' request
 - [x] Send 'POST' request with/without body
'''
pr = repo.create_pull(title='Pull Request title', body=body, head="developer", base="master")

print('--> Pull request #', pr.number, ' created.')
