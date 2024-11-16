from dataset_viewer import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog



def main() -> None:
    try:

        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(window)
        window.show()

        ui.btn_exit.clicked.connect(lambda: sys.exit(app.exec_()))
        sys.exit(app.exec_())
    except Exception as ex:
        print("Error in main:", ex)


if __name__ == "__main__":
    main()
