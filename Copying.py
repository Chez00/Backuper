import os
import shutil
import threading
import asyncio


class CopyFiles:
    Prog = 0
    Count = 0
    Locker = threading.Lock()

    def __init__(self, ui, x):
        super().__init__()
        self.ui = ui
        if x:
            self.start_copy()

    def start_copy(self):
        src = self.ui.lineEdit.text()
        dst = self.ui.lineEdit_2.text()
        if src != '' and dst != '':
            self.ui.label_8.setText('Выполняется копирование данных:')
            self.Count = 0
            self.Prog = 0
            self.fcount(src)
            self.ui.progressBar.setValue(0)
            self.ui.frame_8.show()
            copy = threading.Thread(target=self.copytree, args=(src, dst))
            copy.start()
        else:
            print('Error')

    async def progress_bar(self):
        progg = self.Prog / self.Count * 100
        print(round(self.Prog, 2), 'МБ. из ', round(self.Count, 2), 'МБ.')
        self.ui.progressBar.setValue(progg)
        if progg >= 100:
            self.ui.label_8.setText('Копирование завершено!')

        else:
            self.ui.label_8.setText('Выполняется копирование данных:')

    def copytree(self, src, dst, symlinks=False, ignore=None):

        try:
            if not os.path.exists(dst):
                os.makedirs(dst)
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(dst, item)
                self.Prog += os.path.getsize(s) / 1024 / 1024
                if os.path.isdir(s):
                    self.copytree(s, d, symlinks, ignore)
                else:
                    if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                        shutil.copy2(s, d)
                        asyncio.run(self.progress_bar())
        except ValueError:
            print('Error')


    def fcount(self, path):
        for f in os.listdir(path):
            s = os.path.join(path, f)
            self.Count += os.path.getsize(s) / 1024 / 1024
            if os.path.isdir(s):
                self.fcount(s)
