[![PyPI Version](https://img.shields.io/pypi/v/hdf5view.svg)](https://pypi.python.org/pypi/hdf5view/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/hdf5view.svg)](https://pypi.python.org/pypi/hdf5view/)

# **hdf5view** <img src="https://raw.githubusercontent.com/tgwoodcock/hdf5view/main/src/hdf5view/resources/images/hdf5view.ico" width="28" />  

**Simple Qt/Python based viewer for HDF5 files.**

Features:
- Image tab(s) showing rgb(a) or grayscale images of a selected node:

![Image](https://raw.githubusercontent.com/tgwoodcock/hdf5view/main/docs/_static/readme/imageview.png)

<br>

- Plot tab(s) showing columns of data in a node:

![Image](https://raw.githubusercontent.com/tgwoodcock/hdf5view/main/docs/_static/readme/plotview.png)
   
<br>

- Table tab giving a view of the data in the dataset selected:

![Image](https://raw.githubusercontent.com/tgwoodcock/hdf5view/main/docs/_static/readme/tableview.png)

<br>

- File Structure table giving a tree view of the hdf5 file
- Attributes table showing any attributes assigned to a dataset
- Dataset table showing *e.g.* the shape, number of dimensions and data type of a dataset
- Slice table showing which slice of the data is currently displayed (can be set by the user)
- Export images/plots in a variety of formats (image files, data files, hdf5, matplotlib window)
- Datasets are loaded dynamically, so hopefully it should be able to handle HDF5 files of any size and structure.
- Warnings are given when selecting a dataset if loading it would consume more than 30% of the available memory. The user can the opt to abort or continue loading.

<br>

**Why use hdf5view?**

hdf5view is a simple Qt/Python based tool which aims to be easy to use and to allow you to get a view of your data with just a few clicks. If you need to check the structure of an HDF5 file, quickly see what data it contains or choose a dataset for futher analysis in another program, hdf5view may be for you. We don't aim to be able to create or edit HDF5 files and have only minimal possibilties for data analysis other than just viewing it. Other viewers for HDF5 files are available, which may be more suited to your needs, see [related projects](https://tgwoodcock.github.io/hdf5view/user/related_projects.html).

<br>

## Documentation

The documentation for hdf5view is here: [https://tgwoodcock.github.io/hdf5view](https://tgwoodcock.github.io/hdf5view)

<br>

## **1. Installing**

hdf5view is designed to be platform independent and can be installed with `pip`. Please see the [installation guide](https://tgwoodcock.github.io/hdf5view/user/installation.html) for details.

<br>

## **2. Running**

The [usage guide](https://tgwoodcock.github.io/hdf5view/user/basic_usage.html) shows various ways to start hdf5view and open HDF5 files in the application.

#### **Context menu**

A particularly useful way to use hdf5view is to add an entry to the context menu. This way, you can open any HDF5 file with two clicks. Please see the [context menu guide](https://tgwoodcock.github.io/hdf5view/user/basic_usage.html#setting-up-the-context-menu) for instructions on how to set this up.


## **3. Usage**

In the [documentation](https://tgwoodcock.github.io/hdf5view), there are tutorials on how to use

- the [table tab](https://tgwoodcock.github.io/hdf5view/user/table_tab.html)
- the [image tab](https://tgwoodcock.github.io/hdf5view/user/image_tab.html) and
- the [plot tab](https://tgwoodcock.github.io/hdf5view/user/plot_tab.html) to view your data.

<br>

## **4. Testing**

Currently there are no unit tests for this package. The gui has been tested with qtpy=2.2.0, pyqtgraph=0.12.4 and h5py=3.7.0 in combination with pyqt5=5.15.7, pyside2=5.15.2.1, pyqt6=6.3.1 and pyside6=6.3.2, and it works with all of the Qt API bindings.

<br>

## **5. Issues**

If there are any issues, please feel free to use the [issues mechanism on github](https://github.com/tgwoodcock/hdf5view/issues) to get in touch.

<br>

## **6. Contributing**

If you are interested in contributing to the hdf5view project, please see the [contributing guide](https://tgwoodcock.github.io/hdf5view/dev/index.html).

## TODO:

* Implement dynamic loading for files larger than the available memory
* Add tests
* Possibly add 3D rendering, likely based on pyqtgraph
