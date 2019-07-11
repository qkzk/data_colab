#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Équipe pédagogique DIU-EIL Lille'
__date__ = 'juin 2019'
__doc__ = """
   Encoding and decoding utility for base64 files.
   Requires the codage64 module.

   :author: {:s}
   :date: {:s}
""".format(__author__, __date__)

import sys
import codage64


def usage():
    '''
    prints how to use the program
    '''
    print("Usage : {} [-e|-d] <fichier source> [fichier cible]\n".format(sys.argv[0]),
          file=sys.stderr)
    print("\t -e pour encoder\n\t -d pour decoder\n", file=sys.stderr)
    exit(1)

def main():
    '''
    main procedure
    '''
    if len(sys.argv) not in (3, 4):
        usage()
    else:
        option = sys.argv[1]
        source_file = sys.argv[2]
        if option == "-e":
            codage64.base64_encode(source_file)
        elif option == "-d":
            target_file = sys.argv[3]
            print(codage64.base64_decode(source_file, target_file))
        else:
            usage()
    exit(0)

if __name__ == '__main__':
    main()
