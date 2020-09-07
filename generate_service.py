#!/usr/bin/env python3

from os import environ, path, chmod

service_file = 'meetings_assistant.service'
user = environ.get('USER')
current_directory = path.dirname(path.realpath(__file__))

with open(service_file, 'w') as sf:
    sf.writelines(
        f'[Unit]\n\
Description=Meetings Assistant\n\
After=graphical.target\n\
[Service]\n\
User={user}\n\
Type=simple\n\
ExecStart={current_directory}/main.py\n\
Restart=on-failure\n\
[Install]\n\
WantedBy=multi-user.target\n'
    )

chmod(service_file, 420)  # 644 in octal
