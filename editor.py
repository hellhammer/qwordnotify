from PyQt4 import QtCore, QtGui
from ui_editor import Ui_EditorForm

class EditorForm(QtGui.QWidget, Ui_EditorForm):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.connect(self.savePushButton, QtCore.SIGNAL('clicked()'), self.saveButtonClicked)
        self.connect(self.cancelPushButton, QtCore.SIGNAL('clicked()'), self.cancelButtonClicked)

    def saveButtonClicked(self):
        reply = QtGui.QMessageBox.question(self, "SAVE?", "Really save?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.saveTrigger(self.filePathLabel.text())
        #self.close()

    def cancelButtonClicked(self):
        self.close()

    def saveTrigger(self, filePath):
        data = self.plainTextEdit.toPlainText()
        data = str(data.toUtf8())
        f = open(filePath, 'w')
        f.write(data)
        f.close()
        self.close()
