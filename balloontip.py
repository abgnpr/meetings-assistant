from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
 
class BalloonTip:
    def __init__(self):
        message_map = { win32con.WM_DESTROY: self.onDestroy, }
        
        # Register the Window class.
        wc = WNDCLASS()
        self.hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = "PythonTaskbar"
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        self.classAtom = RegisterClass(wc)
        
        self.style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        
        iconPathName = os.path.abspath(os.path.join( sys.path[0], "balloontip.ico" ))
        try:
            self.hicon = LoadImage(hinst, iconPathName, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            self.hicon = LoadIcon(0, win32con.IDI_APPLICATION)
        
        
    def show(self, title, msg):
        """ Shows balloon notification """
        self.hwnd = CreateWindow(
            self.classAtom, "Taskbar", self.style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, self.hinst, None
        )
        UpdateWindow(self.hwnd)
        self.nid = (self.hwnd, 0, self.flags, win32con.WM_USER+20, self.hicon, "Meetings Assistant")
        Shell_NotifyIcon(NIM_ADD, self.nid)
        Shell_NotifyIcon(NIM_MODIFY,(
            self.hwnd, 0, NIF_INFO, win32con.WM_USER+20, self.hicon, 
            "Balloon tip",title,200,msg
            )
        )


    def destroy(self):
        DestroyWindow(self.hwnd)


    def onDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, self.nid)
        PostQuitMessage(0) # Terminate the app.