#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, QAction, qApp, QFileDialog, \
    QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem, QColorDialog
from PyQt5.QtGui import QIcon, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import Qt


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
        self.picture_add_button.released.connect(self.add_picture)
        self.color_select_button.released.connect(self.set_background_color)
        self.file_edit.textChanged.connect(self._update_background_preview)
        self.background_color = QColor()
        self._add_file_dialog()
        self.show()

    def _select_file(self):
        fname, _ = QFileDialog.getOpenFileName(directory=os.path.expanduser('~'), filter="Images (*.png *.xpm *.jpg)")
        self.file_edit.setText(fname)

    def _update_background_preview(self):
        scene = QGraphicsScene()
        qpixmap = QPixmap(self.file_edit.text())
        scene.addPixmap(qpixmap)
        self.background_preview.setScene(scene)
        self.background_preview.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

    def _add_file_dialog(self):
        self.file_browse_button.clicked.connect(self._select_file)

    def render_monitors(self, monitors):
        pen = QPen()
        pen.setWidth(10)
        brush = QBrush()
        scene = QGraphicsScene()
        for mon in monitors:
            this_rect = QGraphicsRectItem(mon.x(), mon.y(), mon.width(), mon.height())
            this_rect.setPen(pen)
            this_rect.setBrush(brush)
            this_rect.setZValue(1)
            scene.addItem(this_rect)
        self.monitor_display.setScene(scene)
        self.monitor_display.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)

    def add_picture(self):
        qpixmap = QPixmap(self.file_edit.text())
        self.monitor_display.scene().addPixmap(qpixmap)

    def set_background_color(self):
        color_dialog = QColorDialog()
        self.background_color = color_dialog.getColor()
        p = self.background_color_preview.palette()
        p.setColor(self.background_color_preview.backgroundRole(), self.background_color)
        self.background_color_preview.setPalette(p)


if __name__ == "__main__":
    # get the directory of this script
    path = os.path.dirname(os.path.abspath(__file__))

    app = Wallpaste(sys.argv)
    win = WallpasteMainWindow(path)
    desk_widget = WallpasteDesktopWidget()

    win.render_monitors(desk_widget.get_screen_resolutions())

    sys.exit(app.exec_())
