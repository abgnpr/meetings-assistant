import environment_setup
from tkinter import Tk, Frame, Label, Button, TRUE, LEFT, RIGHT, X, Y
from logger import log
from webbrowser import open_new


class AssistantWindow(Frame):
    """ tkinter GUI to assist in attending meetings """

    def __init__(self, meeting={}, attendeeName='Username'):
        self.master = Tk()
        # keep on top of other windows until dismissed
        self.master.call('wm', 'attributes', '.', '-topmost', '1')
        super().__init__(self.master)

        self.meeting = meeting
        self.attendeeName = attendeeName
        
        self.pack()
        self.setup()
        self.copyAttendeeToClip()
        self.show()


    def show(self):
        """ displays the assistant console """
        self.mainloop()


    def close(self):
        """ closes the assistant window """
        self.master.destroy()


    def openBrowser(self):
        """ opens the browser with meeting url and id """
        open_new('https://zoom.us/wc/join/' + self.meeting['id'])
        self.join.configure(text="Join again ↻")


    def copyAttendeeToClip(self):
        """ copies attendee name to clipboard """
        self.master.clipboard_clear()
        self.master.clipboard_append(self.attendeeName)
        self.copyAttendee.configure(text='Copied!')
        self.copyPswd.configure(text='Copy')


    def copyPswdToClip(self):
        """ copies meeting password to clipboard """
        self.master.clipboard_clear()
        self.master.clipboard_append(self.meeting['pswd'])
        self.copyAttendee.configure(text='Copy')
        self.copyPswd.configure(text='Copied!')


    def logPresence(self):
        """ marks meeting attendance as present 'P' """
        log(self.meeting['name'], 'P')
        self.close()


    def logAbsence(self):
        """ marks meeting attendance as absent 'A' """
        log(self.meeting['name'], 'A')
        self.close()


    def setup(self):
        """ prepare the widget layout """

        """ set window title """
        self.master.title('Meetings Assistant')
        
        """ top: meeting name & join button """
        self.top = Frame(self)
        self.top.pack(fill=X)

        self.meetingTitleText = Label(self.top, text='Meeting : ' + self.meeting['name'])
        self.meetingTitleText.pack(fill=X, pady=10)
        
        self.join = Button(self.top, text="Join!", bg="yellow", command=self.openBrowser)
        self.join.pack(pady=10)

        """ attendee name """
        self.mid1 = Frame(self)
        self.mid1.pack(fill=X, padx = 25)
        
        self.attendeeText = Label(self.mid1, text='Attendee  :   ' +self.attendeeName)
        self.attendeeText.pack(side=LEFT)

        self.copyAttendee = Button(self.mid1, text="Copy", command=self.copyAttendeeToClip)
        self.copyAttendee.pack(side=RIGHT, padx=20)

        """ password """
        self.mid2 = Frame(self)
        self.mid2.pack(fill=X, padx=25)

        self.pswdText = Label(self.mid2, text='Password :   [   ' + self.meeting['pswd'] + '   ]')
        self.pswdText.pack(side=LEFT)

        self.copyPswd = Button(self.mid2, text="Copy", command=self.copyPswdToClip)
        self.copyPswd.pack(side=RIGHT, padx=20)

        """ bottom: attendance log """
        self.bottom = Frame(self)
        self.bottom.pack(fill=X, pady=10, padx=5)

        self.attendanceText = Label(self.bottom,text='Attendance Log')
        self.attendanceText.pack(fill=X, pady=10)

        self.attending = Button(self.bottom, text="Attending", bg="green", command=self.logPresence)
        self.attending.pack(side=LEFT, expand=TRUE)
        
        self.notAttending = Button(self.bottom, text="Not attending", bg="red", command=self.logAbsence)
        self.notAttending.pack(side=LEFT, expand=TRUE)
        
        self.noUpdate = Button(self.bottom, text="Don't log", command=self.close)
        self.noUpdate.pack(side=LEFT, expand=TRUE)

