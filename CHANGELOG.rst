.. _changelog:

=========
Changelog
=========

All changes to this project which may affect users are documented in this file. The format is based
on `Keep a Changelog <https://keepachangelog.com/en/1.1.0>`__, and this project tries
its best to adhere to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`__.

..
   Categories are:

   Added
   -----

   Changed
   -------

   Removed
   -------

   Deprecated
   ----------

   Fixed
   -----

0.2.0 (2024-11-25)
==================

Added
-----

- Documentation, built using Sphinx and the PyData theme.
- Pre-commit linting and formatting using ruff. The file .pre-commit-config-yaml has been added to the top level. Users can install the hooks locally with ``pre-commit install``. All staged changes are then passed through the ruff linter and formatter according to the sets of rules used. See the guide to :ref:`code-style` and pyproject.toml for further details.

Changed
-------

- removed a line of code from hdf5view/views.py, which was causing problems on macOS. (`#12 <https://github.com/tgwoodcock/hdf5view/issues/12>`_)
- removed import of QVariant. This caused problems with PySide6 as it is obsolete. None can be returned instead of an invalid QVariant. This is now done in several functions. (`#13 <https://github.com/tgwoodcock/hdf5view/issues/13>`_)
- All Python files have been run through the ruff linter and formatter to ensure consistent code style.