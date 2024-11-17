import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from imgiterator import ImageIterator


class UiMainWindow(object):
    def setup_ui(self, main_window: QMainWindow) -> None:
        """
        Creates User Interface
        :param main_window: QMainWindow object
        """
        main_window.setObjectName("main_window")
        main_window.setWindowTitle("Dataset Viewer")
        main_window.setFixedSize(1280, 720)
        main_window.setStyleSheet("background-color: rgb(43, 45, 48);")

        self.container = QtWidgets.QWidget(main_window)
        self.container.setObjectName("container")

        self.image = QtWidgets.QLabel(self.container)
        self.image.setGeometry(QtCore.QRect(260, 80, 1000, 600))
        self.image.setText("Waiting for input...")
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.image.setStyleSheet("color: rgb(111, 115, 122);\n"
                                   "font: 18pt \"Roboto\";\n")

        self.btns_col = QtWidgets.QWidget(self.container)
        self.btns_col.setGeometry(QtCore.QRect(10, 50, 240, 660))
        self.btns_col.setObjectName("btns_col")
        self.btns_layout = QtWidgets.QVBoxLayout(self.btns_col)
        self.btns_layout.setContentsMargins(0, 0, 0, 0)
        self.btns_layout.setSpacing(100)
        self.btns_layout.setObjectName("btns_layout")

        self.btn_choose_csv = QtWidgets.QPushButton(self.btns_col)
        self.btn_choose_csv.setStyleSheet("font: 18pt \"Roboto\";\n"
                                          "background-color: rgb(43, 45, 48);\n"
                                          "border: 2px solid rgb(67, 69, 74);\n"
                                          "border-radius: 5px;\n"
                                          "color: rgb(111, 115, 122);")
        self.btn_choose_csv.setText("Choose CSV file")
        self.btn_choose_csv.setObjectName("btn_choose_csv")
        self.btns_layout.addWidget(self.btn_choose_csv)

        self.btn_next_img = QtWidgets.QPushButton(self.btns_col)
        self.btn_next_img.setStyleSheet("font: 18pt \"Roboto\";\n"
                                        "background-color: rgb(43, 45, 48);\n"
                                        "border: 2px solid rgb(67, 69, 74);\n"
                                        "border-radius: 5px;\n"
                                        "color: rgb(111, 115, 122);")
        self.btn_next_img.setObjectName("btn_next_img")
        self.btn_next_img.setText("Next >")
        self.btns_layout.addWidget(self.btn_next_img)

        self.btn_exit = QtWidgets.QPushButton(self.btns_col)
        self.btn_exit.setStyleSheet("font: 18pt \"Roboto\";\n"
                                    "background-color: rgb(43, 45, 48);\n"
                                    "border: 2px solid rgb(67, 69, 74);\n"
                                    "border-radius: 5px;\n"
                                    "color: rgb(111, 115, 122);")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.setText("Exit")
        self.btns_layout.addWidget(self.btn_exit)

        self.img_title = QtWidgets.QLabel(self.container)
        self.img_title.setGeometry(QtCore.QRect(530, 20, 453, 46))
        self.img_title.setObjectName("img_title")
        self.img_title.setStyleSheet("color: rgb(111, 115, 122);\n"
                                     "font: 18pt \"Roboto\";\n")

        main_window.setCentralWidget(self.container)

        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.btn_choose_csv.clicked.connect(self.load_csv)
        self.btn_next_img.clicked.connect(self.next_img)

    def set_iterator(self) -> None:
        """
        Creates ImageIterator iterator
        """
        self.iterator = ImageIterator(self.csv_path)
        iter(self.iterator)

    def load_csv(self) -> None:
        """
        Opens file dialog window and loads first image from dataset
        """
        filename, _ = QFileDialog.getOpenFileName(self.container, "Select a File", "", "CSV file (*.csv)")
        try:
            self.csv_path = filename
            self.set_iterator()
            self.next_img()
        except:
            self.display_error("Something went wrong! File wasn't opened.")

    def next_img(self) -> None:
        """
        Changes current displaying image and its title
        """
        try:
            next_img_path = next(self.iterator)
            self.image.setPixmap(QtGui.QPixmap(next_img_path).scaled(self.image.size(), QtCore.Qt.KeepAspectRatio))
            self.img_title.setText("Current image: " + os.path.basename(next_img_path))
        except StopIteration:
            self.set_iterator()
            self.next_img()
        except:
            self.display_error("Can't show image! Maybe you haven't loaded CSV or "
                               "dataset is not valid.")

    def display_error(self, text: str) -> None:
        """
        Pops error window
        :param text: description of error
        """
        err = QMessageBox()
        err.setWindowTitle("Error!")
        err.setText(text)
        err.setIcon(QMessageBox.Warning)
        err.exec()
