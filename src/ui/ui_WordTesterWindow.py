# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WordTesterWindow.ui'
#
# Created: Fri May 20 16:25:49 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_WordTesterWindow(object):
    def setupUi(self, WordTesterWindow):
        WordTesterWindow.setObjectName("WordTesterWindow")
        WordTesterWindow.resize(752, 480)
        WordTesterWindow.setMinimumSize(QtCore.QSize(752, 480))
        self.centralwidget = QtGui.QWidget(WordTesterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.wordTableWidget = QtGui.QWidget(self.centralwidget)
        self.wordTableWidget.setObjectName("wordTableWidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.wordTableWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.wordsTable = WordTableView(self.wordTableWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wordsTable.sizePolicy().hasHeightForWidth())
        self.wordsTable.setSizePolicy(sizePolicy)
        self.wordsTable.setMinimumSize(QtCore.QSize(351, 0))
        self.wordsTable.setObjectName("wordsTable")
        self.gridLayout_2.addWidget(self.wordsTable, 0, 0, 1, 1)
        self.searchBarFrame = QtGui.QFrame(self.wordTableWidget)
        self.searchBarFrame.setFrameShape(QtGui.QFrame.NoFrame)
        self.searchBarFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.searchBarFrame.setObjectName("searchBarFrame")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.searchBarFrame)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.searchBarFrame)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.searchLineEdit = QtGui.QLineEdit(self.searchBarFrame)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout_3.addWidget(self.searchLineEdit)
        self.searchCheckBox = QtGui.QCheckBox(self.searchBarFrame)
        self.searchCheckBox.setObjectName("searchCheckBox")
        self.horizontalLayout_3.addWidget(self.searchCheckBox)
        self.gridLayout_2.addWidget(self.searchBarFrame, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.wordTableWidget, 0, 0, 2, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(105, 0))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.numberOfWordsSpinBox = QtGui.QSpinBox(self.groupBox)
        self.numberOfWordsSpinBox.setMaximum(999)
        self.numberOfWordsSpinBox.setObjectName("numberOfWordsSpinBox")
        self.horizontalLayout.addWidget(self.numberOfWordsSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.repetitionsCheckBox = QtGui.QCheckBox(self.groupBox)
        self.repetitionsCheckBox.setObjectName("repetitionsCheckBox")
        self.verticalLayout_2.addWidget(self.repetitionsCheckBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.testDifficultyComboBox = QtGui.QComboBox(self.groupBox)
        self.testDifficultyComboBox.setObjectName("testDifficultyComboBox")
        self.testDifficultyComboBox.addItem("")
        self.testDifficultyComboBox.addItem("")
        self.testDifficultyComboBox.addItem("")
        self.testDifficultyComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.testDifficultyComboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.beginTestButton = QtGui.QPushButton(self.groupBox)
        self.beginTestButton.setObjectName("beginTestButton")
        self.horizontalLayout_2.addWidget(self.beginTestButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.allCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.allCheckBox.setObjectName("allCheckBox")
        self.verticalLayout.addWidget(self.allCheckBox)
        self.easyCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.easyCheckBox.setObjectName("easyCheckBox")
        self.verticalLayout.addWidget(self.easyCheckBox)
        self.mediumCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.mediumCheckBox.setObjectName("mediumCheckBox")
        self.verticalLayout.addWidget(self.mediumCheckBox)
        self.hardCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.hardCheckBox.setObjectName("hardCheckBox")
        self.verticalLayout.addWidget(self.hardCheckBox)
        self.wordsOnlyCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.wordsOnlyCheckBox.setObjectName("wordsOnlyCheckBox")
        self.verticalLayout.addWidget(self.wordsOnlyCheckBox)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.scanCheckBox = QtGui.QCheckBox(self.groupBox_2)
        self.scanCheckBox.setObjectName("scanCheckBox")
        self.horizontalLayout_5.addWidget(self.scanCheckBox)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 7)
        self.gridLayout.setColumnStretch(1, 4)
        WordTesterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(WordTesterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 25))
        self.menubar.setObjectName("menubar")
        WordTesterWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(WordTesterWindow)
        self.statusbar.setObjectName("statusbar")
        WordTesterWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.searchLineEdit)
        self.label_2.setBuddy(self.numberOfWordsSpinBox)
        self.label_3.setBuddy(self.testDifficultyComboBox)

        self.retranslateUi(WordTesterWindow)
        QtCore.QMetaObject.connectSlotsByName(WordTesterWindow)

    def retranslateUi(self, WordTesterWindow):
        WordTesterWindow.setWindowTitle(QtGui.QApplication.translate("WordTesterWindow", "Word Tester", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("WordTesterWindow", "Search: ", None, QtGui.QApplication.UnicodeUTF8))
        self.searchCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Search backwards", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("WordTesterWindow", "Test properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("WordTesterWindow", "Words in test:", None, QtGui.QApplication.UnicodeUTF8))
        self.repetitionsCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Allow repetitions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("WordTesterWindow", "Difficulty:", None, QtGui.QApplication.UnicodeUTF8))
        self.testDifficultyComboBox.setItemText(0, QtGui.QApplication.translate("WordTesterWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.testDifficultyComboBox.setItemText(1, QtGui.QApplication.translate("WordTesterWindow", "Easy", None, QtGui.QApplication.UnicodeUTF8))
        self.testDifficultyComboBox.setItemText(2, QtGui.QApplication.translate("WordTesterWindow", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.testDifficultyComboBox.setItemText(3, QtGui.QApplication.translate("WordTesterWindow", "Hard", None, QtGui.QApplication.UnicodeUTF8))
        self.beginTestButton.setText(QtGui.QApplication.translate("WordTesterWindow", "Begin Test", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("WordTesterWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.allCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.easyCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Easy", None, QtGui.QApplication.UnicodeUTF8))
        self.mediumCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.hardCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Hard", None, QtGui.QApplication.UnicodeUTF8))
        self.wordsOnlyCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Show words only", None, QtGui.QApplication.UnicodeUTF8))
        self.scanCheckBox.setText(QtGui.QApplication.translate("WordTesterWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))

from WordTableView import WordTableView
