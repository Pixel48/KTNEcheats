#
# -*- coding: utf-8 -*-
# KTNEpassworld.py

import sys

# globals
WORDS = (
  'about', 'after', 'again', 'below', 'could',
  'every', 'first', 'found', 'great', 'house',
  'large', 'learn', 'never', 'other', 'place',
  'plant', 'point', 'right', 'small', 'sound',
  'spell', 'still', 'study', 'their', 'there',
  'these', 'thing', 'think', 'three', 'water',
  'where', 'which', 'world', 'would', 'write')
al = ''
bl = ''
cl = ''
dl = ''
el = ''

# functions
def ask():
  if 'n' in input('Repeat? [Y/n] ').lower():
    sys.exit()
  else: cli()

# iace functions
def gui():
  print("GUI not avaible now,\ please wait for update")
  sys.exit()
def cli():
  print("\n\t=== KTaNE password cracker v1.4 ===\n\t\t--- by Pixel ---\n\n")
  did = False
  al = input('Pierwsze litery: '))
  bl = input('Drugie litery:   '))
  cl = input('Trzecie litery:  '))
  dl = input('Czwarte litery:  '))
  el = input('Piąte litery:    '))

  for a in al:
    for b in bl:
      for c in cl:
        for d in dl:
          for e in el:
            word = str(a + b + c + d + e)
            if word in WORDS:
              did = True
              print("\n\n\t\t", end='')
              print(word.upper())
              print("\n")
              ask()
  if not did:
    print("\n\n\t\tBad characters!\n")
    ask()

# main functions
def main(gui):
  if gui:
    gui()
  else:
    cli()
if __name__=='__main__':
    main(sys.argv[1])
