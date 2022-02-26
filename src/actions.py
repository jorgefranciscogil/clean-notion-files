import os
from src.NotionEntry.NotionEntry import NotionEntry

def walkdir(src):
  print(f'from... {src}\n')
  for entry in os.scandir(src):
    notionEntry = None
    _is = checkers(entry.path)
    isNotionFolder = entry.is_dir() and _is['notScriptsFolder'] and _is['notHiddenEntry']
    isNotionFile = entry.is_file() and _is['markdownFile']

    # Filer by notion file
    if isNotionFolder or isNotionFile:
      notionEntry = NotionEntry(entry.path)
      if isNotionFolder:
        notionEntry.createTargetFolder()
      if isNotionFile:
        notionEntry.createTargetFile()
    
    if entry.is_dir() and not notionEntry is None:
      # Recursive called
      walkdir(notionEntry.getPath())
      # When returns from folder and therefore it has already renamed, remove source folder.
      notionEntry.removeSourceFolder()

def checkers(entryPath):
  print("entryPath ----->>>>>", entryPath, os.path.basename(entryPath))
  return {
    'notHiddenEntry': not os.path.basename(entryPath).startswith('.'),
    'notScriptsFolder': os.path.basename(entryPath) != 'clean-notion-files',
    'markdownFile': entryPath.endswith(".md")
  }