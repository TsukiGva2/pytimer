# pytimer
a thing i hacked together in 5 minutes when i needed something like a timer on my terminal and then decided to make it public

# how to run this thing
make sure you have the musicalbeeps library installed, if not, run the command

    $ pip3 install -r requirements.txt

to install the latest version i tested this thing in

or

    $ pip3 install musicalbeeps

to install the latest version (NOTE: replace pip3 with your pip executable name).

and then run the script with whatever name is your python3 executable.

i tested this on python 3.9.5, but i'm pretty sure it works on python >= 3.5, the code is pretty basic.

# arguments

currently there is only 1 optional parameter and 1 positional argument

    usage: pytimer.py [-h] [--log LOG] [--repeat] time

    positional arguments:
      time        time to wait in seconds, postfix with 'm' or 'h' for minutes/hours

    optional arguments:
      -h, --help  show this help message and exit
      --log LOG   wheter or not to display time elapsed and stuff, takes the time between logs as an argument
      --repeat    when used makes the song at the end repeat until interrupted

# how to specify time

you can specify the time for the timer in two different ways

- you can write it like: "hh:mm:ss", e.g. 1:2:3 or 01:02:03 but not 001:002:003
- or you can write a single number with a postfix, e.g. 10s = 10 = 00:00:10, 10m = 00:10:00, 10h = 10:00:00

# yes it plays a little song when it's over so cute uwu
