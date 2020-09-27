# Developer Guide

## Table of Contents
- [Motivation and Intent](#motivation-and-intent)
- [Coding Style Guide](#coding-style-guide)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [Merging](#merging)

## Motivation and Intent
Provide a way for people to contribute updates, fix bugs, try out ideas, etc.


## Coding Style Guide
### Tools
The following tools are used as standard.

* [mypy] - python's static type checker
* [black] - opinionated python linter 

[mypy]: http://mypy-lang.org/
[black]: https://github.com/psf/black

When you submit a pull request the CI, Github Actions, will run these tools automatically. 

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
  


## Getting Started
To get started, pick your favorite editor, create a virtual environment and then run:

```shell
poetry install
```

This will install all of the dependencies needed to run the software.  To run, please run:

```shell script
python -m scripts
```

## Testing
Updates to the software should also include updates to testing where needed and possible.  Please add where
 appropriate, if you can
.  To
run the current suite of tests, simply run:

```shell
pytest --cov=nqp
```

## Merging
To include any changes into the NQP engine you can submit a pull request. 

Any pull request must pass mypy's typing check
 and must remain compatible with the building of the [Sphinx] documentation, so that the docs are always up to date
 . As you'd expect, all tests must pass, too.
 
[Sphinx]: https://www.sphinx-doc.org/en/master/  
