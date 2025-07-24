import sys
from PhiLia093.h import *
from stdqt import *
from ctypes import windll

def set_cursor_pos(x, y):
    windll.user32.SetCursorPos(x, y)

def block_input(block:bool):
    windll.user32.BlockInput(block)

class RemoteCopyClient(QWebSocket):
    def __init__(self) -> None:
        super().__init__()
        self.window = RemoteCopyWindow(self.current_code)
        self.current_code:str|None = None
        self.textMessageReceived.connect(self.cuslot_on_text_message_received)
        self.open(QUrl('ws://47.119.20.14:52520/remote_copy'))
    def cuslot_on_text_message_received(self, msg:str) -> None:
        def _set_code(code:str):
            self.current_code = code
            self.window.o_code.setText(code)
            self.window.show()
        with mccmd.Parser(msg) as parser:
            parser.resolve_overload_and_bind(
                {
                    ('/join', str): _set_code
                }
            )

class RemoteCopyWindow(QWidget):
    def __init__(self, code:str) -> None:
        super().__init__()      
        self.code = code

        self.setGeometry(1920 - 400 - 20, 1080 - 200 - 70, 400, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.o_code = QLabel(self)
        self.o_code.setGeometry(0, 75, 400, 50)
        self.o_code.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.o_code.setFont(QFont('汉仪旗黑 75S', 36))
        self.o_code.setText(code)

        self.o_btn = QPushButton(self)
        self.o_btn.setGeometry((400 - 120) // 2, 75 + 50 + 10, 120, 50)
        self.o_btn.setFont(QFont('汉仪旗黑 55S', 18))
        self.o_btn.setText('帮我输')
        self.o_btn.clicked.connect(self.code_inputing_flow)

        #self.o_cyrene = QImage()
    def code_inputing_flow(self) -> None:
        def _thread():
            block_input(True)  # 屏蔽输入
            try:
                game = FindWindow(None, 'Draw&Guess')
                print(game)
                if game:
                    if re.search(r'^[a-zA-Z]{4}$', self.code):
                        op1 = (476, 320)
                        op2 = (784, 480)
                        x1, y1, x2, y2 = GetWindowRect(game)
                        dx = abs(x2 - x1)
                        dy = abs(y2 - y1)
                        p1 = (int(dx * (op1[0] / 1280)), int(dy * (op1[1] / 720)))
                        p2 = (int(dx * (op2[0] / 1280)), int(dy * (op2[1] / 720)))
                        p1_lparam = (p1[1] << 16) | p1[0]
                        p2_lparam = (p2[1] << 16) | p2[0]
                        
                        set_cursor_pos(x1 + p1[0], y1 + p1[1])
                        PostMessage(game, WM_LBUTTONDOWN, 0, p1_lparam)
                        PostMessage(game, WM_LBUTTONUP, 0, p1_lparam)
                        time.sleep(0.1)
                        PostMessage(game, WM_LBUTTONDOWN, 0, p1_lparam)
                        PostMessage(game, WM_LBUTTONUP, 0, p1_lparam)
                        time.sleep(0.5)

                        set_cursor_pos(x1 + p2[0], y1 + p2[1])
                        PostMessage(game, WM_LBUTTONDOWN, 0, p2_lparam)
                        PostMessage(game, WM_LBUTTONUP, 0, p2_lparam)
                        time.sleep(0.5)
                        PostMessage(game, WM_LBUTTONDOWN, 0, p2_lparam)
                        PostMessage(game, WM_LBUTTONUP, 0, p2_lparam)
                        time.sleep(0.1)
                        
                        for char in self.code:
                            PostMessage(game, WM_CHAR, ord(char.upper()), 0)
                        time.sleep(0.2)
                        SendMessage(game, WM_KEYDOWN, VK_RETURN, 0)
                        SendMessage(game, WM_KEYUP, VK_RETURN, 0)
            finally:
                block_input(False)  # 恢复输入
        Thread(target=_thread).start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RemoteCopyWindow('ABCD')
    window.show()
    app.exec()