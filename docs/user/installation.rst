============
Installation
============

hdf5view is designed to work on Windows, macOS and Linux. Python >= 3.6 is required and, in addition to installing :ref:`install-hdf5view`, you will need to install one of the available :ref:`install-qt-api-bindings`.

.. _install-hdf5view:

hdf5view
--------

To install the current release of hdf5view from `PyPI <https://pypi.org/project/hdf5view/>`_ using ``pip``, enter the following command in the terminal:

.. code-block::
   
   pip install hdf5view


Alternatively, to install hdf5view from source, clone the `repository <https://github.com/tgwoodcock/hdf5view>`_ from GitHub and install with ``pip``:

.. code-block::

   git clone https://github.com/tgwoodcock/hdf5view.git
   cd hdf5view
   pip install .

.. note::

   If you would like to contribute to hdf5view, please have a look at the :ref:`contributing-guide` guide for instructions on :ref:`installing-a-development-environment`.  


.. _install-qt-api-bindings:
   
Qt API Bindings
---------------

One of `pyqt5 <https://www.riverbankcomputing.com/software/pyqt/>`_, `pyside2 <https://pyside.org>`_, `pyqt6 <https://www.riverbankcomputing.com/software/pyqt/>`_ or `pyside6 <https://pyside.org>`_ is required in order to be able to run hdf5view. Please install *any one of these*. For instance, to install pyqt5 with ``pip``:

.. code-block::

   pip install pyqt5

   
.. note::
   pyside2 is not compatible with Python 3.12

.. note::
   hdf5view uses `qtpy <https://github.com/spyder-ide/qtpy>`_ as an abstraction layer for pyqt5/pyside2/pyqt6/pyside6. If you have any of these Qt API bindings installed, qtpy will take the first available one in the order shown in the previous sentence. hdf5view works with all of the bindings. 
   
.. tip::
   If you have *more than one* of the bindings installed and want to specify *which one* should be used for hdf5view, you can do this by setting the ``QT_API`` environment variable before running hdf5view. For example: if you have pyqt5 and pyside2 installed and you want hdf5view to use PySide2, on Windows PowerShell:

   .. code-block:: powershell

      $env:QT_API = 'pyside2'

   or on linux (Ubuntu/Debian):

   .. code-block:: bash

      export QT_API=pyside2


Other Dependencies
------------------

The other dependencies required by hdf5view (`qtpy <https://github.com/spyder-ide/qtpy>`_, `h5py <https://www.h5py.org/>`_, `psutil <https://github.com/giampaolo/psutil>`_ and `pyqtgraph <https://www.pyqtgraph.org/>`_) will be installed automatically during the installation of hdf5view, if they are not already present on your system. Currently installed versions of these dependencies will not be overwritten by installing hdf5view. 

.. note::
   `pyqtgraph <https://www.pyqtgraph.org/>`_ 0.12 supports all of pyqt5, pyside2, pyqt6 or pyside6. Older versions of pyqtgraph may not support all of them.


To uninstall hdf5view:
----------------------

.. code-block::

   pip uninstall hdf5view
