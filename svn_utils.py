"""
This file contains a few useful commands for interacting with a remote
svn repo via wrapped command line calls.

@author: stephen.huenneke@opower.com
"""

import os,subprocess

class SvnRepo:

    def __init__(self, log, args):
        self._repo_url = args.repo_url
        self._log = log
        self._args = args

    def get_svn_info(self, svn_path):
        info_lines = subprocess.Popen("svn info %s" % os.path.join(self._repo_url,svn_path), stdout=subprocess.PIPE, shell=True).stdout.read()
        return info_lines

    def get_svn_files(self, svn_root_dir):
        files = subprocess.Popen("svn ls %s" % os.path.join(self._repo_url,svn_root_dir), stdout=subprocess.PIPE, shell=True).stdout.read()
        files = files.split("\n")
        return filter(lambda x: x and x[-1] == "/", files)

    def get_svn_subdirs(self, svn_root_dir):
        return filter(lambda x: x and x[-1] == "/", self.get_svn_files(svn_root_dir))
