from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 715)
        MainWindow.setMaximumSize(QtCore.QSize(600, 715))
        MainWindow.setStyleSheet("background-color: rgb(27, 29, 35)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.full_address = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full_address.sizePolicy().hasHeightForWidth())
        self.full_address.setSizePolicy(sizePolicy)
        self.full_address.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.full_address.setFont(font)
        self.full_address.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.full_address.setReadOnly(True)
        self.full_address.setObjectName("full_address")
        self.gridLayout.addWidget(self.full_address, 3, 0, 2, 1)
        self.index = QtWidgets.QCheckBox(self.centralwidget)
        self.index.setMinimumSize(QtCore.QSize(0, 50))
        self.index.setStyleSheet("QCheckBox {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}")
        self.index.setObjectName("index")
        self.gridLayout.addWidget(self.index, 4, 1, 1, 1)
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setMinimumSize(QtCore.QSize(0, 50))
        self.type.setStyleSheet("QComboBox {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(37, 39, 48);\n"
"    background-color: rgb(34, 36, 44);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(34, 36, 44);\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}\n"
"QComboBox QListView\n"
"{\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    selection-background-color: rgb(37, 39, 48);\n"
"}")
        self.type.setEditable(False)
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.gridLayout.addWidget(self.type, 0, 1, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.resetButton.setFont(font)
        self.resetButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 1, 1, 1, 1)
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.findButton.setFont(font)
        self.findButton.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QPushButton:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.findButton.setObjectName("findButton")
        self.gridLayout.addWidget(self.findButton, 3, 1, 1, 1)
        self.object = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.object.sizePolicy().hasHeightForWidth())
        self.object.setSizePolicy(sizePolicy)
        self.object.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.object.setFont(font)
        self.object.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 20px;\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(43, 45, 46);\n"
"}")
        self.object.setObjectName("object")
        self.gridLayout.addWidget(self.object, 0, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.map = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setMinimumSize(QtCore.QSize(503, 377))
        self.map.setMaximumSize(QtCore.QSize(650, 450))
        self.map.setStyleSheet("")
        self.map.setText("")
        self.map.setObjectName("map")
        self.verticalLayout.addWidget(self.map)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.full_address.setPlaceholderText(_translate("MainWindow", "Полный адрес"))
        self.index.setText(_translate("MainWindow", "Почтовый индекс"))
        self.type.setCurrentText(_translate("MainWindow", "Схема"))
        self.type.setItemText(0, _translate("MainWindow", "Схема"))
        self.type.setItemText(1, _translate("MainWindow", "Спутник"))
        self.type.setItemText(2, _translate("MainWindow", "Гибрид"))
        self.resetButton.setText(_translate("MainWindow", "Сброс поискового результата"))
        self.findButton.setText(_translate("MainWindow", "Найти"))
        self.object.setPlaceholderText(_translate("MainWindow", "Запрос для поиска"))

