from copy import deepcopy
from zipfile import ZipFile
import sys

z1 = ZipFile(sys.argv[1], 'r')
z2 = ZipFile(sys.argv[2], 'w')
enc = sys.argv[3]

for info in z1.infolist():
    fixed_info = deepcopy(info)
    fixed_info.filename = info.filename.decode(enc)
    z2.writestr(fixed_info, z1.read(info.filename))
