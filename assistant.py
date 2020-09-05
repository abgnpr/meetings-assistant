import environment
from logger import log
from webbrowser import open_new
from tkinter import Tk, Frame, Button

tkRoot = Tk()

class AssistantWindow(Frame):
    def __init__(self, master=tkRoot, meeting={}, attendeeName='Username'):
        super().__init__(master)
        self.master = master
        self.meeting = meeting
        self.attendeeName = attendeeName
        self.pack()
        self.setTitle()
        self.createButtons()
        self.copyNameToClip()
    

    def setTitle(self):
        self.master.title('Meeting: ' + self.meeting['name'])


    def createButtons(self):
        
        """Join Controls"""
        self.join = Button(self, text="Join Meeting!", bg="yellow", command=self.openBrowser)
        self.join.pack(side="left")

        self.reload = Button(self, text="↻", command=self.openBrowser)
        self.reload.pack(side="left")
        
        self.copyPswd = Button(self, text="Copy password", command=self.copyPswdToClip)
        self.copyPswd.pack(side="left")

        """attendance buttons"""
        self.attending = Button(self, text="Attending", bg="green", command=self.logPresence)
        self.attending.pack(side="left")
        
        self.not_attending = Button(self, text="Not attending", bg="red", command=self.logAbsence)
        self.not_attending.pack(side="left")
        
        self.no_class_today = Button(self, text="No class today", command=self.master.destroy)
        self.no_class_today.pack(side="bottom")


    def openBrowser(self):
        open_new('https://zoom.us/wc/join/' + self.meeting['id'])
        # self.join.changeText =


    def copyNameToClip(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.attendeeName)


    def copyPswdToClip(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.meeting['pswd'])


    def logPresence(self):
        log(self.meeting['name'], 'P') # mark absent
        self.master.destroy()


    def logAbsence(self):
        log(self.meeting['name'], 'A') # mark present
        self.master.destroy()


    def show(self):
        self.mainloop()
