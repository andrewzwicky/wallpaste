#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication,QWidget, QDesktopWidget, QMainWindow, QAction, qApp, QFileDialog
from PyQt5.QtGui import QIcon


def run():
    app = Wallpaste(sys.argv)
    mw = WallpasteMainWindow()
    desk_widget = WallpasteDesktopWidget()

    print(desk_widget.get_screen_resolutions())

    sys.exit(app.exec_())


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

    def __init__(self):
        super().__init__()
        self.resize(800, 550)
        self.center()
        self.setWindowTitle("wallpaste")
        self._add_menubar()
        self._add_fileselector()
        self.setCentralWidget(QWidget())
        self.centralWidget().show()
        self.show()

    # http://zetcode.com/gui/pyqt5/firstprograms/
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _add_menubar(self):
        self.mb = self.menuBar()
        self.mb.addMenu("test")

    def _add_fileselector(self):
        QFileDialog(self.centralWidget())


class TestImport(QMainWindow):

    def __init__(self, path):
        super().__init__()
        uic.loadUi(os.path.join(path,'wallpaste.ui'), self)
        self.show()

if __name__ == "__main__":
    # get the directory of this script
    path = os.path.dirname(os.path.abspath(__file__))

    app = Wallpaste(sys.argv)
    win = TestImport(path)
    sys.exit(app.exec_())
