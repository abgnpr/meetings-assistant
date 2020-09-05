from logger import log
import tkinter as tk


class LoggerPrompt(tk.Frame):
    def __init__(self, master=None, meetingName='meeting'):
        super().__init__(master)
        self.master = master
        self.meetingName = meetingName
        self.pack()
        self.createButtons()

    def createButtons(self):
        self.attending = tk.Button(
            self, text="↻", bg="yellow")
        self.attending.pack(side="left")
        self.attending = tk.Button(
            self, text="Attending", bg="green", command=self.logPresence)
        self.attending.pack(side="left")
        self.not_attending = tk.Button(
            self, text="Not attending", bg="red", command=self.logAbsence)
        self.not_attending.pack(side="left")
        self.no_class_today = tk.Button(
            self, text="No class today", command=self.master.destroy)
        self.no_class_today.pack(side="bottom")

    def logPresence(self):
        log(self.meetingName, 'P')
        self.master.destroy()

    def logAbsence(self):
        log(self.meetingName, 'A')
        self.master.destroy()

def showLoggerPrompt(meetingName):
    window = tk.Tk()
    window.title('Meetings Logger')
    loggerPrompt = LoggerPrompt(master=window, meetingName=meetingName)
    loggerPrompt.mainloop()
