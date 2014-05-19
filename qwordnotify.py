#!/usr/bin/env python

import os
import sys
from PyQt4 import QtCore, QtGui
from ui_qwordnotify import Ui_MainWindow

class WordNotify_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

#        self.pswd()
#        self.load()

        self.tray = SystemTrayIcon(self)
        self.tray.show()

        self.connect(self.savePushButton, QtCore.SIGNAL('clicked()'), self.saveClicked)
        self.connect(self.startPushButton, QtCore.SIGNAL('clicked()'), self.startClicked)
        self.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        self.connect(self.actionAbout_Qt, QtCore.SIGNAL('triggered()'), self.aboutQt)
        self.connect(self.actionQuit, QtCore.SIGNAL('triggered()'), self.quit)

    def saveClicked(self):
        self.tray.showMessage("TEST TITLE", "MESSAGE HERE")

    def startClicked(self):
        pass

    def about(self):
        QtGui.QMessageBox.about(self, "TITLE", "TEXT")

    def aboutQt(self):
        QtGui.QApplication.aboutQt()

    def quit(self):
        QtGui.qApp.quit()


#######################################################################################

class RightClickMenu(QtGui.QMenu):
    def __init__(self, parent=None):
        QtGui.QMenu.__init__(self, "Edit", parent)

        icon = QtGui.QIcon.fromTheme("edit-cut")
        self.addAction(QtGui.QAction(icon, "&Cut", self))

        icon = QtGui.QIcon.fromTheme("edit-copy")
        self.addAction(QtGui.QAction(icon, "Copy (&X)", self))

        icon = QtGui.QIcon.fromTheme("edit-paste")
        self.addAction(QtGui.QAction(icon, "&Paste", self))

class LeftClickMenu(QtGui.QMenu):
    def __init__(self, parent=None):
        QtGui.QMenu.__init__(self, "File", parent)

        icon = QtGui.QIcon.fromTheme("document-new")
        self.addAction(QtGui.QAction(icon, "&New", self))

        icon = QtGui.QIcon.fromTheme("document-open")
        self.addAction(QtGui.QAction(icon, "&Open", self))

        icon = QtGui.QIcon.fromTheme("document-save")
        self.addAction(QtGui.QAction(icon, "&Save", self))


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, parent)
        self.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), "icon.png")))

        self.right_menu = RightClickMenu()
        self.setContextMenu(self.right_menu)

        self.left_menu = LeftClickMenu()

        self.activated.connect(self.click_trap)

    def click_trap(self, value):
        if value == self.Trigger: #left click!
            self.left_menu.exec_(QtGui.QCursor.pos())

    def show(self):
        QtGui.QSystemTrayIcon.show(self)

######################################################################################



app = QtGui.QApplication(sys.argv)

window = WordNotify_Window()
window.show()

#tray = SystemTrayIcon()
#tray.show()

sys.exit(app.exec_())
