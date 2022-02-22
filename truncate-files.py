import sys
from actions import getParams, walkdir

rootDir = getParams(sys.argv)

# os.rename('../Definitive frontend 2021 28a5bfcea3b84955a7247a42c83deaad', '../Definitive frontend 2021')

walkdir(rootDir)