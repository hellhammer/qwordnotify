#!/usr/bin/env python

import os
import sys
import time
import random
from PyQt4 import QtCore, QtGui
from ui_qwordnotify import Ui_MainWindow
import preferences

class WordNotify_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.initPreferences()
        self.initDictList()
        self.initSysTray()
        self.sysTray.show()

        self.connect(self.dictListView, QtCore.SIGNAL('clicked(QModelIndex)'), self.selectDict)
        self.connect(self.dictListView, QtCore.SIGNAL('doubleClicked(QModelIndex)'), self.editDict)
        self.connect(self.stopPushButton, QtCore.SIGNAL('clicked()'), self.stopClicked)
        self.connect(self.startPushButton, QtCore.SIGNAL('clicked()'), self.startClicked)
        self.connect(self.optionsPushButton, QtCore.SIGNAL('clicked()'), self.optionsClicked)
        self.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        self.connect(self.actionAbout_Qt, QtCore.SIGNAL('triggered()'), self.aboutQt)
        self.connect(self.actionQuit, QtCore.SIGNAL('triggered()'), self.quit)
        self.connect(self.actionStart, QtCore.SIGNAL('triggered()'), self.startClicked)
        self.connect(self.actionStop, QtCore.SIGNAL('triggered()'), self.stopClicked)
        self.connect(self.actionShow, QtCore.SIGNAL('triggered()'), self.showTriggered)
        self.connect(self.actionHide, QtCore.SIGNAL('triggered()'), self.hideTriggered)



    def initPreferences(self):
        self.preferences = QtCore.QSettings("preferences.cfg", QtCore.QSettings.IniFormat)

    def initSysTray(self):
        self.sysTray = QtGui.QSystemTrayIcon()
        self.sysTray.setIcon(QtGui.QIcon(os.path.join(os.getcwd(), "icon.png")))
        rightClickMenu = QtGui.QMenu()
        rightClickMenu.addAction(self.actionStart)
        rightClickMenu.addAction(self.actionStop)
        rightClickMenu.addSeparator()
        rightClickMenu.addAction(self.actionShow)
        rightClickMenu.addAction(self.actionHide)
        rightClickMenu.addSeparator()
        rightClickMenu.addAction(self.actionAbout)
        rightClickMenu.addAction(self.actionAbout_Qt)
        rightClickMenu.addSeparator()
        rightClickMenu.addAction(self.actionQuit)
        self.sysTray.setContextMenu(rightClickMenu)
        self.sysTray.activated.connect(self.click_trap)

    def click_trap(self, value):
        if value == self.sysTray.Trigger: #left click!
            if self.isHidden():
                self.showTriggered()
            else:
                self.hideTriggered()

    def showTriggered(self):
        self.show()

    def hideTriggered(self):
        self.hide()

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
        print currentIndex.row()
        filePath = self.model.filePath(currentIndex)
        self.preferences.setValue("index", currentIndex.row())
        self.preferences.setValue("dict", filePath)
        self.preferences.sync()

    def addDict(self):
        pass

    def editDict(self):
        print "DEBUG: EDIT SELECTED!"

    def removeDict(self):
        pass

    def initTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.start(self.delay)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'), self.timerUpdate)

    def timerUpdate(self):
        listSize = len(self.myList)
        random.shuffle(self.myList)
        randnumber = random.randrange(0, listSize)
        randline = self.myList[randnumber]
        print randnumber, randline
        randdata = randline.split(":")
        randword = randdata[0]
        randdesc = randdata[1]
        if (len(randdata) > 2):
            randdesc = randdesc + "\n" + randdata[2]
        randdesc = randdesc[:-1]
        randword = QtCore.QString.fromUtf8(randword)
        randdesc = QtCore.QString.fromUtf8(randdesc)
        self.sysTray.showMessage(randword, randdesc, self.timeout)

    def startClicked(self):
        self.hide()
        filePath = self.preferences.value("dict").toString()
        self.timeout = self.preferences.value("timeout").toInt()[0]*1000
        self.delay = self.preferences.value("delay").toInt()[0]*1000
        self.myList = []
        with open(filePath) as f:
            for line in f:
                self.myList.append(line)
        f.close()
        random.shuffle(self.myList)

        self.initTimer()
        self.sysTray.showMessage("qWordNotify", "Timer started!")

    def stopClicked(self):
        self.timer.stop()
        self.sysTray.showMessage("qWordNotify", "Timer stopped!")

    def optionsClicked(self):
        self.prefDialog = preferences.PreferencesDialog()
        self.prefDialog.setModal(True)
        self.prefDialog.show()

    def about(self):
        QtGui.QMessageBox.information(self, "About qWordNotify", "<b>qWordNotify 0.1</b><br>(c) 2014 Anonymous")

    def aboutQt(self):
        QtGui.QApplication.aboutQt()

    def quit(self):
        QtGui.qApp.quit()


app = QtGui.QApplication(sys.argv)
#app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
window = WordNotify_Window()
window.show()

sys.exit(app.exec_())
