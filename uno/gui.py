#import PhiLia093.h
#from PhiLia093.h import *
import sys
import os
import threading
from stdqt import *

ROWDY = 30

class Fonts():
    @staticmethod
    def initialize():
        fontdb = QtGui.QFontDatabase()
        _hyqh_55s_font_id = fontdb.addApplicationFont('./font/HYQiHei_55S.ttf')
        _hyqh_75s_font_id = fontdb.addApplicationFont('./font/HYQiHei_75S.ttf')

    font_harmony = QFont()
    font_harmony.setFamily("汉仪旗黑 75w")

    font_harmony_title = QFont()
    font_harmony_title.setFamily("HarmonyOS Sans SC Black")

class CustomQThread(QThread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args,  **kwargs)
        self.target_func = lambda : print('void function')
    def setTargetFunction(self, func) -> None:
        self.target_func = func
    def run(self) -> None:
        self.target_func()

# class Avatar(QWidget):  这样写不行!
class Avatar(QLabel):
    def __init__(self, parent:'ActionQueueGui', qqid:int):
        super().__init__(parent)
        self.player_id = qqid
        self.css = f"""
Avatar {{
    border-radius: 10px;
    border-image: url(D:/python_works/PhiLia093/cache/avatar_{qqid}.png);
}}
"""
        self.setStyleSheet(self.css)
        self.show()
    def switch_to_big(self) -> None:
        print('变大动画')
    def switch_to_small(self) -> None:
        print('变小动画')

class ActionQueueGui(QWidget):
    def __init__(self, parent:QWidget):
        super().__init__(parent)
        self.actionque:list[int] = [986561577, 1590947611, 3265356703, 3484868850]
        self.players:list[int] = [986561577, 1590947611, 3265356703, 3484868850]
        self.action_avatar_que:list[Avatar] = []
        self.cnt_players = 0
        self.player_lock = False
    def reverse(self) -> None:
        self.actionque.reverse()
        self.refresh_actionque()
    def append_left(self, user:int) -> None:
        self
    def append(self, user:int) -> None:
        self
    def pop_left(self) -> None:
        self
    def refresh_actionque(self) -> None:
        self.action_avatar_que.clear()
        for i, user in enumerate(self.actionque):
            ava = Avatar(self, user)
            self.action_avatar_que += [ava]
            if i == 0:
                ava.switch_to_big()
                ava.setGeometry(*self.calc_avatar_pos(i), 100, 100)
            else:
                ava.switch_to_small()
                ava.setGeometry(*self.calc_avatar_pos(i), 64, 64)
    def calc_avatar_pos(self, i:int) -> tuple[int, int]:  # 算头像坐标
        ans = (0, 0)
        x = 0
        y = 0
        deltax = 10
        if i == 0:
            dx = 100
            dy = 100
            x = 15
            y = 0
            ans = (x, y)
        else:
            dx = 64
            dy = 64
            x = 15 + 100 + i * deltax + (i - 1) * dx
            y = 36
            ans = (x, y)
        return ans

class RankRow(QWidget):
    def __init__(self, parent, user:int):
        super().__init__(parent)
        self.setFixedSize(300, 50)

        self.o_number = QLabel(self)
        self.o_number.setGeometry(0, 0, 50, ROWDY)

        self.o_player = QLabel(self)
        self.o_player.setGeometry(50, 0, 175, ROWDY)
        
        self.o_score = QLabel(self)
        self.o_score.setGeometry(225, 0, 75, ROWDY)
        
        self.setup_test_values()
    def setup_test_values(self):
        self.o_number.setText('1')
        self.o_player.setText('Test')
        self.o_score.setText('100')

class RankGui(QWidget): 
    def __init__(self, parent):
        super().__init__(parent)
        self.rows:list[RankRow] = []
        self.o_title = QLabel(self)
        self.o_title.setText('名次')
        self.o_title.setGeometry(0, 0, 300, 70)
        self.setup_test_values()
    def init_row(self, user:int) -> None:
        self.rows += [RankRow(self, user)]
    def lay_rank_rows(self) -> None:
        self.sort_rank()
        for i, row in enumerate(self.rows):
            x = 0
            y = self.o_title.height() + i * ROWDY
            row.setGeometry(x, y, 300, ROWDY)
    def setup_test_values(self):
        for i in range(7):
            self.init_row(111111)
    def sort_rank(self) -> None:
        return

class OperationZoneGui(QWidget): ...

class GameWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1280, 720)
        self.action_que = ActionQueueGui(self)
        self.action_que.refresh_actionque()
        self.action_que.setGeometry(0, 0, 1280, 200)

        self.rank = RankGui(self)
        self.rank.setGeometry(1280 - 300, 150, 300, 720 - 150)
        self.rank.lay_rank_rows()

        self.operation_zone = OperationZoneGui
        self.thread_load_css()
        
    def thread_load_css(self) -> None:
        def _thread():
            try:
                with open('./uno/global.css', 'r', encoding='utf-8') as f:
                    css = f.read()
                self.setStyleSheet(css)
            except Exception:
                print('unable to load css')
        threading.Thread(target=_thread).start()

class OutWindow(QWidget):
    def __init__(self, user:int):
        super().__init__()
        self.qqid = user

        #self.o_avatar = Avatar(self, user)
        self.o_avatar = Avatar(self, 1590947611)
        self.o_avatar.setGeometry((1920 - 640) // 2, 100, 640, 640)
        
        self.o_out = QLabel(self)
        self.o_out.setGeometry((1920 + 640) // 2 - 400 // 2, 100 + 640 - 400 // 2, 400, 400)
        self.o_out.setPixmap(QPixmap('./uno/r_out.png'))

    def showEvent(self, a0):
        self.playsound()
        _timer = QTimer(self)
        _timer.timeout.connect(self.close)
        _timer.start(14 * 1000)
        super().showEvent(a0)
    def playsound(self) -> None:
        def _play():
            self.med = QMediaPlayer()
            self.med.setMedia(QMediaContent(QUrl.fromLocalFile('D:/python_works/PhiLia093/uno/out.ogg')))
            self.med.setVolume(30)
            self.med.play()
        # 一定要 self. , 否则会被 Python 删掉
        self._thread = CustomQThread()
        self._thread.setTargetFunction(_play)
        self._thread.start()

class UnoMainWindow(QWidget): ...

app = QApplication(sys.argv)

gw = GameWindow()
gw.show()

OutWindow(123333).showFullScreen()

app.exec()