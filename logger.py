import csv
from utility import dateToday, timeNow


def init():
    with open('meetings-log.csv', 'w', newline='') as csvfile:
        log = csv.writer(csvfile, delimiter=',')
        log.writerow(['Date', 'Time', 'Subject/Topic', 'Attendance'])


def log(meetingName, attendance):
    with open('meetings-log.csv', 'a', newline='') as csvfile:
        log = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        log.writerow([
            dateToday(), timeNow(), meetingName, attendance
        ])

# todo: add file exists??

init()