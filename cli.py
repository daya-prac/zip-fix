#!/usr/bin/python

from __future__ import print_function
from __future__ import unicode_literals

from copy import deepcopy
from zipfile import ZipFile
import sys

def usage():
    print('usage: %s zip-in zip-out encoding' % sys.argv[0])

def main():
    if len(sys.argv) < 4:
        usage()
        sys.exit(1)
    z1 = ZipFile(sys.argv[1], 'r')
    z2 = ZipFile(sys.argv[2], 'w')
    enc = sys.argv[3]
    for info in z1.infolist():
        fixed_info = deepcopy(info)
        try:
            fixed_info.filename = info.filename.encode('cp437').decode(enc)
        except Exception as ex:
            print(ex)
            sys.exit(1)
        z2.writestr(fixed_info, z1.read(info.filename))

if __name__ == '__main__':
    main()
