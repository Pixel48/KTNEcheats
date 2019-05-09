#
# -*- coding: utf-8 -*-
# KTNEwhoIsOn'FIRST'.py
# by Pixel

import sys, time

# globals
TITLES = (
  'YES', 'FIRST', 'DISPLAY', 'OKAY', 'SAYS', 'NOTHING',
  '', ' ', 'BLANK', 'NO', 'LED',  'LEAD', 'READ',
  'RED', 'REED', 'LEED', 'HOLD ON', 'YOU', 'YOU ARE',
  'YOUR', 'YOU\'RE', 'UR', 'THERE', 'THEY\'RE', 'THEIR',
  'THEY ARE', 'SEE', 'C', 'CEE')
WORDS = {
  'READY':     ('YES', 'OKAY', 'WHAT', 'MIDDLE', 'LEFT', 'PRESS', 'RIGHT', 'BLANK', 'READY', 'NO', 'FIRST', 'UHHH', 'NOTHING', 'WAIT'),
  'FIRST':     ('LEFT', 'OKAY', 'YES', 'MIDDLE', 'NO', 'RIGHT', 'NOTHING', 'UHHH', 'WAIT', 'READY', 'BLANK', 'WHAT', 'PRESS', 'FIRST'),
  'NO':        ('BLANK', 'UHHH', 'WAIT', 'FIRST', 'WHAT', 'READY', 'RIGHT', 'YES', 'NOTHING', 'LEFT', 'PRESS', 'OKAY', 'NO', 'MIDDLE'),
  'BLANK':     ('WAIT', 'RIGHT', 'OKAY', 'MIDDLE', 'BLANK', 'PRESS', 'READY', 'NOTHING', 'NO', 'WHAT', 'LEFT', 'UHHH', 'YES', 'FIRST'),
  'NOTHING':   ('UHHH', 'RIGHT', 'OKAY', 'MIDDLE', 'YES', 'BLANK', 'NO', 'PRESS', 'LEFT', 'WHAT', 'WAIT', 'FIRST', 'NOTHING', 'READY'),
  'YES':       ('OKAY', 'RIGHT', 'UHHH', 'MIDDLE', 'FIRST', 'WHAT', 'PRESS', 'READY', 'NOTHING', 'YES', 'LEFT', 'BLANK', 'NO', 'WAIT'),
  'WHAT':      ('UHHH', 'WHAT', 'LEFT', 'NOTHING', 'READY', 'BLANK', 'MIDDLE', 'NO', 'OKAY', 'FIRST', 'WAIT', 'YES', 'PRESS', 'RIGHT'),
  'UHHH':      ('READY', 'NOTHING', 'LEFT', 'WHAT', 'OKAY', 'YES', 'RIGHT', 'NO', 'PRESS', 'BLANK', 'UHHH', 'MIDDLE', 'WAIT', 'FIRST'),
  'LEFT':      ('RIGHT', 'LEFT', 'FIRST', 'NO', 'MIDDLE', 'YES', 'BLANK', 'WHAT', 'UHHH', 'WAIT', 'PRESS', 'READY', 'OKAY', 'NOTHING'),
  'RIGHT':     ('YES', 'NOTHING', 'READY', 'PRESS', 'NO', 'WAIT', 'WHAT', 'RIGHT', 'MIDDLE', 'LEFT', 'UHHH', 'BLANK', 'OKAY', 'FIRST'),
  'MIDDLE':    ('BLANK', 'READY', 'OKAY', 'WHAT', 'NOTHING', 'PRESS', 'NO', 'WAIT', 'LEFT', 'MIDDLE', 'RIGHT', 'FIRST', 'UHHH', 'YES'),
  'OKAY':      ('MIDDLE', 'NO', 'FIRST', 'YES', 'UHHH', 'NOTHING', 'WAIT', 'OKAY', 'LEFT', 'READY', 'BLANK', 'PRESS', 'WHAT', 'RIGHT'),
  'WAIT':      ('UHHH', 'NO', 'BLANK', 'OKAY', 'YES', 'LEFT', 'FIRST', 'PRESS', 'WHAT', 'WAIT', 'NOTHING', 'READY', 'RIGHT', 'MIDDLE'),
  'PRESS':     ('RIGHT', 'MIDDLE', 'YES', 'READY', 'PRESS', 'OKAY', 'NOTHING', 'UHHH', 'BLANK', 'LEFT', 'FIRST', 'WHAT', 'NO', 'WAIT'),
  'YOU':       ('SURE', 'YOU ARE', 'YOUR', 'YOU\'RE', 'NEXT', 'UH HUH', 'UR', 'HOLD', 'WHAT?', 'YOU', 'UH UH', 'LIKE', 'DONE', 'U'),
  'YOU ARE':   ('YOUR', 'NEXT', 'LIKE', 'UH HUH', 'WHAT?', 'DONE', 'UH UH', 'HOLD', 'YOU', 'U', 'YOU\'RE', 'SURE', 'UR', 'YOU ARE'),
  'YOUR':      ('UH UH', 'YOU ARE', 'UH HUH', 'YOUR', 'NEXT', 'UR', 'SURE', 'U', 'YOU\'RE', 'YOU', 'WHAT?', 'HOLD', 'LIKE', 'DONE'),
  'YOU\'RE':   ('YOU', 'YOU\'RE', 'UR', 'NEXT', 'UH UH', 'YOU ARE', 'U', 'YOUR', 'WHAT?', 'UH HUH', 'SURE', 'DONE', 'LIKE', 'HOLD'),
  'UR':        ('DONE', 'U', 'UR', 'UH HUH', 'WHAT?', 'SURE', 'YOUR', 'HOLD', 'YOU\'RE', 'LIKE', 'NEXT', 'UH UH', 'YOU ARE', 'YOU'),
  "U":         ('UH HUH', 'SURE', 'NEXT', 'WHAT?', 'YOU\'RE', 'UR', 'UH UH', 'DONE', 'U', 'YOU', 'LIKE', 'HOLD', 'YOU' 'ARE', 'YOUR'),
  'UH HUH':    ('UH HUH', 'YOUR', 'YOU ARE', 'YOU', 'DONE', 'HOLD', 'UH UH', 'NEXT', 'SURE', 'LIKE', 'YOU\'RE', 'UR', 'U', 'WHAT?'),
  'UH UH':     ('UR', 'U', 'YOU ARE', 'YOU\'RE', 'NEXT', 'UH UH', 'DONE', 'YOU', 'UH HUH', 'LIKE', 'YOUR', 'SURE', 'HOLD', 'WHAT?'),
  'WHAT?':     ('YOU', 'HOLD', 'YOU\'RE', 'YOUR', 'U', 'DONE', 'UH UH', 'LIKE', 'YOU ARE', 'UH HUH', 'UR', 'NEXT', 'WHAT?', 'SURE'),
  'DONE':      ('SURE', 'UH HUH', 'NEXT', 'WHAT?', 'YOUR', 'UR', 'YOU\'RE', 'HOLD', 'LIKE', 'YOU', 'U', 'YOU ARE', 'UH UH', 'DONE'),
  'NEXT':      ('WHAT?', 'UH HUH', 'UH UH', 'YOUR', 'HOLD', 'SURE', 'NEXT', 'LIKE', 'DONE', 'YOU ARE', 'UR', 'YOU\'RE', 'U', 'YOU'),
  'HOLD':      ('YOU ARE', 'U', 'DONE', 'UH UH', 'YOU', 'UR', 'SURE', 'WHAT?', 'YOU\'RE', 'NEXT', 'HOLD', 'UH HUH', 'YOUR', 'LIKE'),
  'SURE':      ('YOU ARE', 'DONE', 'LIKE', 'YOU\'RE', 'YOU', 'HOLD', 'UH HUH', 'UR', 'SURE', 'U', 'WHAT?', 'NEXT', 'YOUR', 'UH UH'),
  'LIKE':      ('YOU\'RE', 'NEXT', 'U', 'UR', 'HOLD', 'DONE', 'UH UH', 'WHAT?', 'UH HUH', 'YOU', 'LIKE', 'SURE', 'YOU ARE')}

