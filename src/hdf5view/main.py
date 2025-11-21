"""
Contains the main application entry point or command line
interface and defines the paths for the application to
find its resources.
"""

import argparse
import os
import sys

# import traceback
import qtpy
from qtpy.QtCore import (
    Qt,
)
from qtpy.QtGui import (
    QIcon,
)
from qtpy.QtWidgets import (
    QApplication,
)

os.environ["PYQTGRAPH_QT_LIB"] = qtpy.API_NAME

from .mainwindow import MainWindow

# def my_excepthook(e_type, value, tb):
#     """
#     Catch and print exceptions to help with debugging Qt guis.
#     """
#     m_1 = '\x1b[31m\x1b[1m'
#     m_2 = f"Unhandled error: {e_type} {value} {''.join(traceback.format_tb(tb))}"
#     m_3 = '\x1b[0m'
#     print(m_1 + m_2 + m_3)

# sys.excepthook = my_excepthook


basedir = os.path.dirname(__file__)
resource_path = os.path.join(basedir, "resources", "images")
qtpy.QtCore.QDir.addSearchPath("icons", resource_path)


def main():
    """Define the main application entry point (cli)."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, required=False, action="append")
    args = parser.parse_args()

    if qtpy.API_NAME in ["PyQt5", "PySide2"]:
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    app.setOrganizationName("hdf5view")
    app.setApplicationName("hdf5view")
    app.setWindowIcon(QIcon("icons:hdf5view.svg"))

    window = MainWindow(app)
    window.show()

    # Open files if supplied on command line
    if args.file:
        for file in args.file:
            window.open_file(file)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
