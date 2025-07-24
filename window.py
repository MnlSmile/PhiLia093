import win32gui, win32con, win32api, pyautogui

defview = workerw = 0x0
target = win32gui.FindWindow(None, 'Draw&Guess')
program_manager = win32gui.FindWindow(None, 'Program Manager')
target_parent = win32gui.FindWindow(None, 'PhiLia093')
win32gui.SendMessage(program_manager, 0x52C)
def EnumWindowsProc(tophandle:int, topparamhandle):
    global defview, workerw, target, target_parent
    _tg = win32gui.FindWindowEx(tophandle, 0, None, 'Draw&Guess')
    _dv = win32gui.FindWindowEx(tophandle, 0, "SHELLDLL_DefView", None)
    _ww = win32gui.FindWindowEx(tophandle, 0, "WorkerW", "")
    _tg_parent = win32gui.FindWindowEx(tophandle, 0, None, 'PhiLia093')
    if _dv:
        defview = _dv
    if _ww:
        workerw = _ww
    if _tg:
        target = _tg
    if _tg_parent:
        target_parent = _tg_parent
    return True
win32gui.EnumWindows(EnumWindowsProc, 'a')
reset = 0x0001000C

style = win32gui.GetWindowLong(target, win32con.GWL_STYLE)
style &= ~(win32con.WS_CAPTION | win32con.WS_THICKFRAME)
win32gui.SetWindowLong(target, win32con.GWL_STYLE, style)
win32gui.SetWindowPos(target, None, 0, 0, 0, 0, win32con.SWP_FRAMECHANGED | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

gui_opration_window = pyautogui

#win32gui.SetParent(target, reset)
#win32gui.SetParent(0x000F0C38, workerw)
'''
pm = win32gui.FindWindow(None, 'Program Manager')
win32gui.SendMessage(pm, 0x52C)
def EnumWindowsProc(tophandle:int, topparamhandle):
    global defview
    _dv = win32gui.FindWindowEx(tophandle, 0, "SHELLDLL_DefView", None)
    if _dv:
        defview = _dv
    return True
win32gui.EnumWindows(EnumWindowsProc, 'a')'''