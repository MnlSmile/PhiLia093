import PhiLia093.h
from PhiLia093.h import *

class CustomQThread(QThread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args,  **kwargs)
        self.target_func = lambda : print('void function')
    def setTargetFunction(self, func) -> None:
        self.target_func = func
    def run(self) -> None:
        self.target_func()

def main():
    if not os.path.exists('./cache'):
        os.mkdir('cache')
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('PhiLia093')
    window.show()

    qq_bind.user_qq_local_bind_business_flow()
    return app.exec()

if __name__ == '__main__':
    thread = CustomQThread()
    thread.start()
    sys.exit(main())