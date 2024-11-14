"""
Contains a function to generate an hdf5 file with
datasets of various types for demonstration purposes.
"""

import pathlib

import h5py
import numpy as np
from PIL import Image


def make_demo_hdf5():
    """
    Create an hdf5 file with some datasets of
    different types as a demonstration.

    The file "demo.hdf5" will be saved in the
    current user's home directory.

    Returns
    -------
    None.

    """
    with h5py.File(
        pathlib.Path.joinpath(pathlib.Path.home(), "demo.hdf5"), "w"
    ) as file1:
        x = np.arange(0, 361 * 4, 4)

        # single column of data
        d1 = file1.create_dataset(
            "/x sin x", data=np.deg2rad(x) * np.sin(np.deg2rad(x)), dtype=np.float32
        )
        d1.attrs["x range"] = "0:361*4:4"
        d1.attrs["x unit"] = "degrees"

        # 3 columns of data
        d2 = file1.create_dataset(
            "/3columns",
            data=np.stack(
                (x[:91], np.sin(np.deg2rad(x[:91])), np.cos(np.deg2rad(x[:91]))), axis=1
            ),
            dtype=np.float32,
        )
        d2.attrs["col 0"] = "x"
        d2.attrs["col 1"] = "sin x"
        d2.attrs["col 2"] = "cos x"
        d2.attrs["x range"] = "0:364:4"
        d2.attrs["x unit"] = "degrees"

        # string
        d3 = file1.create_dataset("/str", data=b"this is a string")
        d3.attrs["Weather"] = "sunny"
        d3.attrs["number"] = 42

        # compound names
        my_dtype = np.dtype(
            [("x", np.uint16), ("sin x", np.float32), ("cos x", np.float32)]
        )

        s_a = np.array(
            [
                tuple([j, np.sin(np.deg2rad(x[:91]))[i], np.cos(np.deg2rad(x[:91]))[i]])
                for i, j in enumerate(x[:91])
            ],
            dtype=my_dtype,
        )

        d3 = file1.create_dataset("/compound_names", data=s_a, dtype=my_dtype)
        d3.attrs["x range"] = "0:364:4"
        d3.attrs["x unit"] = "degrees"

        # stack of greyscale images
        i_d = np.random.randint(0, 256, 3 * 1024**2).reshape((3, 1024, 1024))
        i_d[0, 100:151, 200:251] = 0
        i_d[1, 600:651, 700:751] = 0
        i_d[2, 900:1001, 800:951] = 0
        file1["/luminance"] = i_d.astype(np.uint8)

        # stack of rgba images
        i_d2 = np.random.randint(0, 256, 3 * 4 * 1024**2).reshape((3, 1024, 1024, 4))
        i_d2[:, :, :, 3] = 255
        i_d2[0, 100:151, 200:251] = np.array([1, 0, 0, 1]) * 255
        i_d2[1, 600:651, 700:751] = np.array([1, 1, 0, 1]) * 255
        i_d2[2, 900:1001, 800:951] = np.array([1, 1, 1, 1]) * 255
        file1["/rgba"] = i_d2.astype(np.uint8)

        # hdf5view logo (single rgba image)
        file1["/hdf5view logo"] = np.array(
            Image.open(r"images\hdf5view.ico"), dtype=np.uint8
        )


if __name__ == "__main__":
    make_demo_hdf5()
