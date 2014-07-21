#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os           # for handling paths
import sys          # for app args
import csv
import shutil       # for copying files
import random       # random generator
#import pynotify
import subprocess
from PyQt4 import QtCore, QtGui
from ui_qwordnotify import Ui_MainWindow
from preferences import PreferencesDialog
from editor import EditorForm

appVersion = "0.3.0"

class WordNotify_Window(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)                  # UI init

        self.initPreferences()              # prefs init
        self.initDictList()                 # dicts init
        self.initSysTray()                  # sys tray init
        self.sysTray.show()                 # sys tray is visible

        self.connect(self.dictListView, QtCore.SIGNAL('clicked(QModelIndex)'), self.selectDict)
        self.connect(self.dictListView, QtCore.SIGNAL('doubleClicked(QModelIndex)'), self.editDict)
        self.connect(self.stopPushButton, QtCore.SIGNAL('clicked()'), self.stopClicked)
        self.connect(self.startPushButton, QtCore.SIGNAL('clicked()'), self.startClicked)
        self.connect(self.optionsPushButton, QtCore.SIGNAL('clicked()'), self.optionsClicked)
        self.connect(self.dictNewPushButton, QtCore.SIGNAL('clicked()'), self.newDict)
        self.connect(self.dictAddPushButton, QtCore.SIGNAL('clicked()'), self.addDict)
        self.connect(self.dictEditPushButton, QtCore.SIGNAL('clicked()'), self.editDict)
        self.connect(self.dictRemovePushButton, QtCore.SIGNAL('clicked()'), self.removeDict)
        self.connect(self.actionAbout, QtCore.SIGNAL('triggered()'), self.about)
        self.connect(self.actionAbout_Qt, QtCore.SIGNAL('triggered()'), self.aboutQt)
        self.connect(self.actionQuit, QtCore.SIGNAL('triggered()'), self.quit)
        self.connect(self.actionStart, QtCore.SIGNAL('triggered()'), self.startClicked)
        self.connect(self.actionStop, QtCore.SIGNAL('triggered()'), self.stopClicked)
        self.connect(self.actionShowHide, QtCore.SIGNAL('triggered()'), self.show_hideTriggered)
        self.connect(self.actionNew, QtCore.SIGNAL('triggered()'), self.newDict)
        self.connect(self.actionAdd, QtCore.SIGNAL('triggered()'), self.addDict)
        self.connect(self.actionEdit, QtCore.SIGNAL('triggered()'), self.editDict)
        self.connect(self.actionRemove, QtCore.SIGNAL('triggered()'), self.removeDict)
        self.connect(self.actionPreferences, QtCore.SIGNAL('triggered()'), self.optionsClicked)

    def initPreferences(self):
        self.preferences = QtCore.QSettings("preferences.cfg", QtCore.QSettings.IniFormat)  # reading cfg ini file
        self.preferences.setIniCodec('UTF-8')

    def initSysTray(self):
        self.sysTray = QtGui.QSystemTrayIcon()          # creating sys tray
        iconPath = os.path.join(os.getcwd(), "icon.png")   # unicoded icon path
        iconPath = iconPath.decode('utf-8')             # unicoded icon path
        self.sysTray.setIcon(QtGui.QIcon(iconPath))     # setting icon
        rightClickMenu = QtGui.QMenu()                  # creating menu
        rightClickMenu.addAction(self.actionStart)      # adding actions to menu
        rightClickMenu.addAction(self.actionStop)       # adding actions to menu
        rightClickMenu.addSeparator()                   # adding separator
        rightClickMenu.addAction(self.actionShowHide)   # adding actions to menu
        rightClickMenu.addSeparator()                   # adding separator
        rightClickMenu.addAction(self.actionAbout)      # adding actions to menu
        rightClickMenu.addAction(self.actionAbout_Qt)   # adding actions to menu
        rightClickMenu.addSeparator()                   # separator
        self.actionQuit.setIcon(QtGui.QIcon("icons/exit.png"))
        rightClickMenu.addAction(self.actionQuit)       # adding actions to menu
        self.sysTray.setContextMenu(rightClickMenu)     # setting menu for systray
        self.sysTray.activated.connect(self.click_trap) # signal for icon left click

    def click_trap(self, value):
        if value == self.sysTray.Trigger:   # left click!
            self.show_hideTriggered()       # invoking show/hide event

    def show_hideTriggered(self):
        if self.isHidden():         # check if MainWindow is hidden
            self.show()             # if True then Show
        else:
            self.hide()             # else Hide

    def initDictList(self):
        dictsPath = os.path.join(os.getcwd(), "dicts")      # setting path with current path + dicts
        dictsPath = dictsPath.decode('utf-8')
        self.model = QtGui.QFileSystemModel()               # creating FS model
        self.modelIndex = QtCore.QModelIndex()              # creating model index
        self.model.setRootPath(dictsPath)                   # setting path for model
        self.modelIndex = self.model.index(dictsPath)       # getting model index
        self.dictListView.setModel(self.model)              # setting model for ListView
        self.dictListView.setRootIndex(self.modelIndex)     # setting index for ListView

        currentIndex = self.preferences.value("dict")       # reading index from cfg
        currentIndex = currentIndex.toString()              # translation to QString

        self.dictListView.setAutoScroll(True)               # autoscrolling
        self.dictListView.setCurrentIndex(self.model.index(currentIndex))   # setting index
        self.dictListView.scrollTo(self.model.index(currentIndex))  # scroll to current index

    def selectDict(self):
        currentIndex = self.dictListView.currentIndex()         # getting current index
        filePath = self.model.filePath(currentIndex)            # getting file path from index
        self.debug("%d %s" % (currentIndex.row(), filePath))    # debug info current row & file path
        self.preferences.setValue("index", currentIndex.row())  # saving row to cfg
        self.preferences.setValue("dict", filePath)             # saving file path to cfg
        self.preferences.sync()                                 # updating cfg file

    def newDict(self):
        selectDialog = QtGui.QFileDialog()
        newDictPath = selectDialog.getSaveFileName(self, self.tr('Name of new dict...'), 'dicts', 'TXT Files (*.txt)')
        if newDictPath != "":
            self.editorForm = EditorForm()
            self.editorForm.filePathLabel.setText(newDictPath)
            self.editorForm.show()
