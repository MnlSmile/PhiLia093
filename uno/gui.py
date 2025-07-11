#import PhiLia093.h
#from PhiLia093.h import *
import sys
import os
from stdqt import *

# class Avatar(QWidget):  这样写不行!
class Avatar(QLabel):
    def __init__(self, parent:'ActionQueueGui', qqid:int):
        super().__init__(parent)
        self.player_id = qqid
        self.css = f"""
Avatar {{
    border-radius: 10px;
    border: black solid 2px;
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
            
app = QApplication(sys.argv)
window = QWidget()
window.setFixedSize(400, 400)
actionque = ActionQueueGui(window)
actionque.setGeometry(0, 0, 10**9, 300)
actionque.refresh_actionque()

window.show()
app.exec()