import sys

from Copying import CopyFiles as Copy
from PySide6.QtWidgets import *
from Design import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame_8.hide()
        self.inputButtom()

    def inputButtom(self):
        self.ui.toolButton.clicked.connect(lambda: self.ui.lineEdit.setText(QFileDialog.getExistingDirectory()))
        self.ui.toolButton_2.clicked.connect(lambda: self.ui.lineEdit_2.setText(QFileDialog.getExistingDirectory()))
        self.ui.pushButton_2.clicked.connect(lambda: Copy(self.ui, True))


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
