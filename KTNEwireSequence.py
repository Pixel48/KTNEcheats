#
# -*- coding: utf-8 -*-
# KTNEwireSequence.py
#   by Pixel

import sys

# globals
COUNTER = {'red':0, 'blue':0, 'black':0}
START = True

# functions
def getPos():
  pos = ''
  while pos not in ('a', 'b', 'c'):
    pos = input('Wire slot (A, B or C): ').lower()
  return pos
def getColor():
  color = ''
  while color not in ('red', 'blue', 'black'):
    color = input('Wire color (Red, Blue, Black): ').lower()
  if color == 'red':
    COUNTER['red'] += 1
    return 'red'
  elif color == 'blue':
    COUNTER['blue'] += 1
    return 'blue'
  elif color == 'black':
    COUNTER['black'] += 1
    return 'black'
def doCut(color, pos):
  if color == 'red':
    if pos == 'a' and COUNTER[color] in (3, 4, 6, 7, 8):
        return True
    elif pos == 'b' and COUNTER[color] in (2, 5, 7, 9):
        return True
    elif pos == 'c' and COUNTER[color] in (1, 4, 6, 7):
        return True
  elif color == 'blue':
    if pos == 'a' and COUNTER[color] in (2, 4, 8, 9):
        return True
    elif pos == 'b' and COUNTER[color] in (1, 3, 5, 6):
        return True
    elif pos == 'c' and COUNTER[color] in (2, 6, 7, 8):
        return True
  elif color == 'black':
    if pos == 'a' and COUNTER[color] in (1, 2, 4, 7):
        return True
    elif pos == 'b' and COUNTER[color] in (1, 3, 5, 6, 7):
        return True
    elif pos == 'c' and COUNTER[color] in (1, 2, 4, 6, 8, 9):
        return True
  else:
    return False

# iface functions
def gui():
  print("GUI not avaible now,\ please wait for update")
  sys.exit()
def cli():
  try:
    if START:
      print("\n\n\t=== KTaNE Wire sequences cheat v0.5 ===\n\t\t--- by Pixel ---\n\n")
      START = False
    color = getColor()
    pos = getPos()
    if doCut(color, pos):
      print("\n\tCut.\n")
    else:
      print("\n\tDON\'T CUT!")
    if 'n' in input('Next wire?[Y/n] ').lower():
      if 'n' in input('Restart?[Y/n] ').lower():
        sys.exit()
      else:
        START = True
        cli()
    else:
      cli()
  except KeyboardInterrupt:
    print('[!]Interrupted by user\n')
    time.sleep(1)
    sys.exit()

# main functions
def main(iface):
  if iface in ('-g', '--gui'):
    gui()
  else:
    cli()
if __name__ == '__main__':
  main(sys.argv[1:])
