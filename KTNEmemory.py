#
# -*- coding: utf-8 -*-
# KTNEmemory.py
#   by Pixel

import sys

# globals
START = True
STAGE = 0
STAGES = 5
STAGE_LIST = {
  1:0,
  2:0,
  3:0,
  4:0,
  5:0}

# functions
def nextStage():
  STAGE += 1
  if STAGE > STAGES:
    print("All stages done.")
    ask()
def getStageNo(STAGE):
  while STAGE_LIST[STAGE] not in range(1, 6):
    try:
      STAGE_LIST[STAGE] = int(input('Display integer: '))
    except ValueError as e:
      print("Integer!")
      STAGE_LIST[STAGE] = 0
  else:
    print("Integer out of range!")
    STAGE_LIST[STAGE] = 0
def ask():
  if 'y' in input('Repeat?[N/y] ').lower(): cli()
  else: sys.exit()

# iface functions
def gui():
  print("GUI not avaible now,\ please wait for update")
  sys.exit()
def cli():
  try:
    if START:
      print("\n\n\t=== KTaNE Memory cheat v0.5 ===\n\t\t--- by Pixel ---\n\n")
      START = not START


  except KeyboardInterrupt:
    print("[*]Interrupted by user")
    sys.exit()

# main functions
def main(iface):
  if iface in ('-g', '--gui'):
    gui()
  else: cli()
if __name__ == '__main__':
  main(sys.argv[1:])
