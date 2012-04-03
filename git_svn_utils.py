"""
A utility class with some useful ways of interacting with a git-svn
repo.  Basically just a wrapper for the command line.

@author: stephen.huenneke@opower.com
"""

import re
import os,subprocess
import svn_utils

class GitSvnRepo:

    def __init__(self, directory, log, args):
        self._directory = directory
        self._log = log
        self._args = args

    def get_unpushed_commits(self):
        os.chdir(self._directory)
        result = subprocess.Popen("git log -n %s" % self._args.max_revisions, shell=True, stdout=subprocess.PIPE)
        commits_re = re.compile('(.^commit [a-f0-9]+.)', flags=re.M | re.S)
        git_log = result.stdout.read()
        commits = re.split(commits_re, git_log)
        unpushed_commits = []
        for commit in commits:
            if re.search('git-svn-id: \w+', commit):
                break
            else:
                unpushed_commits.append(commit)
        if unpushed_commits:
            self._log.info("%s has unpushed commits." % self._directory)
            if self._args.verbose:
                for commit in unpushed_commits:
                    self._log.debug("Unpushed commit:\n%s" % commit)
        else:
            self._log.debug("No unpushed commits for %s" % self._directory)

    def fetch_svn_branches(self):
        os.chdir(self._directory)
        self._log.debug("Fetching branches and updates for %s" % self._directory)
        result = subprocess.call('git svn fetch', shell=True)
        if result != 0:
            # A problem occured! Eep!
            self._log.error("Error rebasing %s" % self._directory)
            exit(result)
            
    def update_git_svn(self):
        os.chdir(self._directory)
        local_changes = self.has_changes()
        if local_changes:
            self._log.debug("Stashing uncommitted changes in %s" % self._directory)
            subprocess.call('git stash', shell=True)

        self._log.debug("Rebasing from subversion %s" % self._directory)
        result = subprocess.call('git svn rebase', shell=True)
        if result != 0:
            # A problem occured! Eep!
            self._log.error("Error rebasing %s" % self._directory)
            exit(result)

        if local_changes:
            self._log.debug("Unstashing uncommitted changes in %s" % self._directory)
            result = subprocess.call('git stash pop', shell=True)
            if result != 0:
                # A problem occured! Eep!
                self._log.error("Error rebasing %s" % self._directory)
                exit(result)

    def has_changes(self):
        os.chdir(self._directory)
        self._log.debug("Checking for changes in %s" % self._directory)
        git_status = subprocess.Popen('git status', shell=True, stdout=subprocess.PIPE).stdout.read()
        if not re.search('Changes[\s\w]+commit[\s\w]*:', git_status, re.M):
            self._log.debug("No changes staged or uncommitted on %s" % self._directory)
            return False
        self._log.debug("Found changes staged or uncommitted on %s" % self._directory)
        self._log.debug("Status:\n%s", git_status)
        return True

    def check_for_updates(self):
        self._log.error("TODO: make this actually look for unstaged changes.")
        return

    def check_for_dcommits(self):
        self._log.error("TODO: make this actually look for dcommits.")
        return


