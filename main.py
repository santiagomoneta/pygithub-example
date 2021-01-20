# pyGithub demo
# Jan 2021
# By Santiago Moneta
# The goal is to demonstrate how to login, create files and updates files in github

from github import Github

# Login to github
# g = Github('username','password')
g = Github('**********token************')

# Get User from the token used to login
user = g.get_user()

# Load all user's repos for in memory
print()
repos = g.get_user(user.login).get_repos()

# Print all the user's repo names
print()
for repo in repos:
    print(repo.name)

# create a new repo named "sandbox"
print()
repo = user.create_repo("sandbox")

# Create a new file in the sandbox repo / master branch
# since the repo is new, there is no branches so master will be "created" as well.
print()
repo = g.get_repo(user.login+"/sandbox")
repo.create_file("test.txt", "commit message", "this is the file content", branch="master")

# create a developer branch from master
print()
sb = repo.get_branch('master')
repo.create_git_ref(ref='refs/heads/' + 'developer', sha=sb.commit.sha)

# Update the test.txt file in the developer branch with new content
print()
contents = repo.get_contents("test.txt", ref="developer")
repo.update_file(contents.path, "CommitMessage", "This is new content", contents.sha, branch="developer")

# Create pull request to merge the developer branch with the master branch
print()

body = '''
SUMMARY
Change HTTP library used to send requests

TESTS
 - [x] Send 'GET' request
 - [x] Send 'POST' request with/without body
'''
pr = repo.create_pull(title='Pull Request title', body=body, head="developer", base="master")
print()
print('Pull request #', pr.number, ' created.')
