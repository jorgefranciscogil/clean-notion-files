## VSCode

Go to settings and add below entry to set relative path of your libraries:

`"python.envFile": "${workspaceFolder}/.env"`

Into `.env` file type:

`PYTHONPATH=./scripts/src:${PYTHONPATH}`
## Upgrade python

### Install python3.9

#### Linux

`sudo apt-get update && sudo apt-get upgrade`
`sudo apt-get install python3.9`

#### Mac OS

Install python through python environment (recomended):

`brew install pyenv`

Configuring and initializing:

`echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc`
`echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc`
`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init --path)"\nfi' >> ~/.zshrc`

[source 1](https://www.freecodecamp.org/news/python-version-on-mac-update/)
[source 2](https://stackoverflow.com/questions/33321312/cannot-switch-python-with-pyenv)

Note that your .zshrc file has changed.

cat `~/.zshrc`

To install a specific Python version, run:

`pyenv install <version>`

To list available versions:

`pyenv versions`

To select a version:

`pyenv global <version>`

> However, if you want install python 3 directly, you can type:
> `brew install python3`

#### Install pip

`sudo apt install python3-pip`

Check if pip 21.x.x was installed

`python3.9 -m pip --version`

Make sure your pip version has installed as latest

`python -m pip install -U pip`

## Run

`python -m pip install -e .` or `pip install -e .`

[Configuring metadata](https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata)

[setuptools](https://pythonhosted.org/an_example_pypi_project/setuptools.html)

`python -m truncate-files <source_path>`

**Example**

`$ ~[..]/scripts> python -m truncate-files ..`
