from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time

def notify(title, msg):
    message_map = { win32con.WM_DESTROY: onDestroy, }

    # Register the Window class.
    wc = WNDCLASS()
    hinst = wc.hInstance = GetModuleHandle(None)
    wc.lpszClassName = "PythonTaskbar"
    wc.lpfnWndProc = message_map # could also specify a wndproc.
    classAtom = RegisterClass(wc)

    style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
    flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
    icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE

    hwnd = CreateWindow(
        classAtom, "Taskbar", style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hinst, None
    )
    UpdateWindow(hwnd)


    iconPathName = os.path.abspath(os.path.join( sys.path[0], "images/meeting.ico" ))
    try:
        hicon = LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
    except:
        hicon = LoadIcon(0, win32con.IDI_APPLICATION)
    nid = (hwnd, 0, flags, win32con.WM_USER+20, hicon, "Meetings Assistant")


    Shell_NotifyIcon(NIM_ADD, nid)
    Shell_NotifyIcon(NIM_MODIFY,(
        hwnd, 0, NIF_INFO, win32con.WM_USER+20, hicon,
        "Balloon tip",title,200,msg
        )
    )

    time.sleep(5)

    DestroyWindow(hwnd)


def onDestroy(hwnd, msg, wparam, lparam):
    nid = (hwnd, 0)
    Shell_NotifyIcon(NIM_DELETE, nid)
    PostQuitMessage(0) # Terminate the app.
