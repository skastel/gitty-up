# GittyUp

Manage your various git-svn repos and maintain an up to date clone of
the master SVN repo. By default, the script assumes you have the a
shell alias of $R to your svn remote repo, if you don't you can always
use

@author: stephen.huenneke@opower.com

# Requirements
The only requirement is a vanilla install of Python 2.7.

# Usage:
Manage your local git-svn repos [-h] [-r REPO_URL] [-p REPO_PATH]
                                       [-d REPO_DIR] [-n] [-u] [-f]
                                       [--check-for-changes]
                                       [--check-for-unpublished]
                                       [--max-lookback-revisions MAX_REVISIONS]
                                       [-v] [-s SKIP_DIRS]

optional arguments:
  -h, --help            show this help message and exit
  -r REPO_URL, --svn-url REPO_URL
                        The url of the remote svn repo, defaults to the $R
                        shell variable
  -p REPO_PATH, --path REPO_PATH
                        The path from the root svn/local repo path
  -d REPO_DIR, --local-dir REPO_DIR
                        The path to your local repo, defaults to the
                        $workspace shell variable
  -n, --find-new-projects
  -u, --update
  -f, --fetch
  --check-for-changes
  --check-for-unpublished
  --max-lookback-revisions MAX_REVISIONS
                        Used in conjuction with check-for-unpublished,
                        specifies a maximum number of past revisions to
                        examine, default is 10.
  -v, --verbose
  -s SKIP_DIRS, --skip-dir SKIP_DIRS
                        Skip all directory paths that match this arg

# Examples:

Update repos on a path:
 [~]$ gitty-up --update -p libs

Fetch svn branches on a path:
 [~]$ gitty-up --fetch -p libs

Find projects missing from local checkout:
 [~]$ gitty-up --find-new-projects -p libs

Fetch svn branches on a path:
 [~]$ gitty-up -fun -p libs -s settings -s content
