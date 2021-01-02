# -*- coding:utf-8 -*-
__author__ = 'liuxiaotong'

from pprint import pprint

from github import Github


def get_repo(repo_full_name):
    return Github().get_repo(repo_full_name)


def get_repo_owner_github_id(repo_full_name):
    g = Github()
    repo = g.get_repo(repo_full_name)
    return repo.owner.id


if __name__ == "__main__":
    print(get_repo_owner_github_id('timbby/flask'))
    _repo = get_repo('timbby/flask')
    branch = _repo.get_branch('master')
    # pprint(branch.__dict__)
    commit = branch.commit
    # pprint(branch.commit)
    # pprint(branch.commit.parents)
    for i in range(20):
        _ = commit.parents
