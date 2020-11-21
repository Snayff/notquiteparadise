# Developer Guide

## Table of Contents
- [Motivation and Intent](#motivation-and-intent)
- [Coding Style Guide](#coding-style-guide)
- [Contributing](#contributing)

## Motivation and Intent
Provide a way for people to contribute updates, fix bugs, try out ideas, etc.


## Coding Style Guide
### Tools
The following tools are used as standard to ensure a consistent and reliable codebase.
 
* [pytest] - python testing library. 
* [mypy] - python's static type checker.
* [black] - opinionated python linter.
* [isort] - manage the order of imports. 

[pytest]: https://docs.pytest.org/en/stable/
[mypy]: http://mypy-lang.org/
[black]: https://black.readthedocs.io/en/stable/
[isort]: https://pycqa.github.io/isort/

When you submit a pull request the CI, Github Actions, will run  pytext and mypy automatically. Out of courtesy, black and isort, which change your code, are ready for you to use but are not applied directly.  

### Naming conventions
Below are the naming conventions followed in this project:
* If only one of a class should exist the creation function is called "init_[object]", otherwise "create_[object]".
* Where the object is taken as an argument the function name should default to "create_[object_type]".
* If checking a bool use IsA or HasA.
* If setting a variable from statically held data prefix with "load_[data]"
* Where a variable name contains "name" the variable may include spaces and other special characters. Where it
 includes "key" it may contain
 alphanumeric values only.
* Arguments should be in a consistent order:
  1. Identifiers (entity, skill)
  2. Affected items (position, tiles)
  3. Qualifiers
* Externally held data should be defined in a dataclass in definitions.py.
  


## Contributing
### Getting started
To get started, [fork the repo] and open it up in your favorite editor. Then, open your terminal and point it to
 where you just saved the repo and then run:

```shell
poetry install
```

This will install all of the dependencies needed, using [poetry].  

To run the program use:

```shell script
python -m scripts
```

If you're not sure where to start helping out you can look at the existing feature requests and issues, [here]. Pick
 one you think you'd like to tackle and make the relevant changes to your fork. 
 
[fork the repo]: https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo
[poetry]: https://python-poetry.org/
[here]: https://github.com/Snayff/notquiteparadise/issues
 
### Testing
Updates to the code should ideally include updates to the test suite. Please add new tests to support your changes, if
 you can. At the very least, as you'd imagine all tests must pass before code can be merged.
  
To run the current suite of tests and confirm they're all passing, use:

```shell
pytest --cov=nqp
```

And to check that all the types are what they should be:
```shell
mypy
```
 
### Merging
When you're ready, submit a [pull request] to have your changes added to the main repository. Any pull request must
 the checks in the Github Actions, currently mypy type checking and pytest's testing. The code must remain compatible with the building of the [Sphinx] documentation, so that the docs are always up to date. 
 
[Sphinx]: https://www.sphinx-doc.org/en/master/  
[pull request]: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request

### Existing Issues
If you find any problems in the existing code you can raise a [new issue] on GitHub.

[new issue]: https://github.com/Snayff/notquiteparadise/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D







