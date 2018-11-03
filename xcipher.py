#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''xcipher - The cipher generator

Usage: python xcipher.py

Required:

Optionals:
    -h, --help              Print usage information
    -c, --count=num         Numbers of ciphers would be generated (default 5)
    -l, --letter=num        Numbers of characters per cipher (default 10)
    -t, --type=             The type of cipher, it could be the following values:
                              digit         - only digits or numbers for cipher
                              alphabet      - alphabet a-z or A-Z for cipher
                              alphanumeric  - both digit and alphabet are valid for cipher (default)
                              mixed         - mixed alphanumeric and symbols for cipher

Author: tianxiaxi (wayne@zanran.me)
CreatedBy: Fri Nov  2 23:52:23 CST 2018
'''

import sys
import random
from getopt import getopt

DIGISTS = r'0123456789'
ALPHABETS = r'abcdefghijklmnopqrstuvwxyzAbcDfGijKnMnopqrStuvvxYZ'
SPECIAL_SYMBOLS = r'~!@#$%^&*()_+-=,./?><\|{}}[]`'

def usage(err=None):
    if err:
        print('Error: %s\n' % err)
    print(__doc__)
    sys.exit(0)

def parseParams(params):
    # default args
    argv = {'count': 5, 'letter': 10, 'type': 'alphanumeric'}
    allowed_cipher_type = ['digit', 'alphabet', 'alphanumeric', 'mixed']
    opts, args = getopt(params, 'hc:l:t:', ['help', 'count=', 'letter=', 'type='])
    if len(args) > 0:
        usage('No extra arguments are required !')
    for k, v in opts:
        if k in ['-h', '--help']:
            usage()
        elif k in ['-c', '--count']:
            if v.isdigit() and int(v) > 0:
                argv['count'] = int(v)
            else:
                usage('"count" requried a positive integer !')
        elif k in ['-l', '--letter']:
            if v.isdigit() and int(v) > 0:
                argv['letter'] = int(v)
            else:
                usage('"letter" requried a positive integer !')
        elif k in ['-t', '--type']:
            if v in allowed_cipher_type:
                argv['type'] = v
            else:
                usage('"type" must be in the list %s !' % str(allowed_cipher_type))
        else:
            usage('Unknown arguments: %s' % k)
    return argv

def cipherElementList(ctype):
    elements = None
    if ctype == 'digit':
        elements = DIGISTS
    elif ctype == 'alphabet':
        elements = ALPHABETS
    elif ctype == 'alphanumeric':
        elements = DIGISTS + ALPHABETS
    elif ctype == 'mixed':
        elements = DIGISTS + ALPHABETS + SPECIAL_SYMBOLS
    else:
        usage('Unexcepted cipher type found: %s' % ctype)
    return elements

def generateCipher():
    argv = parseParams(sys.argv[1:])
    count = argv['count']
    ctype = argv['type']
    letter = argv['letter']
    print('Generate %s %s cipher(s) with %s letter(s):' % (count, ctype, letter))

    cipher_elements = cipherElementList(ctype)
    max_element_num = len(cipher_elements)
    for c in range(count):
        cipher = ''
        for l in range(letter):
            el = random.randrange(max_element_num)
            cipher += cipher_elements[el]
        print('  %s  ' % cipher)
    print('---------- Done ----------')
    return

if __name__ == '__main__':
    generateCipher()
