# Developer Guide

## Motivation
Provide a way for people to contribute updates, fix bugs, try out ideas, etc.


## Design Philosophies 
* **Flow** - Periods of impetus to ensure the player is driven forward appropriately. Periods of openness to allow self
 pacing, reflection and exploration.
* **Coherent** - Information pertinent to the player is always made available and easy to parse, utilising a mix of
 art and text. Avoid need for external resource use e.g. a wiki.
* **Flexible**  - Never a best way, always a different one. The only limitations in place should be those that drive
 diversity of play.
* **Accessible** - Supports different kinds of players, e.g. can use keyboard, mouse or controller interchangeably, with
 minimal
 difference in experience. e.g. Colour scheme is colour-blind aware.
* **Customisable** - Near-core game settings can be influenced or set by the player allowing for extensive
 personalisation.

## Coding Style Guide
There are a number of conventions followed, including using the following tool:

* [mypy] - python's static linter

[mypy]: http://mypy-lang.org/

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
Updates to the software should also include updates to testing where needed.  Please add where appropriate.  To
run the current suite of tests, simply run:

```shell
pytest
```

## Merging
To include any development into NQP you can submit a pull request. 

Any pull request must pass mypy's typing check
 and must remain compatible with the building of the [Sphinx] documentation so that the docs are always up to date. 
 
[Sphinx]: https://www.sphinx-doc.org/en/master/  
