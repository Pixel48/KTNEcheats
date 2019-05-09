#
# -*- coding: utf-8 -*-
# KTNEbutton.py
#   by Pixel

import sys

# globals
SERIAL = ''
BATERRIES = False

# functions
def isMultiBaterries():
  x = input('Is more then one baterry on bomb?[Y/n] ')
  if x.lower() in ('n', 'no'):
    return False
  else:
    return True
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

# iface functions
def gui():
  print('GUI not avaible now,\ please wait for update')
  sys.exit()
def cli():
  try:
        print('\n\n\t=== KTaNE Button assistant v0.5 ===\n\t\t--- by Pixel ---\n\n')
  except KeyboardInterrupt as e:
    print('[!]Interrupted by user\n')
    askReload()

# launcher
def main(iface):
  if iface in ('-g', '--gui'):
    gui()
  else:
    cli()
if __name__ == '__main__':
  main(sys.argv[1:])
