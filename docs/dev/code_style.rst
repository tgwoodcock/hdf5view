.. _code-style:

==========
Code style
==========

This project aims to follow the `Style Guide for Python Code <https://peps.python.org/pep-0008/>`_. We use `ruff <https://docs.astral.sh/ruff/>`_ as a linter and formatter with the following sets of rules:

.. code-block::

   "B",   # flake8-bugbear
   "D",   # pydocstyle
   "E",   # pycodestyle
   "F",   # Pyflakes
   "I",   # isort
   "SIM", # flake8-simplify
   "UP",  # pyupgrade
   
Some of the rules in these sets are mutually conflicting and in these cases, some rules are selected to be ignored. See the pyproject.toml for details.

We use `pre-commit <https://pre-commit.com>`__ to run ``ruff`` automatically prior to
each local commit.
Please install it in your environment like this::

    pre-commit install

Next time you commit some code, your code will be linted and formatted in place using ``ruff``.

We format docstrings according to the `numpy <https://numpydoc.readthedocs.io/en/latest/format.html>`_ standard (with some exceptions). Some linting and formatting of docstrings is carried out by ruff and the docstrings are
additionally checked against this standard when building the documentation.