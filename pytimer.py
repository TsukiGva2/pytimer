import musicalbeeps
from time import sleep, time
from sys import argv, exit
from math import floor
import re
import argparse

time_multipliers   = {"s":1, "m":60, "h":3600}
time_multipliers_l = [3600, 60, 1]

def parse_time(some_time):
  result = some_time
  is_precise_time = re.match(r"(\d\d?)(?::(\d\d?))(?::(\d\d?))?", some_time)
  if is_precise_time:
    result = 0
    for index, g in enumerate(is_precise_time.groups("0")):
      result += int(g) * time_multipliers_l[index]
  else:
    tprefix = some_time[-1]
    if tprefix == "m" or tprefix == "h" or tprefix == "s":
      result = int(result[:-1]) * time_multipliers[tprefix]
    else:
      result = int(result)
  return result

def preetify(some_time):
  result = floor(some_time)

  hours, minutes, secs = 0, 0, result

  if secs > 0:
    minutes = floor(secs/60)
    hours   = floor(minutes/60)
    minutes %= 60
    secs    %= 60

  return str("<{h}:{m}:{s}>".format(h=hours, m=minutes, s=secs))

if __name__ == "__main__":
  p = argparse.ArgumentParser()
  p.add_argument("time", help="time to wait in seconds, postfix with 'm' or 'h' for minutes/hours")
  p.add_argument("--log", help="wheter or not to display time elapsed and stuff, takes the time between logs as an argument", type=int)
  p.add_argument("--repeat", help="when used makes the song at the end repeat until interrupted", action="store_true")

  args = p.parse_args()

  elapsed = 0
  prev = time()

  total_time = parse_time(args.time)
  preety_time = preetify(total_time)

  while elapsed < total_time:
    curr = time()
    elapsed += curr - prev
    prev = curr
    if args.log:
      print("elapsed: {e}/{t}".format(e=preetify(elapsed), t=preety_time))
      sleep(args.log)

  print("time's up!")

  try:
    player = musicalbeeps.Player(volume = 0.5, mute_output = True)
    while True:
      for _ in range(0, 4):
        player.play_note("Bb", 0.2)
        player.play_note("A", 0.2)
        player.play_note("Ab", 0.2)
      player.play_note("G", 0.7)
      player.play_note("Gb", 0.4)
      player.play_note("Bb", 0.2)
      if !args.repeat:
        break
  except KeyboardInterrupt:
      exit(0)
