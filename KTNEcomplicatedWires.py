#
# -*- coding: utf-8 -*-
# KTNEcomplicatedWires.py
#   by Pixel

import sys, time

# globals
WIRES = 0
SERIAL_EVEN = False
PARALLEL_PORT = False
BATERRIES = False

# main functions
def getWires():
  x = None
  while type(x) != type(int()) or x > 6 or x < 1:
    try:
      x = int(input('How many wires? '))
    except KeyboardInterrupt:
      print('[!]Interrupted by user')
      sys.exit()
    except:
      x = 0
  return x
def getSerial():
  x = None
  while type(x) != type(str()) or len(x) != 6:
    x = input('Bomb serial no.: ').upper()
  return x
def isEven(char):
  char = int(char)
  if char % 2 == 0:
    return True
  else:
    return False
def isParallelPort():
  x = input('Have bomb got a parallel port?[y/N] ')
  if x.lower() in ('y', 'yes'):
    return True
  else:
    return False
def isMultiBaterries():
  x = input('Is more then one baterry on bomb?[Y/n] ')
  if x.lower() in ('n', 'no'):
    return False
  else:
    return True
def getWireInfo():
  red = input('Is red?[y/N] ')
  if 'y' in red.lower():
    red = True
  else:
    red = False

  blue = input('Is blue[y/N] ')
  if 'y' in blue.lower():
    blue = True
  else:
    blue = False

  star = input('Have got any star?[y/N]' )
  if 'y' in star.lower():
    star = True
  else:
    star = False

  led = input('Is led on?[y/N] ')
  if 'y' in led.lower():
    led = True
  else:
    led = False

  return red, blue, star, led # output: red, blue, star, led
def doCut(red, blue, star, led):
  if red == blue == star == led == False:
    return True # 0000/0
  elif red == blue == star == False and led == True: # 0001/1
    return False
  elif red == blue == led == False and star == True: # 0010/2
    return True
  elif red == blue == False and star == led == True: # 0011/3
    if BATERRIES:
      return True
    else:
      return False
  elif red == star == led == False and blue == True: # 0100/4
    if SERIAL_EVEN:
      return True
    else:
      return False
  elif red == star == False and blue == led == True: # 0101/5
    return False
  elif red == led == False and blue == star == True: # 0110/6
    return False
  elif red == False and blue == star == led == True: # 0111/7
    if PARALLEL_PORT:
      return True
    else:
      return False
  elif blue == star == led == False and red == True: # 1000/8
    if SERIAL_EVEN:
      return True
    else:
      return False
  elif blue == star == False and red == led == True: # 1001/9
    if BATERRIES:
      return True
    else:
      return False
  elif blue == led == False and red == star == True: # 1010/10
    return True
  elif blue == False and red == star == led == True: # 1011/11
    if BATERRIES:
      return True
    else:
      return False
  elif red == blue == False and star == led == True: # 1100/12
    if BATERRIES:
      return True
    else:
      return False
  elif star == False and red == blue == led == True: # 1101/13
    if SERIAL_EVEN:
      return True
    else:
      return False
  elif led == False and red == blue == star == True: # 1110/14
    if PARALLEL_PORT:
      return True
    else:
      return False
  elif red == blue == star == led == True: # 111/15
    return False
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
    print('\n\n\t=== KTaNE "Who\'s on first" assistant v0.5 ===\n\t\t--- by Pixel ---\n\n')
    WIRES = getWires()
    SERIAL = getSerial()
    SERIAL_EVEN = isEven(SERIAL[-1:])
    PARALLEL_PORT = isParallelPort()
    BATERRIES = isMultiBaterries()
    print()
    displayLoadingBar()
    for i in range(WIRES):
      i += 1
      print('{}. wire info:'.format(i))
      red, blue, star, led = getWireInfo()
      cut = doCut(red, blue, star, led)
      if cut:
        print('\n\t\tCut.\n')
      else:
        print('\n\t\tDON\'T CUT!\n')
      askReload()
  except KeyboardInterrupt:
    print('[!]Interrupted by user\n')
    askReload()

# launcher functions
def main(iface):
  if iface in ('-g', '--gui'):
    gui()
  else:
    cli()
if __name__ == '__main__':
  main(sys.argv[1:])
