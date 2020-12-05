Developer Guide
======================

So you want to contribute to Not Quite Paradise? Huzzah! Any support is welcome and greatly appreciated!

Tools Used
-------------------

The following tools are used as standard to ensure a consistent and reliable codebase.

* `pytest <https://docs.pytest.org/en/stable/>`_ - a testing library.
* `mypy <http://mypy-lang.org/>`_ - a static type checker.
* `black <https://black.readthedocs.io/en/stable/>`_ - an opinionated `linter <https://en.wikipedia.org/wiki/Lint_(software)>`_.
* `isort <https://pycqa.github.io/isort/>`_ - manage the order of imports.

When you submit a pull request the CI, Github Actions, will run  pytext and mypy automatically. Out of courtesy, black and isort, which change your code, are ready for you to use but are not applied directly.

Naming conventions
----------------------

Below are the naming conventions followed in Not Quite Paradise:
* If only one of a class should exist the creation function is called "init_[object]", otherwise "create_[object]".
* Where the object is taken as an argument the function name should default to "create_[object_type]".
* If checking a bool use IsA or HasA.
* If setting a variable from statically held data prefix with "load_[data]"
* Where a variable name contains "name" the variable may include spaces and other special characters. Where it includes "key" it may contain alphanumeric values only.
* "Handle" is for a conditional execution, i.e. the function will check criteria is met before executing.
* "Process" is for a mass application of a function. e.g. "process_lighting" applies lighting to all applicable entities.
* Arguments should be in a consistent order:
1. Identifiers (entity, skill, etc.)
2. Affected items (position, tiles, etc.)
3. Qualifiers
* Externally held data should be defined in a dataclass in definitions.py.


Contributing
---------------------

Forking
^^^^^^^^^^^^^^^

To get started, `fork the repository <https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo>`_ and open it up in your favorite editor. Next, open your terminal and point it to where you just saved the Not Quite Paradise repository. If you want to use `poetry <https://python-poetry.org/>`_ you would then run::

    pip install poetry
    poetry install

This will install all of the dependencies needed, using poetry.

To run the program use::

    python -m scripts


If you're not sure where to start helping out you can look at the existing feature requests and issues, `here <https://github.com/Snayff/notquiteparadise/issues>`_. Pick one you think you'd like to tackle and make the relevant changes to your fork.

Tests and Testing
^^^^^^^^^^^^^^^^^^^^^

Updates to the code should ideally include updates to the test suite. Please add new tests to support your changes, if you can. At the very least, as you'd imagine all tests must pass before code can be merged.

To run the current suite of tests and confirm they're all passing, use::

    pytest --cov=nqp

And to check that all the types are what they should be is as simple as typing::

    mypy


.. tip::
    If you create a Pull Request and push your changes the Continuous Integration will run these checks for you and let you know the result.

Merging
^^^^^^^^^^^^^^^^^^^
When you're ready, submit a `pull request <https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request>`_ to have your changes added to the main repository. Any pull request must the checks in the Github Actions, currently mypy type checking and pytest's testing. The code must remain compatible with the building of the `Sphinx <https://www.sphinx-doc.org/en/master/>`_ documentation, so that the docs are always up to date.

Bug, Issues and Defects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you find any problems in the existing code you can raise a `new issue <https://github.com/Snayff/notquiteparadise/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBUG%5D>`_ on Not Quite Paradise's GitHub page.


