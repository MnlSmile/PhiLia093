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
import win32gui
import win32con
import pyautogui
import MCLikeCommandParser as mccmd
import psutil
import time

from win32con import *
from win32gui import *
from threading import Thread
from stdqt import *
from typing import *

ALARM_WINDOW_TITLE = '!!!'
class AlarmWindow:
    instances = []
    def __init__(self, tip:str) -> None:
        AlarmWindow.instances += [self]

        self.alarm_window = QWidget()
        self.alarm_window.setFixedSize(800, 200)
        self.alarm_window.setWindowTitle(ALARM_WINDOW_TITLE)

        self.o_tip = QLabel(self.alarm_window)
        self.o_tip.setFixedWidth(self.alarm_window.width())
        self.o_tip.setMinimumHeight(100)
        self.o_tip.setWordWrap(True)
        self.o_tip.setTextFormat(Qt.RichText)
        _splited = tip.split(endl)
        self.tip = endl.join(_splited[:-1])
        self.err = _splited[-1]
        self.tiptext = f"""
        <head>
            <style>
                * {{
                    margin: 0px, 0px, 0px, 0px;
                }}
            </style>
        </head>
        <p>
            <font face=\"汉仪旗黑 75S\" size=\"48\">
                {self.tip}
            </font>
        </p>
        <p>
            <font face=\"汉仪旗黑 55S\" size=\"24\">
                {self.err}
            </font>
        </p>
        """
        self.o_tip.setText(self.tiptext)
        def _thread():
            try:
                with open('./global.css', 'r', encoding='utf-8') as f:
                    css = f.read()
                self.alarm_window.setStyleSheet(css)
            except Exception:
                pass
        Thread(target=_thread).start()

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