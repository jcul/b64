#!/usr/bin/python3

import sys
import argparse
import base64

parser = argparse.ArgumentParser(description='Encode and Decode base64.')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encode', action='store_const', const=base64.standard_b64encode, dest='func')
group.add_argument('-d', '--decode', action='store_const', const=base64.standard_b64decode, dest='func')

parser.add_argument('-i', '--infile', dest='infile', metavar='INFILE', help='Defaults to stdin')
parser.add_argument('-o', '--outfile', dest='outfile', metavar='OUTFILE', help='Defaults to stdout')
parser.add_argument('args', nargs='*')

opts = parser.parse_args()

if (opts.infile == None):
    instr = ' '.join(opts.args).encode()
else:
    with open(opts.infile, 'rb') as ifh:
        instr = ifh.read()

outstr = opts.func(instr)

if (opts.outfile == None):
    print(outstr) 
else:
    with open(opts.outfile, 'wb') as ofh:
        ofh.write(outstr) 

