import re, shutil, os, urllib.parse
class NotionEntry:

  # RegExp for Notion file token
  NOTION_ENTRY_TOKEN = '\s[0-9a-f]+'
  NOTION_FOLDER_TOKEN = '\s[0-9a-f]+\/'
  NOTION_FILE_TOKEN = '\s[0-9a-f]+\.' 

  def __init__(self, path):
    self.__path = path
    # set cleaned path
    self.cleanedPath = self.__removeTokensFromPath(self.__path)

  def getPath(self):
    return self.__path

  def tryMove(self):
    if self.__path != self.cleanedPath:
      shutil.move(self.__path, self.cleanedPath)

  def createTargetFile(self):
    # get source file
    backupPath = self.__backup(self.__path)
    print("---->>> FILE ---->>>>", self.__path)
    fin = open(backupPath, 'rt')
    fout = open(self.cleanedPath, 'w+')
    newLine = ""
    mainTitle = ""
    for line in fin:
      newLine = line
      if self.__isMainTitle(newLine) and not mainTitle:
        mainTitle = line
        print("MAIN TITLE!!!", mainTitle)
      # print("newLine", newLine)
      if self.__isNotionLink(line):
        # Group 1: \[.*\] ; Group 2: \.*
        matchedLine = re.search('(\[.*\])\((.*)\)', line)
        quoteUrl = matchedLine.group(2)
        newLine = rf"{matchedLine.group(1)}({self.__removeTokensFromLine(quoteUrl)})"
      fout.write(newLine)
    fin.close()
    fout.close()
    os.remove(backupPath)
  
  def createTargetFolder(self):
    if not os.path.exists(self.cleanedPath):
      os.makedirs(self.cleanedPath)

  def removeSourceFolder(self):
    try:
      if os.path.exists(self.__path):
        os.rmdir(self.__path)
    except OSError as e:
      print("Error: %s : %s" % (self.__path, e.strerror))
      shutil.rmtree(self.__path, ignore_errors=True)

  def __backup(self, path):
    backupPath = re.sub(r'\.md', '.backup.md', path)
    backupCleanedPath = self.__removeFileTokenFromPath(backupPath)
    os.rename(path, backupCleanedPath)
    return backupCleanedPath

  def __removeTokensFromPath(self, path):
    pathWithoutFolderTokens = self.__removeFolderTokensFromPath(path)
    pathWithoutTokens = self.__removeFileTokenFromPath(pathWithoutFolderTokens)
    return pathWithoutTokens

  def __getMainTitle(self, path):
    pass

  def __removeFolderTokensFromPath(self, path):
    pathWithoutFolderTokens = re.sub(rf'{self.NOTION_FOLDER_TOKEN}', "/", urllib.parse.unquote(path))
    pathWithoutFolderTokens = re.sub(rf'{self.NOTION_ENTRY_TOKEN}', "", urllib.parse.unquote(pathWithoutFolderTokens))
    return pathWithoutFolderTokens
  
  def __removeFileTokenFromPath(self, path):
    pathWithoutToken = re.sub(rf'{self.NOTION_FILE_TOKEN}', ".", path)
    return pathWithoutToken
  
  def __removeTokensFromLine(self, quoteUrl):
    unquoteUrlWithoutTokens = self.__removeTokensFromPath(quoteUrl)
    quoteUrlWithoutToken = urllib.parse.quote(unquoteUrlWithoutTokens)
    return quoteUrlWithoutToken

  def __isNotionLink(self, line):
    isNotionLink = False
    matchedLine = re.search('(\[.*\])\((.*)\)', line)
    if matchedLine is not None:
      isNotionLink = bool(re.search(rf'{self.NOTION_FILE_TOKEN}', urllib.parse.unquote(matchedLine.group(2))))
    return isNotionLink
  
  def __isMainTitle(self, line):
    matchedLine = re.search('^([#]{1}\s)(.+)$', line)
    return matchedLine
