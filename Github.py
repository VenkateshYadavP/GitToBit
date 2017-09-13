
from github3 import Github # pip install PyGithub

GH_USERNAME = 'UserName'
GH_PASSWORD = 'Password'

## Get list of all your github private repos.
## By default we filter out public repos and repos where you are not the owner. You can change this.
g = Github(GH_USERNAME, GH_PASSWORD)
print(g)
theRepos = []
for repo in g.get_user().get_repos():
    g.repos.delete(repo.name)
