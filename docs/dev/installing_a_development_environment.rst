.. _installing-a-development-environment:

====================================
Installing a Development Environment
====================================

To contribute to hdf5view, please `fork <https://docs.github.com/en/get-started/quickstart/contributing-to-projects#about-forking>`_ the `repository <https://github.com/tgwoodcock/hdf5view>`_.


Set up a virtual environment, called *e.g.* "dev_hdf5view" using ``venv`` in Python [#f1]_::

   python -m venv dev_hdf5view
   
Change directories into your virtual environment and clone *your forked repository* into it (replacing "your-username" in the code below)::
   
   cd dev_hdf5view
   git clone https://github.com/your-username/hdf5view.git
   
Activate the virtual environment:

.. tab-set::

    .. tab-item:: Windows

        .. code-block:: powershell

            .\Scripts\Activate.ps1

    .. tab-item:: macOS

        .. code-block:: bash

            source bin/activate
			
    .. tab-item:: Linux

        .. code-block:: bash

            source bin/activate



Set the ``upstream`` remote to the main hdf5view repository::
    
   cd hdf5view
   git remote add upstream https://github.com/tgwoodcock/hdf5view.git

Install hdf5view in editable mode with the optional dependencies for development::

   pip install -e .[dev]

.. rubric:: Footnotes

.. [#f1] You could also use a different tool of your choice for making virtual environments.