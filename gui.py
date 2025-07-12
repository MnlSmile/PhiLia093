from PhiLia093.h import *

import qq_bind

class MainWindow(QWidget): ...

def main():
    if not os.path.exists('./cache'):
        os.mkdir('cache')

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('PhiLia093')
    try:
        with open('./global.css', 'r', encoding='utf-8') as f:
            css = f.read()
        window.setStyleSheet(css)
    except Exception:
        pass
    window.show()

    qq_bind.user_qq_local_bind_business_flow()
    return app.exec()

if __name__ == '__main__':
    sys.exit(main())