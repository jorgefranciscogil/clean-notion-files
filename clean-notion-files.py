import sys, os

from src import actions
# from . import .src.actions
# import .src.actions

# rootDir = actions.getParams(sys.argv)
currentDir = os.getcwd()

# print("rootDir", rootDir)
print("currentDir", currentDir)
print(__name__)

if __name__ == '__main__':
    actions.walkdir(currentDir)