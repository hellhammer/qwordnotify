# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from ui_editor import Ui_EditorForm

class EditorForm(QtGui.QWidget, Ui_EditorForm):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.connect(self.savePushButton, QtCore.SIGNAL('clicked()'), self.saveButtonClicked)
        self.connect(self.cancelPushButton, QtCore.SIGNAL('clicked()'), self.cancelButtonClicked)

    def saveButtonClicked(self):
        reply = QtGui.QMessageBox.question(self, self.tr("SAVING"), self.tr("Really save?"), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.saveTrigger(self.filePathLabel.text())

    def cancelButtonClicked(self):
        self.close()

    def saveTrigger(self, filePath):
        data = self.plainTextEdit.toPlainText()
        data = str(data.toUtf8())

        filePath = str(filePath.toUtf8())
        filePath = filePath.decode('utf-8')

        f = open(filePath, 'w')
        f.write(data)
        f.close()

        self.close()
        
    def tr(self, text):
        return QtCore.QCoreApplication.translate("EditorForm", text)
