#!/usr/bin/python

# make the name of all the folders in localdir as the
# entries in fp-lib-table
# i.e., generate fp-lib-table.for-pretty under current folder

import re
import os
import sys
import shutil

# set localdir to the location where you want to
# store your local copy of the GitHub repository
d = './kicad'

env = {}
env.update(os.environ)
sep = ';' if (re.compile('^[wW][Ii][Nn]').match(sys.platform)) else ':'

dirs = [x for x in os.listdir(d) if os.path.isdir(os.path.join(d, x))]

fp_new = os.path.join(d, 'fp-lib-table.new')
fkisysmod = open(fp_new, 'w')
fkisysmod.write('(fp_lib_table\n')
for dir in dirs:
    # print(dir, ': ')
    mo = re.search(r'^.*[.]pretty$', dir)
    if mo:
        s = str(mo.group())
        fp, _ = os.path.splitext(s)
        # 2016-12-17: change KISYSMOD to KIGITHUB
        line = '  (lib (name ' + fp + ')(type KiCad)(uri ${KIGITHUB}/' + s + \
               ')(options "")(descr "offline kicad footprint"))'
        fkisysmod.write(line + '\n')
    sys.stdout.flush()
fkisysmod.write(')')
fkisysmod.close()

# Warning:
# please replace <postgres> with your own user name
env['HOME'] = 'C:/Users/postgres/AppData/Roaming/kicad'
topath = os.path.join(env['HOME'], 'fp-lib-table')

print(".. copying: ", fp_new)
print("......  to: ", topath)
print("warning: overwrite default")
shutil.copyfile(fp_new, topath)

print(".. done")
print("before running kicad, you will need to set")
print("the following environment variable:")
print("KISYSMOD=%s\n" % d)
