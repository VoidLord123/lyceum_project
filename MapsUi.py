from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 643)
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
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 50))
        self.checkBox.setStyleSheet("QCheckBox {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    border-radius: 10px;\n"
"    color: #FFF;\n"
"    padding-right: 10px;\n"
"    padding-left: 10px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 1, 1, 1)
        self.full_address = QtWidgets.QLineEdit(self.centralwidget)
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
        self.scale = QtWidgets.QLineEdit(self.centralwidget)
        self.scale.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scale.setFont(font)
        self.scale.setStyleSheet("QLineEdit {\n"
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
        self.scale.setObjectName("scale")
        self.gridLayout.addWidget(self.scale, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox.setStyleSheet("QComboBox {\n"
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
"")
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.coordinates = QtWidgets.QLineEdit(self.centralwidget)
        self.coordinates.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.coordinates.setFont(font)
        self.coordinates.setStyleSheet("QLineEdit {\n"
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
        self.coordinates.setObjectName("coordinates")
        self.gridLayout.addWidget(self.coordinates, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(503, 377))
        self.label.setStyleSheet("QLabel {\n"
"    border: 2px solid rgb(37, 39, 48);\n"
"    color: #FFF;\n"
"    padding-right: 20px;\n"
"    padding-left: 20px;\n"
"    background-color: rgb(34, 36, 44);\n"
"}\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(1, 1)
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
        self.resetButton.setText(_translate("MainWindow", "Сброс поискового результата"))
        self.findButton.setText(_translate("MainWindow", "Найти"))
        self.checkBox.setText(_translate("MainWindow", "Почтовый индекс"))
        self.full_address.setPlaceholderText(_translate("MainWindow", "Полный адрес"))
        self.scale.setPlaceholderText(_translate("MainWindow", "Масштаб"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Схема"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Схема"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Спутник"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Гибрид"))
        self.coordinates.setPlaceholderText(_translate("MainWindow", "Координаты"))
