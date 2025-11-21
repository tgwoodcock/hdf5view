.. _basic-usage:

============
Basic Usage
============

Opening an HDF5 File
---------------------

With hdf5view you can either:

1. Open any HDF5 file with two clicks using the context menu. To enable this, please follow the guide to :ref:`context-menu-setup`.

**or**

2. Open the hdf5view application and use the ``File > Open`` menu to open a file or drag and drop a file onto the application window. To start the hdf5view application, double click ``hdf5view.exe`` in the ``Scripts`` folder of your Python distribution.
   
   .. tip::
   
      You can create a desktop link to ``hdf5view.exe`` in the ``Scripts`` folder of your Python distribution for convenience. A Windows icon file hdf5view.ico is provided in the folder hdf5view/resources/images.
   
   .. note::

      If you prefer working at the terminal, you can start the hdf5view application using
   
      .. code-block:: shell
      
	     hdf5view
   
      You can open a file directly using
   
      .. code-block:: shell
   
         hdf5view -f <path/to/my/hdf5file>

      Or you can open several files in one window by repeating the "-f" flag:
   
      .. code-block:: shell
   
         hdf5view -f <path/to/first_hdf5file> -f <path/to/second_hdf5file>

|

.. _initial-app-state-file:
 
Initial State of the Application
--------------------------------

Once you have opened an HDF5 file with hdf5view, the application window will look like this:

.. image:: /_static/tutorials/app_init_file.png

|

The application window contains five separate widgets:

File Structure Table
+++++++++++++++++++++

The File Structure table (left hand side of the application), shows the structure of the open HDF5 file as a directory tree. By default it is initally at the root group and you can double-click on the folder or click the arrow to expand the tree and navigate to other groups or datasets.

.. figure:: /_static/tutorials/tt4.png

   The File Structure table with expanded directory structure and the dataset "3columns" selected.
 
Central Tabbed Area
++++++++++++++++++++

The central tabbed area shows the data in a particular dataset. By default a ``Table`` tab is visible. You can add ``Image`` and ``Plot`` tabs here later.

.. figure:: /_static/tutorials/tt7.png

   Part of the central tabbed area showing the default ``Table`` tab. The filename is shown at the top of the tab.
   
Attributes Table
++++++++++++++++

The Attributes table (right hand side, top), shows details of any attributes of the selected dataset.

.. figure:: /_static/tutorials/tt5.png

   The Attributes table.

Dataset Table
++++++++++++++

The Dataset table (right hand side, middle), shows details of the type and shape of the data at the selected dataset.

.. figure:: /_static/tutorials/tt6.png

   The Dataset table.
   
Slice Table
++++++++++++

The Slice table (right hand side, bottom), shows which slice of the data is currently displayed. There are default slice values for particular dataset types and shapes in hdf5view, which are intended as a sensible starting point. You can change the slice to get a different view of the data.

.. figure:: /_static/tutorials/tt8.png

   The Slice table, showing the default slice for the ``Table`` tab at a 2D dataset (all rows and columns are shown in the ``Table``).
 

Detailed guides to using tabs in hdf5view are available in the :ref:`table-tab-tutorial`, :ref:`plot-tab-tutorial` and :ref:`image-tab-tutorial`.

|

.. _context-menu-setup:

Setting up the context menu
---------------------------

A particularly useful way to use hdf5view is to add an entry to the context menu. That way, you can right-click on any HDF5 file and left-click "Open with hdf5view" from the menu that appears.

On Windows, to get "Open with hdf5view" on the right click context menu, we need to modify the registry. To do this, please follow these 7 steps:

1. Run the registry editor (regedit) as an administrator
2. Navigate to ``Computer\HKEY_CLASSES_ROOT\*\shell``
3. Right-click on ``shell`` and select ``New > Key``
4. Name the new key ``Open with hdf5view``
5. Right-click on ``Open with hdf5view`` and select ``New > Key``
6. Name the new key ``command``

   The directory structure should now look like this:

   .. code-block:: none

      -- Computer
          |-- HKEY_CLASSES_ROOT
            |-- *
               |-- shell
                  |-- Open with hdf5view
                     |-- command


7. Click on ``command`` to select it. In the right-hand window, you should see a table with 3 columns (Name, Type and Data). Right-click on the first entry under the ``Name`` column and select ``Modify``. Now find the box ``value data:`` and enter the path to ``hdf5view.exe`` in the Scripts folder of your Python distribution followed by ``-f "%1"``. This should look something like this:

   .. code-block::

      C:\Program Files\PythonXXX\Scripts\hdf5view.exe -f "%1"

   (replace XXX with the number of your Python version *e.g.* 312 for Python312). Finally select `OK`.

   .. tip::
      Enclosing %1 in quotes (as above) ``"%1"`` ensures that filenames including spaces are passed correctly to hdf5view.

   .. tip::
      If you want to add the icon to the context menu as well, right click on the key ``Open with hdf5view`` and select ``New > String Value``. In the right-hand window, right-click on the entry in the ``Name`` column and select ``Modify``. Set the ``value name:`` to ``Icon``. Finally set the ``value data:`` to the path to the hdf5view icon as a string, *e.g.*:

      ``"C:\Program Files\PythonXXX\Lib\site-packages\hdf5view\resources\images\hdf5view.ico"``

Now you can right-click on any HDF5 file and open it with hdf5view.
