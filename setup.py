import setuptools

import sys
from os.path import dirname
# sys.path.append(dirname(__file__))
    
print("Setup...", sys.path)

setuptools.setup (
  name = 'clean-notion-files',
  version = '0.1',
  description = 'Clean notion files',
  url = 'https://github.com/jorgefranciscogil/clean-notion-files',
  author = 'Jorge Francisco Gil',
  author_email = 'jfrangcgmail.com',
  license = 'MIT',
  zip_safe = False,
  scripts=['clean-notion-files.py'],
  packages = setuptools.find_packages()
)

print("PACKAGES ---->>>>", setuptools.find_packages())