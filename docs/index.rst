.. hdf5view documentation master file, created by
   sphinx-quickstart on Fri Oct 25 13:23:08 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

================================
hdf5view |release| documentation
================================

A simple Qt/Python based viewer for HDF5 files.

hdf5view aims to be easy to use and to allow you to get the view of your data that you need with just a few clicks. If you need to check the structure of an HDF5 file, quickly see what data it contains or choose a dataset for futher analysis in another program, hdf5view may be for you. 

We don't aim to be able to create or edit HDF5 files and have only minimal possibilties for data analysis other than just viewing it. Other viewers for HDF5 files are available, see :ref:`related_projects`.


.. toctree::
   :hidden:
   :titlesonly:

   user/index
   dev/index
   reference/index
   changelog
   
.. grid:: 2
    :gutter: 2

    .. grid-item-card::
        :link: user/index
        :link-type: doc

        :octicon:`book;2em;sd-text-info` User Guide
        ^^^

        Guides for installing and using using hdf5view.

    .. grid-item-card::
        :link: reference/index
        :link-type: doc

        :octicon:`code;2em;sd-text-info` API reference
        ^^^

        Descriptions of all functions, modules, and objects in hdf5view.

    .. grid-item-card::
        :link: dev/index
        :link-type: doc

        :octicon:`people;2em;sd-text-info` Contributing
        ^^^

        hdf5view is an open source project which welcomes contributions from its users.
