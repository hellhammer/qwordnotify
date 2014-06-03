# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created: Tue Jun  3 22:00:17 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EditorForm(object):
    def setupUi(self, EditorForm):
        EditorForm.setObjectName(_fromUtf8("EditorForm"))
        EditorForm.setWindowModality(QtCore.Qt.WindowModal)
        EditorForm.resize(489, 307)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditorForm.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(EditorForm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(EditorForm)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filePathLabel = QtGui.QLabel(EditorForm)
        self.filePathLabel.setObjectName(_fromUtf8("filePathLabel"))
        self.horizontalLayout.addWidget(self.filePathLabel)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelPushButton = QtGui.QPushButton(EditorForm)
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.savePushButton = QtGui.QPushButton(EditorForm)
        self.savePushButton.setObjectName(_fromUtf8("savePushButton"))
        self.horizontalLayout.addWidget(self.savePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(EditorForm)
        QtCore.QMetaObject.connectSlotsByName(EditorForm)

    def retranslateUi(self, EditorForm):
        EditorForm.setWindowTitle(_translate("EditorForm", "Editor", None))
        self.filePathLabel.setText(_translate("EditorForm", "file path", None))
        self.cancelPushButton.setText(_translate("EditorForm", "Cancel", None))
        self.savePushButton.setText(_translate("EditorForm", "Save", None))