# global TABLE, T0x0, T0x1, T1x0, T1x1, T2x0, T2x1

TABLE = []
T0x0 = ''
T0x1 = ''
T1x0 = ''
T1x1 = ''
T2x0 = ''
T2x1 = ''

# table map
# _________________
# |     TITLE     |
# | T0x0  | T0x1  |
# | T1x0  | T1x1  |
# | T2x0  | T2x1  |

# functions
def newTable():
  return [
  ['', ''],
  ['', ''],
  ['', '']]
def mapTable(TABLE):
  return TABLE[0][0], TABLE[0][1], TABLE[1][0], TABLE[1][1], TABLE[2][0], TABLE[2][1]
def showTable(TABLE, TITLE):
  T0x0, T0x1, T1x0, T1x1, T2x0, T2x1 = mapTable(TABLE)
  print("""
  \t _______
  \t|{:_^7s}|
  \t|{:^3s}|{:^3s}|
  \t|{:^3s}|{:^3s}|
  \t|{:_^3s}|{:_^3s}|\n
  """.format(
  TITLE,
  T0x0, T0x1,
  T1x0, T1x1,
  T2x0, T2x1))
def getEyePos(TITLE):
  if TITLE == 'UR':
    return (0,0)
  elif TITLE in ('YES', 'NOTHING', 'LED', 'THEY ARE'):
    return (1,0)
  elif TITLE in ('', 'REED', 'LEED', 'THEY\'RE'):
    return (2,0)
  elif TITLE in ('FIRST', 'OKAY', 'C'):
    return (0,1)
  elif TITLE in ('BLANK', 'READ', 'RED', 'YOU', 'YOUR', 'YOU\'RE', 'THEIR'):
    return (1,1)
  elif TITLE in ('DISPLAY', 'SAYS', 'NO', 'LEAD', 'HOLD ON', 'YOU ARE', 'THERE', 'SEE', 'CEE'):
    return (2,1)
