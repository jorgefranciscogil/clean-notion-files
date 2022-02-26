import os
from src import actions

currentDir = os.getcwd()
print("currentDir", currentDir)

if __name__ == '__main__':
    actions.walkdir(currentDir)