#!/usr/bin/env python

import os
import sys
import time
import random
from PyQt4 import QtCore, QtGui
from ui_qwordnotify import Ui_MainWindow

class WordNotify_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.initDictList()

        self.tray = SystemTrayIcon(self)
        self.tray.show()

        self.connect(self.dictListView, QtCore.SIGNAL('clicked(QModelIndex)'), self.selectDict)
        self.connect(self.dictListView, QtCore.SIGNAL('doubleClicked(QModelIndex)'), self.editDict)
        self.connect(self.savePushButton, QtCore.SIGNAL('clicked()'), self.saveClicked)
        self.connect(self.startPushButton, QtCore.SIGNAL('clicked()'), self.startClicked)
        self.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        self.connect(self.actionAbout_Qt, QtCore.SIGNAL('triggered()'), self.aboutQt)
        self.connect(self.actionQuit, QtCore.SIGNAL('triggered()'), self.quit)


    def initDictList(self):
        dictsPath = os.path.join(os.getcwd(), "dicts")
        self.model = QtGui.QFileSystemModel()
        self.modelIndex = QtCore.QModelIndex()
        self.model.setRootPath(dictsPath) # "/home/max/Code/qwordnotify/dicts"
        self.modelIndex = self.model.index(dictsPath)
        self.dictListView.setModel(self.model)
        self.dictListView.setRootIndex(self.modelIndex)



    def selectDict(self):
        currentIndex = self.dictListView.currentIndex()
        filePath = self.model.filePath(currentIndex)
        self.fileLineEdit.setText(filePath)

    def addDict(self):
        pass

    def editDict(self):
        print "DEBUG: EDIT SELECTED!"

    def removeDict(self):
        pass

    def saveClicked(self):
        self.hide()

    def initTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.start(5000)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'), self.timerUpdate)

    def timerUpdate(self):
        listSize = len(self.myList)
        randnumber = random.randrange(0, listSize)
        randline = self.myList[randnumber]
        print randnumber, randline
        randdata = randline.split(":")
        randword = randdata[0]
        randdesc = randdata[1]
        if (len(randdata) > 2):
            randdesc = randdesc + "\n" + randdata[2]
        randdesc = randdesc[:-1]
        self.tray.showMessage(randword.decode('utf-8'), randdesc.decode('utf-8'))

    def startClicked(self):
        filePath = self.fileLineEdit.text()
        timeout = self.timeoutLineEdit.text()
        delay = self.delayLineEdit.text()
        self.myList = []
        with open(filePath) as f:
            for line in f:
                self.myList.append(line)
        f.close()
        random.shuffle(self.myList)

        self.initTimer()

    def about(self):
        QtGui.QMessageBox.information(self, "About qWordNotify", "<b>qWordNotify 0.1</b><br>(c) 2014 Anonymous")

    def aboutQt(self):
        QtGui.QApplication.aboutQt()

    def quit(self):
        QtGui.qApp.quit()

######################################################################################




#######################################################################################

class RightClickMenu(QtGui.QMenu):
    def __init__(self, parent=None):
        QtGui.QMenu.__init__(self, "Menu", parent)

        icon = QtGui.QIcon.fromTheme("edit-cut")
        self.addAction(QtGui.QAction(icon, "&Start", self))

        self.addSeparator()

        icon = QtGui.QIcon.fromTheme("quit")
        self.addAction(QtGui.QAction(icon, "&Quit", self))

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
