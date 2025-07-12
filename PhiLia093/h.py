import stdqt
import threading
import re
import requests
import asyncio
import asyncqt
import httpx
import sys
import os
import functools
import random

from threading import Thread
from stdqt import *
from typing import *

ALARM_WINDOW_TITLE = '!!!'
class AlarmWindow:
    instances = []
    def __init__(self, tip:str) -> None:
        AlarmWindow.instances += [self]
        self.tip = tip
        self.alarm_window = QWidget()
        self.alarm_window.setFixedSize(200, 300)
        self.alarm_window.setWindowTitle(ALARM_WINDOW_TITLE)
        self.o_tip = QLabel(self.alarm_window)
        self.o_tip.setFixedSize(self.alarm_window.size())
        self.o_tip.setText(self.tip)
        self.alarm_window.show()
    def __del__(self) -> None:
        print('shan le!')

class CustomQThread(QThread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args,  **kwargs)
        self.target_func = lambda : print('void function')
    def setTargetFunction(self, func) -> None:
        self.target_func = func
    def run(self) -> None:
        self.target_func()

endl = '\n'