#            QtGui.QMessageBox.information(self, "CREATED", newDictPath + "\nHas been created!")

    def addDict(self):
        selectDialog = QtGui.QFileDialog()
        addDictPath = selectDialog.getOpenFileName(self, self.tr('Select dict...'), '', 'TXT Files (*.txt)')
        if addDictPath != "":
            addDictPath = str(addDictPath.toUtf8())
            addDictPath = addDictPath.decode('utf-8')
            shutil.copy(os.path.abspath(addDictPath), "dicts")
            QtGui.QMessageBox.information(self, self.tr("ADDED"), addDictPath + self.tr("\nHas been added to \'dicts\' directory!"))

    def editDict(self):
        filePath = self.preferences.value("dict")
        filePath = filePath.toString()
        filePath = str(filePath.toUtf8())
        filePath = filePath.decode('utf-8')

        f = open(filePath, 'r')
        data = f.read()
        f.close()

        data = QtCore.QString.fromUtf8(data)
        self.editorForm = EditorForm()
        self.editorForm.plainTextEdit.setPlainText(data)
        self.editorForm.filePathLabel.setText(filePath)
        self.editorForm.show()

    def removeDict(self):
        filePath = self.preferences.value("dict")
        filePath = filePath.toString()
        reply = QtGui.QMessageBox.question(self, self.tr("DELETION"), self.tr("Really delete?\n") + filePath, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            filePath = str(filePath.toUtf8())
            filePath = filePath.decode('utf-8')
            os.remove(os.path.abspath(filePath))
            QtGui.QMessageBox.information(self, self.tr("DELETED"), filePath + self.tr("\nHas been deleted!"))

    def initTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.start(self.delay)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'), self.timerUpdate)

    def timerUpdate(self):
        dictSize = len(self.myDict)
        #random.shuffle(self.myList)
        randNumber = random.randrange(1, dictSize)
        randLine = self.myDict[randNumber]
        #self.debug("%d %s" % (randnumber, randline.rstrip()))

        if (len(randLine) < 3):
            head, body, extra = randLine[0], randLine[1], ''
        else:
            head, body, extra = randLine[0], randLine[1], randLine[2]

        self.debug("[%d/%d] %s ― %s ― %s" % (randNumber, dictSize, head, body, extra))

        head = QtCore.QString.fromUtf8(head)
        body = body + "\n" + extra
        body = body.rstrip()
        #extra = QtCore.QString.fromUtf8(extra)
        body = QtCore.QString.fromUtf8(body)

        if self.notifyd == True:
            #head = str(head)
            #body = str(body)
            head = unicode(head)
            body = unicode(body)
            body = "<b><i>" + body + "</i></b>"
            iconPath = os.path.join(os.getcwd(), "icon.png")   # unicoded icon path
            iconPath = iconPath.decode('utf-8')
            self.showNotifyd(head, body, iconPath, self.timeout)
        elif self.notifyd == False:
            self.sysTray.showMessage(head, body, self.noicon, self.timeout)
        else:
            QtGui.QMessageBox.information(self, self.tr("ERROR"), self.tr("Unexpected error occurred!"))
            self.debug("Unexpected error occurred!")

    def showNotifyd(self, head, body, icon, timeout):
        #msg = pynotify.Notification(head, body, icon)
        #msg.set_timeout(timeout)
        #msg.show()
        ncmd = "notify-send"
        subprocess.call([ncmd, "-t", str(timeout), "-i", icon, head, body])

    def startClicked(self):
        #self.hide()
        filePath = self.preferences.value("dict").toString()
        self.timeout = self.preferences.value("timeout").toInt()[0]*1000
        self.delay = self.preferences.value("delay").toInt()[0]*1000
        if self.preferences.value("notifyd").toString() == "true":
            self.notifyd = True
            #global pynotify
            #import pynotify
            #pynotify.init("init")
        else:
            self.notifyd = False
        self.icon = QtGui.QSystemTrayIcon.Information
        self.noicon = QtGui.QSystemTrayIcon.NoIcon
        self.myDict = {}
        self.myIndex = 0
        filePath = str(filePath.toUtf8())
        filePath = filePath.decode('utf-8')

        with open(filePath, 'rb') as f:
            reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
            for line in reader:
                self.myIndex += 1
                self.myDict[self.myIndex] = line
        f.close()

        #random.shuffle(self.myList)

        self.initTimer()
        self.sysTray.showMessage("qWordNotify", self.tr("Timer started!"), self.icon, 1000)
        self.debug("Timer started!")

    def stopClicked(self):
        self.timer.stop()
        self.sysTray.showMessage("qWordNotify", self.tr("Timer stopped!"), self.icon, 1000)
        self.debug("Timer stopped!")

    def optionsClicked(self):
        self.prefDialog = PreferencesDialog()
        self.prefDialog.setModal(True)
        self.prefDialog.show()

    def about(self):
        QtGui.QMessageBox.information(self, self.tr("About qWordNotify"), "<b>qWordNotify 0.1</b><br>(c) 2014 Anonymous")

    def aboutQt(self):
        QtGui.QApplication.aboutQt()

    def closeEvent(self,event):
        reply=QtGui.QMessageBox.question(self, self.tr("QUITTING"), self.tr("Are you sure to quit?"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply==QtGui.QMessageBox.Yes:
            self.preferences.sync()
            event.accept()
        else:
            event.ignore()

    def quit(self):
        QtGui.qApp.quit()

    def debug(self, msg):
        print "DEBUG:", msg
        
    def tr(self, text):
        return QtCore.QCoreApplication.translate("WordNotify_Window", text)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
#    appTranslator = QtCore.QTranslator()
#    appTranslator.load('lang/ukr.qm')
#    app.installTranslator(appTranslator) 
    #app.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
    window = WordNotify_Window()
    window.setWindowTitle("qWordNotify %s-dev" % appVersion)
    window.show()

sys.exit(app.exec_())
