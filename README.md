# Meetings assistant

A service to assist you in attending your daily online meetings.

Platform: Linux _(graphical)_

For: Oblivious people like me who sit in front of their systems for the whole day and tend to forget their meetings.

## What it does

![Demo](images/demo.gif)

When it's time for a meeting,

- The meeting-assistant service:

  - shows a reminder notification, and
  - opens an assistant window

- The assistant window:

  - loads a meeting according to the schedule
  - opens the browser at the appropriate meeting join page (according to the id)
  - copies your name to clipboard. (Hit paste and join)
  - holds the meeting password. (Click to copy)
  - gives options to update your local attendance sheet

## How it works

![Overview](images/overview.svg)

## Installation

- python (get a distribution that supports `tkinter`)

  ```bash
  sudo apt-get install python3-tk
  ```

- scripts

  ```bash
  git clone https://github.com/mountAP/meetings-assistant.git
  cd meetings-assistant
  pip3 install -r requirements.txt
  ```

- service

  ```bash
  ./installer.sh --install
  ```

- check status

  ```bash
  systemctl status meetings-assistant
  ```

## Schedule your meetings

You can modify **`data.yaml`** and add any number of meetings to the list.

**Note**

- Meeting time must be quoted `'HH:MM'`

- Meeting time must be in 4 digit representation `HH:MM`.

- Preceding 0 is necessary for single digit hours and minutes. These are wrong: `10:2`, `4:25`; these are right: `10:02`, `04:25`.

- Valid values for `days`
  - a list of unquoted weekday names<br>
    `- Monday`<br>
    `- Tuesday`<br>
    `...`<br>
    `- Sunday`<br>
  - an array of quoted weekday names
    `[ 'Monday', 'Tuesday', ..., 'Sunday' ]`
  - a string value
    `'everyday'` or `'Everyday'`

```yaml
# data.yaml

attendee-name: John Doe

meetings:
  - name: Sample meeting 1
    id: 2813176975
    pswd: xxxxxx
    time: '09:00' # <---- quotes important!
    days:
      - Monday
      - Wednesday
      - Friday

  - name: Sample meeting 2
    id: 7709185120
    pswd: yyyyyyy
    time: '10:30'
    days: everyday

  - name: Sample meeting 3
    id: 7709185120
    pswd: zzzzzzz
    time: '04:15'
    days: ['Tuesday', 'Thursday'] # <---- quotes important!


  #  ... add more
```

## Attendance Log

Attendance sheet **`attendance-log.csv`** can be found inside `meetings-assistant/` folder. It can be viewed using any spreadsheet software.

## Test

To test if its working, schedule a test meeting in the next 1-2 minutes and see if the Assistant Window shows up.
