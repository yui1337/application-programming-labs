from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from imgiterator import ImageIterator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.counter = 0
        self.iterator = None
        self.csv_path = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(854, 480))
        MainWindow.setMaximumSize(QtCore.QSize(2560, 1440))
        MainWindow.setStyleSheet("background-color: rgb(43, 45, 48);\n"
                                 "")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(260, 80, 1000, 600))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        #self.image.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("../../../../../images/000001.jpg"))
        self.image.setScaledContents(False)
        #self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setWordWrap(False)
        self.image.setOpenExternalLinks(False)
        #self.image.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.image.setObjectName("image")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 50, 240, 660))
        self.widget.setObjectName("widget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(100)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btn_choose_csv = QtWidgets.QPushButton(self.widget)
        self.btn_choose_csv.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_choose_csv.sizePolicy().hasHeightForWidth())
        self.btn_choose_csv.setSizePolicy(sizePolicy)
        #self.btn_choose_csv.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_choose_csv.setStyleSheet("font: 20pt \"Roboto\";\n"
                                          "background-color: rgb(43, 45, 48);\n"
                                          "border: 2px solid rgb(67, 69, 74);\n"
                                          "border-radius: 5px;\n"
                                          "color: rgb(111, 115, 122);")
        self.btn_choose_csv.setDefault(False)
        self.btn_choose_csv.setFlat(False)
        self.btn_choose_csv.setObjectName("btn_choose_csv")
        self.verticalLayout.addWidget(self.btn_choose_csv)

        self.btn_next_img = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next_img.sizePolicy().hasHeightForWidth())
        self.btn_next_img.setSizePolicy(sizePolicy)
        self.btn_next_img.setStyleSheet("font: 20pt \"Roboto\";\n"
                                        "background-color: rgb(43, 45, 48);\n"
                                        "border: 2px solid rgb(67, 69, 74);\n"
                                        "border-radius: 5px;\n"
                                        "color: rgb(111, 115, 122);")
        self.btn_next_img.setObjectName("btn_next_img")
        self.verticalLayout.addWidget(self.btn_next_img)

        self.btn_exit = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setStyleSheet("font: 20pt \"Roboto\";\n"
                                    "background-color: rgb(43, 45, 48);\n"
                                    "border: 2px solid rgb(67, 69, 74);\n"
                                    "border-radius: 5px;\n"
                                    "color: rgb(111, 115, 122);")
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout.addWidget(self.btn_exit)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(530, 20, 453, 46))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)

        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setStyleSheet("color: rgb(111, 115, 122);\n"
                                   "font: 20pt \"Roboto\";\n"
                                   "border-color: rgb(67, 68, 90);")
        #self.label_3.setTextFormat(QtCore.Qt.PlainText)
        #self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.current_img = QtWidgets.QLabel(self.widget1)
        self.current_img.setStyleSheet("color: rgb(111, 115, 122);\n"
                                       "font: 20pt \"Roboto\";\n"
                                       "border-color: rgb(67, 68, 90);")
       # self.current_img.setTextFormat(QtCore.Qt.PlainText)
        #self.current_img.setAlignment(QtCore.Qt.AlignCenter)
        self.current_img.setObjectName("current_img")
        self.horizontalLayout.addWidget(self.current_img)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_choose_csv.clicked.connect(lambda: self.load_csv())
        self.btn_next_img.clicked.connect(lambda: self.next_img(self))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Просмотр датасета"))
        self.btn_choose_csv.setText(_translate("MainWindow", "Choose CSV file"))
        self.btn_next_img.setText(_translate("MainWindow", "Next >"))
        self.btn_exit.setText(_translate("MainWindow", "Exit"))
        self.label_3.setText(_translate("MainWindow", "Current image:"))
        self.current_img.setText(_translate("MainWindow", "image name"))

    def load_csv(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Select a File", "", "CSV file (*.csv)")
        if filename:
            self.csv_path = filename
            # self.set_viewimages_menu()

    def next_img(self):
        self.iterator = ImageIterator(self.csv_path)
        iter(self.iterator)
        next_img_path = next(self.iterator)
        self.image.setPixmap(QtGui.QPixmap(next_img_path[1]))
        self.counter += 1



