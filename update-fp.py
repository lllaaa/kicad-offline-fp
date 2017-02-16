#!/usr/bin/python

# update all the subfolders under localdir
# code modified from `codeboy2k`
# (deprecated)
# you can use
# $ git submodule update --recursive

import re
import os
import sys
import subprocess

# set localdir to the location where you want to
# store your local copy of the GitHub repository
d = './kicad'

env = {}
env.update(os.environ)
sep = ';' if (re.compile('^[wW][Ii][Nn]').match(sys.platform)) else ':'

args = ['git', 'submodule', 'update']
dirs = [x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))]

for dir in dirs:
    print(dir, ': ')
    sys.stdout.flush()
    os.chdir(os.path.join(d, dir))
    subprocess.call(args)
    os.chdir('../../')
