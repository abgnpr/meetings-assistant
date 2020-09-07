#!/usr/bin/env python3

from os import environ, path

user = environ.get('USER')
current_directory = path.dirname(path.realpath(__file__))

with open('meetings.service', 'w') as d:
    d.writelines(
        f'[Unit]\n\
Description=Meetings Assistant\n\
After=basic.target graphical.target local.fs.target paths.target sysinit.target time-sync.target timers.target\n\
[Service]\n\
User={user}\n\
Type=simple\n\
ExecStart={current_directory}/main.py\n\
Restart=on-failure\n\
[Install]\n\
WantedBy=multi-user.target\n'
    )
