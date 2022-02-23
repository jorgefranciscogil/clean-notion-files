import sys
from actions import getParams, walkdir

rootDir = getParams(sys.argv)

walkdir(rootDir)