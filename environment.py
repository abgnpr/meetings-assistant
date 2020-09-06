import os

# change to current director
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# environment variables needed to run
# in system mode (root) on linux.
os.environ.setdefault('DISPLAY', ':0')
os.environ.setdefault('XAUTHORITY', '/run/user/1000/gdm/Xauthority')
os.environ.setdefault('DBUS_SESSION_BUS_ADDRESS',
                      'unix:path=/run/user/1000/bus')

# NOTE: If the program fails to run on your linux machine,
#       look for the correct values of the above variables
#       for your system. Replace them here if needed. You
#       may use commands `env` or `printenv` in user mode
#       to view the environment variables for your system