import sys
import os
import shutil
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Design import Ui_MainWindow

class MainWindow(QMainWindow):
    Prog = 0
    Count = 0
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame_8.hide()
        self.inputButtom()

    def inputButtom(self):
        self.ui.toolButton.clicked.connect(lambda: self.ui.lineEdit.setText(QFileDialog.getExistingDirectory()))
        self.ui.toolButton_2.clicked.connect(lambda: self.ui.lineEdit_2.setText(QFileDialog.getExistingDirectory()))
        self.ui.pushButton_2.clicked.connect(lambda: self.startCopy())

    def startCopy(self):
        src = self.ui.lineEdit.text()
        dst = self.ui.lineEdit_2.text()
        if src != '' and dst != '':
            self.Count = 0
            self.Prog = 0
            self.fcount(src)
            self.ui.progressBar.setValue(0)
            self.ui.frame_8.show()
            self.copytree(src, dst)
        else:
            print('Error')


    def copytree(self, src, dst, symlinks=False, ignore=None):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            print('ok')
            self.Prog += 1
            self.ProgressBar()
            if os.path.isdir(s):
                self.copytree(s, d, symlinks, ignore)
            else:
                if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                    shutil.copy2(s, d)

    def ProgressBar(self):
        progg = self.Prog / self.Count * 100
        print(self.Prog, 'Файлов из ', self.Count)
        self.ui.progressBar.setValue(progg)
        if progg >= 100:
            self.ui.label_8.setText('Копирование завершено!')
        else:
            self.ui.label_8.setText('Выполняется копирование данных:')

    def fcount(self, path):
        for f in os.listdir(path):
            s = os.path.join(path, f)
            self.Count += 1
            if os.path.isdir(s):
                print('ss')
                self.fcount(s)
            else:
               print('file')

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


