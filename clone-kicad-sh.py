#!/usr/bin/python

# clone the pretty modules specified by fp-lib-table.for-pretty
# under localdir, to the folder localdir
#
# code modified from `codeboy2k`

import re
import os
import sys
import subprocess

# set localdir to the location where you want to
# store your local copy of the GitHub repository
# localdir = '/usr/local/share/kicad/github-repo'
localdir = './kicad/'

orig_table = 'fp-lib-table.stefan'

env = {}
env.update(os.environ)
sep = ';' if (re.compile('^[wW][Ii][Nn]').match(sys.platform)) else ':'
KIGITHUB = 'https://github.com/StefanHamminga'
args = ['git', 'submodule', 'add', '--quiet', 'x']

os.chdir(localdir)

template = orig_table
for line in open(template, 'rU'):
    mo = re.search(r'^.*\(\W*uri\W?([^)]*).*$', line)
    if mo:
        repo = mo.group(1).replace('${KISYSMOD}', KIGITHUB)
        # print(repo)
        args[4] = repo
        # print(localdir)
        # print(args)
        subprocess.call(args)
        # print('done x')

print("you now have a local copy of the GitHub repository")
print("in : ", localdir)
print("updating KiCad ... ")

print(".. done")
print("before running kicad, you will need to set")
print("the following environment variable:")
print("KISYSMOD=%s\n" % localdir)
