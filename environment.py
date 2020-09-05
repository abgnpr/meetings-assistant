import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.environ.setdefault('DISPLAY', ':0')
os.environ.setdefault('XAUTHORITY', '/run/user/1000/gdm/Xauthority')
os.environ.setdefault('DBUS_SESSION_BUS_ADDRESS',
                      'unix:path=/run/user/1000/bus')
