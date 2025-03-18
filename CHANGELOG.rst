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

0.2.5 (2025-03-18)
==================

Fixed
-----

- Ensured resources/images/hdf5view.png is packaged with the source code.

0.2.4 (2025-03-06)
==================

Added
-----

- Added a link to the ``Zenodo`` record for ``hdf5view`` to the ``About...`` dialog in the application.

Changed
-------

- The widths of the columns in the ``File Structure`` table now automatically fit to their contents for easier viewing.
- Single-column datasets on the ``Table`` tab now automatically fit the width to the contents.
- Multi-column datasets on the ``Table`` tab have a fixed column width that can be adjusted by the user.

Fixed
-----

- ``resources/make_demo_hdf5.py`` All paths are now pathlib.Path so it should be platform-independent.
- ``resources/make_demo_hdf5.py`` Added a .png image of the ``hdf5view`` logo to avoid an error being thrown by PIL when reading a .ico file.

0.2.3 (2025-02-11)
==================

Fixed
-----

- Rendering of datasets with ndim == 0 in the TableView.

0.2.2 (2024-11-28)
==================

Changed
-------

- Added Zenodo doi to CITATION.cff

0.2.1 (2024-11-28)
==================

Added
-----

- CITATION.cff to record contribution credits and hold metadata for citations. See `Citation File Format (CFF) <https://citation-file-format.github.io/>`_ for further information. The collective term ``The hdf5view Developers`` has been defined, which includes all contributors to hdf5view as shown in the 
  `contributors graph of the repository <https://github.com/tgwoodcock/hdf5view/graphs/contributors>`_.
- Pre-commit hook to ensure that the CITATION.cff is correctly formatted.

Changed
-------

- Updated the documentation so that the new method of recording package credits is explained in the Contributing guide.
- Updated the LICENSE file and ``About...`` entry in the ``Help`` menu of the application to reflect the new method of recording package credits.

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