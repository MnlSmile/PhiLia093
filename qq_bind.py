from PhiLia093.h import *

LOGIN_WINDOW_TITLE = 'PhiLia093 - User Recognition'
DEBUG_INVALID_QQID = '错的'
HINT_VALID_QQID = ''
HINT_INVALID_QQID = ''
CONFIRM = 'OK'
ALARM_INVALID_QQID = 'Error!'
ALARM_WRITE_FILE_FAIL = '哎呀, 人家的笔记本居然写不了字了!' + endl + 'Error.System.FileIOFail'

ALARM_INVALID_QQID_FOR_CYRENE_FANS = '哎呀, 这好像不是你的QQ号呢, 可不能骗人家哦?' + endl + 'Error.User.InvalidInput'

# 认出昔涟厨的电脑
def user_feature_recognition() -> int:

    return 3265356703

def text_animation(obj:QObject, text:str, dt:int=20) -> None:
    pass

def user_qq_local_bind_business_flow() -> None:
    global login_window
    login_window = QWidget()
    login_window.setWindowTitle(LOGIN_WINDOW_TITLE)
    login_window.setFixedSize(400, 400)
    
    o_qqid_valid_hint = QLabel(login_window)
    o_qqid_valid_hint.setText(HINT_INVALID_QQID)
    
    o_qqid_lineEdit = QLineEdit(login_window)
    o_qqid_lineEdit.setGeometry(100, 100, 100, 50)

    o_qqid_confirm = QPushButton(login_window)
    o_qqid_confirm.setText(CONFIRM)
    def _dynamic_check(_s:str) -> None:
        if not re.search(r'^[0-9]{6,10}$', _s):
            o_qqid_valid_hint.setText(HINT_INVALID_QQID)
            print(DEBUG_INVALID_QQID)
    def _check() -> bool:
        return bool(re.search(r'^[0-9]{6,10}$', o_qqid_lineEdit.text()))
    def _set() -> None:
        if _check():
            def _thread():
                try:
                    with open('./cache/qq_bind', 'w', encoding='utf-8') as f:
                        f.write(o_qqid_lineEdit.text())
                except Exception:
                    AlarmWindow(ALARM_WRITE_FILE_FAIL)
            _t = Thread(target=_thread)
            _t.start()
        else:
            error_window = AlarmWindow(ALARM_INVALID_QQID_FOR_CYRENE_FANS)
            #o_sound = QMultimedia()
            ...
    o_qqid_lineEdit.textChanged.connect(_dynamic_check)
    o_qqid_confirm.clicked.connect(_set)

    login_window.show()