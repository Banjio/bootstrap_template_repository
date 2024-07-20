# A modern Python Project Template

This project aims to be a simple yet modern template for python projects using the following tools:

* __poetry__ for package management 
* __Ruff__ for linting and formatting
* __pytest__ for testing and pytest-cov for test coverage
* __pylance (pyright)__ or __mypy__ for static type checking
* __rich__ as drop in replacement for printing
* __ipython__ for a better REPL experience
* __mkdocs__ as docs generator
* __pyproject.toml__ for configuration

Here is an awesome list of possible tools https://github.com/ml-tooling/best-of-python-dev

For all tools a sensible default configuration is provided in a pyproject.toml, which can be edited to further fit to once needs ruff 

# Setups

Some tools need an initial setup, and some can be installed by using the poetry files. 
Some tools can be reinitiated using their cli tools. Maybe this can be automated with cookiecutter

## poetry

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

## Pytest

*  Is automatically setup using pyproject.toml

## Ruff

* Is automatically setup using pyproject.toml

## Mypy

* Is setup using the pyproject.toml however currently no configuration is done

## Mkdocs

* Run `mkdocs new project_name` to generate the template or just edit the existing one. 
* `mkdocs serve` opens a live server
* Adding material theme will make it look very nice https://github.com/squidfunk/mkdocs-material

Various plugins exist that can be found here https://github.com/mkdocs/catalog, for example for automatic api docs from docstrings etc

# Notes about vscode extensions

Some tools used in this template are also available as vscode-plugins making working with them more native in vscode: 

* ruff (charliermarsh.ruff)
* mypy (ms-python.mypy-type-checker)

# Improvement plans

https://gotofritz.net/blog/creating-a-poetry-driven-python-project-template-with-cookiecutter/#specimen-setup-safety

This project has some valid additions to this project, e.g. safety and a sphinx

* ruff pre-commit-hook
* mypy pre-commit-hook?