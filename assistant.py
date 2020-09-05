from tkinter import Frame, Button, Tk
from webbrowser import open_new
from logger import log

tkRoot = Tk()

class AssistantWindow(Frame):
    def __init__(self, master=None, meeting={}):
        super().__init__(master)
        self.master = master
        self.meeting = meeting
        self.pack()
        self.setTitle()
        self.createButtons()
    
    def setTitle(self):
        self.master.title(self.meeting['name'])

    def createButtons(self):
        self.attending = Button(self, text="Join Meeting!", bg="yellow", command=self.joinMeeting)
        self.attending = Button(self, text="↻", bg="yellow")
        self.attending = Button(self, text="Attending", bg="green", command=self.logPresence)
        self.not_attending = Button(self, text="Not attending", bg="red", command=self.logAbsence)
        self.no_class_today = Button(self, text="No class today", command=self.master.destroy)
        self.attending.pack(side="left")
        self.attending.pack(side="left")
        self.not_attending.pack(side="left")
        self.no_class_today.pack(side="bottom")

    def joinMeeting(self):
        open_new('https://zoom.us/wc/join/' + self.meeting['id'])

    def logPresence(self):
        log(self.meeting['name'], 'P')
        self.master.destroy()

    def logAbsence(self):
        log(self.meeting['name'], 'A')
        self.master.destroy()

    def show(self):
        self.mainloop()


assistant = AssistantWindow(master=tkRoot, meeting='')



# todo Copy to clipboard
