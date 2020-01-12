###############################################################################
#                                                                             #
# The MIT License                                                             #
#                                                                             #
# Copyright (C) 2017 by Juergen Skrotzky (JorgenVikingGod@gmail.com)          #
#               >> https://github.com/Jorgen-VikingGod                        #
#                                                                             #
# Sources: https://github.com/Jorgen-VikingGod/Qt-Frameless-Window-DarkStyle  #
#                                                                             #
# PySide version by Gabor Laszlo (gopher.hu@gmail.com)                        #
###############################################################################

import os

from PySide2.QtGui import QPalette, QColor, Qt
from PySide2.QtWidgets import QProxyStyle, QStyleFactory, QApplication


class Style(QProxyStyle):

    StyleBase = None

    def __init__(self, style=None):
        super(Style, self).__init__(style if style else self.styleBase())
        self._qss = self._load()

    def _load(self):
        resourcesPath = os.path.dirname(os.path.realpath(__file__)) + '/resources'
        with open(resourcesPath + '/style.qss', 'r') as file:
            data = file.read()
        return data.replace(':/images', resourcesPath + '/images')

    def styleBase(self, style=None):
        Style.StyleBase = QStyleFactory.create('Fusion') if not style else style
        return Style.StyleBase

    def baseStyle(self):
        return self.styleBase()

    def polish(self, data):
        super(Style, self).polish(data)
        className = data.__class__.__name__
        if className == 'QPalette':
            self.polishPalette(data)
        elif className == 'QApplication':
            self.polishApplication(data)

    def polishPalette(self, palette):
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.WindowText, QColor(127, 127, 127))
        palette.setColor(QPalette.Base, QColor(42, 42, 42))
        palette.setColor(QPalette.AlternateBase, QColor(50, 50, 50))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, QColor(53, 53, 53))
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.Text, QColor(127, 127, 127))
        palette.setColor(QPalette.Dark, QColor(35, 35, 35))
        palette.setColor(QPalette.Shadow, QColor(20, 20, 20))
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(127, 127, 127))
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.Disabled, QPalette.Highlight, QColor(80, 80, 80))
        palette.setColor(QPalette.HighlightedText, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.HighlightedText, QColor(127, 127, 127))

    def polishApplication(self, app):
        # defaultFont = QApplication.font()
        # defaultFont.setPointSize(defaultFont.pointSize() + 1)
        # app.setFont(defaultFont)
        app.setStyleSheet(self._qss)
