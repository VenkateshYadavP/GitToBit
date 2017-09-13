import os
import subprocess
import glob
from github import Github # pip install PyGithub
from bitbucket.bitbucket import Bitbucket # pip install --user bitbucket-api

GH_USERNAME = 'USERNAME'
GH_PASSWORD = 'PASSWORD'

BB_USERNAME = 'USERNAME'
BB_PASSWORD = 'PASSWORD'

## Set up
d = os.path.expanduser('~/Desktop/Public_Repos')
if not os.path.exists(d):
    os.makedirs(d)
os.chdir(d)

## Get list of all your github private repos.
## By default we filter out public repos and repos where you are not the owner. You can change this.
g = Github(GH_USERNAME, GH_PASSWORD)
print(g)
theRepos = []
for repo in g.get_user().get_repos():
    print(theRepos)
    theRepos.append((repo.name, repo.clone_url))
    os.system('gh re --delete '+ repo.name)

### Go through all the cloned directories, create a bitbucket repo and then push them
### If the repo already exists on github this will skip it.
