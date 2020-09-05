from datetime import datetime
from subprocess import Popen, PIPE, DEVNULL

def dateToday():
    return '05/09/2020'

def timeNow():
    h = datetime.now().hour
    m = datetime.now().minute
    h = str(h) if h > 9 else '0' + str(h)
    m = str(m) if m > 9 else '0' + str(m)
    return h + ':' + m

def copyToClipboard(text):
    echo = Popen(['echo', text], stdout=PIPE)
    Popen(['xclip', '-sel', 'clip'], stdin=echo.stdout)