def getKeyWord(WORDS):
  try:
    keyWord = 'XYZ'
    while keyWord not in WORDS.keys():
      keyWord = input('KeyWord: ').upper()
    return keyWord
  except KeyboardInterrupt:
    print('[!]Interrupt by user\n')
    time.sleep(1)
    sys.exit()

# iface functions
def gui():
  print("GUI not avaible now,\ please wait for update")
  sys.exit()
def cli():
  try:
    TABLE = newTable()
    print("\n\n\t=== KTaNE Who's on first cheat v0.5 ===\n\t\t--- by Pixel ---\n\n")
    TITLE = 'XYZ'
    while TITLE not in TITLES:
      TITLE = input('Display title: ').upper()
    eyePos = getEyePos(TITLE)
    TABLE[eyePos[0]][eyePos[1]] = '<•>'
    if TITLE == 'THEY ARE': TITLE = 'THEYARE'
    time.sleep(1)
    showTable(TABLE, TITLE)
    keyWord = getKeyWord(WORDS)
    print()
    for word in WORDS[keyWord]:
      time.sleep(0.3)
      print('\t', word)
  except KeyboardInterrupt:
    print('[!]Interrupted by user\n')
    time.sleep(1)
    sys.exit()
  if input('\nRepeat?[Y/n] ').lower() in ('', ' ', 'y'):
    print('\n'*50)
    cli()

# main functions
def main(iface):
  if iface in ('-g', '--gui'):
    gui()
  else:
    cli()
if __name__ == '__main__':
  main(sys.argv[1:])
