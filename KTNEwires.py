#
# -*- coding: utf-8 -*-
# KTNEwires.py
#   by Pixel

import sys, time

# globals
WIRES = 0
SERIAL = ''

# main functions
def displayLoadingBar():
  for i in range(51):
    print('Loading... [{:<50s}]{:}\r'.format('='*i, '{}%'.format(i*2)), end='')
    time.sleep(.05)
    print(' '*80, '\r', end='')
def askReload():
  x = input('Reload?[Y/n] ')
  if 'n' in x.lower():
    sys.exit()
  else:
    print('\n'*50)
    cli()
def getSerial():
  x = None
  while type(x) != type(str()) or len(x) != 6:
    x = str(input('Bomb serial no.: ').upper())
  return x
def getWires():
  x = 0
  while type(x) != type(int()) or x > 6 or x < 3:
    try:
      x = int(input('How many wires? '))
    except KeyboardInterrupt:
      print('[!]Interrupted by user')
      askReload()
    except:
      x = 0
  return x
def getBool(question, emptyYes = True):
  try:
    if emptyYes:
      if input(str(question)).lower() in ('n', 'no'):
        return False
      else: return True
    else:
      if input(str(question)).lower() in ('y', 'yes'):
        return True
      else: return False
  except KeyboardInterrupt:
    print('[!]Interrupted by user')
    askReload()

# iface functions
def gui():
  print('GUI not avaible now,\ please wait for update')
  sys.exit()
def cli():
  try:
    print('\n\n\t=== KTaNE "Wires" cheat v0.5 ===\n\t\t--- by Pixel ---\n\n')
    WIRES = getWires()
    SERIAL = getSerial()
    print()
    displayLoadingBar()
    for i in range(WIRES):
      print('Wire ', i+1, ':', sep='')
      if WIRES == 3:
        if not getBool('Are there any red wires? [y/N] ', emptyYes = False):
          print('\n\t\tCut the second wire.')
        elif getBool('Is the last wire white? [y/N] ', emptyYes = False):
          print('\n\t\tCut the last wire.')
        elif getBool('Is there more then one blue wire? [y/N] ', emptyYes = False):
          print('\n\t\tCut the last blue wire.')
        else: print('\n\t\tCut the last wire.')
      elif WIRES == 4:
        if int(SERIAL[-1:]) % 2 != 0:
          if getBool('Is there more then one red wire? [y/N] ', emptyYes = False):
            print('\n\t\tCut the last red wire.')
        elif getBool('Is the last wire yellow? [y/N] ', emptyYes = False) and getBool('Are there any red wires? [y/N] ', emptyYes = False):
          print('\n\t\tCut the first wire.')
        elif getBool('Is there exactly one blue wire? [y/N] ', emptyYes = False):
          print('\n\t\tCut the first wire.')
        elif getBool('Is it more then one yellow wire [y/N] ', emptyYes = False):
          print('\n\t\tCut the last wire.')
        else: print('\n\t\tCut the second wire.')
      elif WIRES == 5:
        if int(SERIAL[-1:]) % 2 != 0:
          if getBool('Is the last wire black? [y/N] ', emptyYes = False):
            print('\n\t\tCut the fourth wire.')
        elif getBool('Is there exactly one red wire? [y/N] ', emptyYes = False) and getBool('Is there more then one yellow wire? [y/N] ', emptyYes = False):
          print('\n\t\tCut the first wire.')
        elif not getBool('Is there any black wires? [y/N] ', emptyYes = False):
          print('\n\t\tCut the second wire.')
        else: print('\n\t\tCut the first wire.')
      elif WIRES == 6:
        if int(SERIAL[-1:]) % 2 != 0:
          if not getBool('Is there any yellow wires? [y/N] ', emptyYes = False):
            print('\n\t\tCut the third wire.')
        elif getBool('Is there exactly one yellow wire? [y/N] ', emptyYes = False) and getBool('Is there more then one white wire? [y/N] ', emptyYes = False):
          print('\n\t\tCut the fourth wire.')
        elif not getBool('Is there any red wires? [y/N] ', emptyYes = False):
          print('\n\t\tCut the last wire.')
        else: print('\n\t\tCut the fourth wire.')
      else:
        print('[!]Unknown error!')
        askReload()
    print()
    askReload()
  except KeyboardInterrupt:
    print('[!]Interrupted by user\n')
    askReload()

# launcher functions
def main(iface):
  if iface in ('-g', '--gui'):
    gui()
  else: cli()
if __name__ == '__main__':
  main(sys.argv[1:])
