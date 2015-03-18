#!/usr/bin/python

from copy import deepcopy
from zipfile import ZipFile
import sys

def usage():
    print 'usage:', sys.argv[0], 'zip-in', 'zip-out', 'encoding'

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
            fixed_info.filename = info.filename.decode(enc)
        except:
            print 'Encoding', enc, 'does not seem to be right'
            sys.exit(1)
        z2.writestr(fixed_info, z1.read(info.filename))

if __name__ == '__main__':
    main()
