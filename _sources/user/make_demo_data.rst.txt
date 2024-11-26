.. _make-demo-data:

=========================
Making the demo HDF5 file
=========================

.. tip::
   The tutorials in the documentation use data in the file ``demo.hdf5``. If you would like to follow the tutorials with the same data, you can create ``demo.hdf5`` by running the script ``make_demo_hdf5.py``, which is located in the ``resources`` folder of hdf5view, *i.e.* here:
   
   .. code-block:: none

      -- path-to-my-python-distribution
          |-- Lib
            |-- site-packages
               |-- hdf5view
                  |-- resources
                     |-- make_demo_hdf5.py

   Running ``make_demo_hdf5.py`` requires the Python packages ``numpy`` and ``Pillow``. If needed, please install these in advance, *e.g.* with ``pip`` :
   
   .. code-block:: shell
      
	  pip install numpy, Pillow