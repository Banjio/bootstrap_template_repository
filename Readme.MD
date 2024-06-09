# A modern Python Project Template

This project aims to be a simple yet modern template for python projects using the following tools:

* poetry for package management 
* Ruff for linting and formatting
* pytest for testing and pytest-cov for test coverage
* pylance (pyright) for static type checking
* rich as drop in replacement for printing
* ipython for a better REPL experience
* TBD: Docs Generator

Here is an awesome list of possible tools https://github.com/ml-tooling/best-of-python-dev

For all tools a sensible default configuration is provided in a pyproject.toml, which can be editet to furhter fit to once needs ruff 

## Setup Poetry 

All dependencies we need for our project template can be installed inside a virtual environment and thus be configured inside a requirements file. Poetry is an exception to this because we need it for our dependency management. Thus, we have to install it separately. The good thing is this only needs to be done once, and then we can always can use our created template with poetry.

The official recommended way to install poetry is via pipx. If you do not have it installed see the official installation guide https://pipx.pypa.io/stable/. 

On arch one can run 

```bash
sudo pacman -Sy python-pipx
```

Afterwards we can install poetry with

```bash
pipx install poetry
```

This ensures that poetry is installed in an isolated way and does not interfer with system wide installations.

Tab completion for your console can be useful and configured with https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh

