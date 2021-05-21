# pytimer
a thing i hacked together in 5 minutes when i needed something like a timer on my terminal and then decided to make it public

# how to run this thing
make sure you have the musicalbeeps library installed, if not, run the command

    $ pip3 install -r requirements.txt

to install the latest version i tested this thing in

or

    $ pip3 install musicalbeeps

to install the latest version.

and then run the script with whatever name is your python3 executable.

i tested this on python 3.9.5, but i'm pretty sure it works on python >= 3.5, the code is pretty basic.

# arguments

currently there is only 1 optional parameter and 1 positional argument

    usage: timer.py [-h] [--log] time

    positional arguments:
      time        time to wait in seconds, postfix with 'm' or 'h' for minutes/hours

    optional arguments:
      -h, --help  show this help message and exit
      --log       wheter or not to display time elapsed and stuff
