import sys
from PyQt4 import QtCore, QtGui
from ui_preferences import Ui_Dialog

class PreferencesDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.initPreferences()

        self.connect(self.savePushButton, QtCore.SIGNAL('clicked()'), self.saveButtonClicked)
        self.connect(self.cancelPushButton, QtCore.SIGNAL('clicked()'), self.cancelButtonClicked)
        self.connect(self.checkBox, QtCore.SIGNAL('stateChanged(int)'), self.notifydChecked)

    def checkOS(self):
        platform = sys.platform
        return platform

    def checkNotifyd(self):
        try:
            import pynotify
            pynotify.init("init")
            msg = pynotify.Notification("INFORMATION", "Using \'notifyd\' option!")
            msg.set_timeout(1000)
            msg.show()
            return True
        except ImportError, e:
            self.debug("%s\nDEBUG: Python package \"pynotify\" not found" % e)
            return False

    def initPreferences(self):
        self.preferences = QtCore.QSettings("preferences.cfg", QtCore.QSettings.IniFormat)
        platform = self.checkOS()
        self.preferences.setValue("platform", platform)
        self.preferences.sync()
        self.fileLineEdit.setText(self.preferences.value("dict").toString())
        self.timeoutLineEdit.setText(self.preferences.value("timeout").toString())
        self.delayLineEdit.setText(self.preferences.value("delay").toString())
        if platform == "linux" or platform == "linux2":
            self.checkBox.setEnabled(True)
        if self.preferences.value("notifyd") == "true":
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)

    def notifydChecked(self):
        if self.checkBox.isChecked():
            if self.checkNotifyd() == False:
                QtGui.QMessageBox.information(self, "ERROR", "Python package \"pynotify\" not found")
                self.checkBox.setChecked(False)

    def saveButtonClicked(self):
        if self.checkBox.isChecked():
            self.preferences.setValue("notifyd", "true")
        else:
            self.preferences.setValue("notifyd", "false")
        self.preferences.setValue("dict", self.fileLineEdit.text())
        self.preferences.setValue("timeout", self.timeoutLineEdit.text())
        self.preferences.setValue("delay", self.delayLineEdit.text())
        self.preferences.sync()
        self.close()

    def cancelButtonClicked(self):
        self.close()

    def debug(self, msg):
        print "DEBUG:", msg