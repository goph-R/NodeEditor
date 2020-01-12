import os

from PySide2.QtCore import QObject, QCoreApplication, QSettings
from PySide2.QtWidgets import QApplication

from MainWindow import MainWindow
from Style import Style


class App(QObject):

    def __init__(self, args):
        super(App, self).__init__()

        QCoreApplication.setOrganizationName('Dynart')
        QCoreApplication.setApplicationName('NodeEditor')
        self._styleContent = ''
        self._qApp = QApplication(args)
        self._qApp.setStyle(Style())
        self._mainWindow = MainWindow(self)
        self._mainWindow.show()

    def run(self):
        settings = QSettings()
        self._mainWindow.restoreGeometry(settings.value('mainWindowGeometry'))
        self._mainWindow.restoreState(settings.value('mainWindowState'))
        return self._qApp.exec_()

    def exit(self, returnCode=0):
        settings = QSettings()
        settings.setValue('mainWindowGeometry', self._mainWindow.saveGeometry())
        settings.setValue('mainWindowState', self._mainWindow.saveState())
        self._qApp.exit(returnCode)
