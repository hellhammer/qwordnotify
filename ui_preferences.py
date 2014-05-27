# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences.ui'
#
# Created: Tue May 27 15:12:59 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(363, 228)
        self.verticalLayout_8 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.fileLabel = QtGui.QLabel(Dialog)
        self.fileLabel.setObjectName(_fromUtf8("fileLabel"))
        self.verticalLayout_3.addWidget(self.fileLabel)
        self.fileLineEdit = QtGui.QLineEdit(Dialog)
        self.fileLineEdit.setObjectName(_fromUtf8("fileLineEdit"))
        self.verticalLayout_3.addWidget(self.fileLineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.timeoutLabel = QtGui.QLabel(Dialog)
        self.timeoutLabel.setObjectName(_fromUtf8("timeoutLabel"))
        self.verticalLayout_4.addWidget(self.timeoutLabel)
        self.timeoutLineEdit = QtGui.QLineEdit(Dialog)
        self.timeoutLineEdit.setText(_fromUtf8(""))
        self.timeoutLineEdit.setObjectName(_fromUtf8("timeoutLineEdit"))
        self.verticalLayout_4.addWidget(self.timeoutLineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.delayLabel = QtGui.QLabel(Dialog)
        self.delayLabel.setObjectName(_fromUtf8("delayLabel"))
        self.verticalLayout_5.addWidget(self.delayLabel)
        self.delayLineEdit = QtGui.QLineEdit(Dialog)
        self.delayLineEdit.setText(_fromUtf8(""))
        self.delayLineEdit.setObjectName(_fromUtf8("delayLineEdit"))
        self.verticalLayout_5.addWidget(self.delayLineEdit)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_8.addWidget(self.line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancelPushButton = QtGui.QPushButton(Dialog)
        self.cancelPushButton.setObjectName(_fromUtf8("cancelPushButton"))
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.savePushButton = QtGui.QPushButton(Dialog)
        self.savePushButton.setObjectName(_fromUtf8("savePushButton"))
        self.horizontalLayout.addWidget(self.savePushButton)
        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Preferences", None))
        self.fileLabel.setText(_translate("Dialog", "File path:", None))
        self.timeoutLabel.setText(_translate("Dialog", "Message timeout (s):", None))
        self.delayLabel.setText(_translate("Dialog", "Message delay (s):", None))
        self.label_2.setText(_translate("Dialog", "Language:", None))
        self.checkBox.setText(_translate("Dialog", "use notifyd", None))
        self.label.setText(_translate("Dialog", "GNULinux only", None))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel", None))
        self.savePushButton.setText(_translate("Dialog", "Save", None))

