from PyQt4 import QtCore, QtGui
from ui_preferences import Ui_Dialog

class PreferencesDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

        self.initPreferences()

        self.connect(self.savePushButton, QtCore.SIGNAL('clicked()'), self.saveButtonClicked)
        self.connect(self.cancelPushButton, QtCore.SIGNAL('clicked()'), self.cancelButtonClicked)

    def initPreferences(self):
        self.preferences = QtCore.QSettings("preferences.cfg", QtCore.QSettings.NativeFormat)
        self.fileLineEdit.setText(self.preferences.value("dict").toString())
        self.timeoutLineEdit.setText(self.preferences.value("timeout").toString())
        self.delayLineEdit.setText(self.preferences.value("delay").toString())
        if self.preferences.value("notifyd") == "true":
            self.checkBox.setChecked(True)

    def saveButtonClicked(self):
        self.preferences.setValue("dict", self.fileLineEdit.text())
        self.preferences.setValue("timeout", self.timeoutLineEdit.text())
        self.preferences.setValue("delay", self.delayLineEdit.text())
        self.preferences.sync()
        self.close()

    def cancelButtonClicked(self):
        self.close()