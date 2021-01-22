# pygithub-example
Simple example of the usage of the PyGithub python module


Source:
https://pygithub.readthedocs.io/en/latest/introduction.html

This only works with Python 2.7

The main goal of this script is to be used as a starting point for anyone who want to work with repos using python and avoid mimmicin que huma behaviour (for example using the os module and the regular git commands).

This sample script will:

1) Login into github using a personal access token.
2) Get and print all the repos for the user under the token.
3) create a new repo called "sandbox", with a sample file (test.txt) in the master branch.
4) Create a new developer branch based on master.
5) Update part of the content in text.txt (developer branch).
6) Create a pull request to merge developer into master.

