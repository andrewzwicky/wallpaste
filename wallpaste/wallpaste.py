#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication,QWidget, QDesktopWidget, QMainWindow, QAction, qApp, QFileDialog
from PyQt5.QtGui import QIcon


class Wallpaste(QApplication):

    def __init__(self, args):
        super().__init__(args)


class WallpasteDesktopWidget(QDesktopWidget):

    def __init__(self):
        super().__init__()

    def get_screen_resolutions(self):
        num_screens = self.screenCount()
        return [self.screenGeometry(i) for i in range(num_screens)]


class WallpasteMainWindow(QMainWindow):

    def __init__(self, path):
        super().__init__()
        uic.loadUi(os.path.join(path, 'wallpaste.ui'), self)
        self._add_file_dialog()
        self.show()

    def _select_file(self):
        fname, _ = QFileDialog.getOpenFileName(directory="/home", filter="Images (*.png *.xpm *.jpg)")
        self.file_edit.setText(fname)

    def _add_file_dialog(self):
        self.file_browse_button.clicked.connect(self._select_file)

if __name__ == "__main__":
    # get the directory of this script
    path = os.path.dirname(os.path.abspath(__file__))

    app = Wallpaste(sys.argv)
    win = WallpasteMainWindow(path)
    desk_widget = WallpasteDesktopWidget()

    print(desk_widget.get_screen_resolutions())

    sys.exit(app.exec_())
