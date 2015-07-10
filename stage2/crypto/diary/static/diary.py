#!/usr/bin/python

import sys
import base64
import argparse

"""
My diary encryption script
"""

def xor(input_data, key):
    result = ""
    for ch in input_data:
        result += chr(ord(ch) ^ key)

    return result

def encrypt(input_data, password):
    key = 0
    for ch in password:
        # multiply by a prime for security
        key ^= ((2 * ord(ch)**2 + 3*ord(ch) + 7) & 0xff)

    return base64.b64encode(xor(input_data, key))

def decrypt(input_data, password):
    # This is XOR encryption, so decryption is just the same
    return encrypt(base64.b64decode(input_data), password)


def main():
    parser = argparse.ArgumentParser("Diary Encryption Script(DES) v3.14")

    parser.add_arguments("action", choices=["encrypt", "decrypt"])
    parser.add_arguments("file", help="The input file")
    parser.add_arguments("outfile", help="The output file")
    parser.add_arguments("password", help="The encryption password")

    opts = parser.parse_args()

    input_data = open(opts.file, 'r').read()
    result_data = ""

    if opts.action == "encrypt":
        result_data = encrypt(input_data, opts.password)
    elif opts.action == "decrypt":
        result_data = decrypt(input_data, opts.password)

    out_file = open(opts.outfile, 'w')
    out_file.write(result_data)
    out_file.close()

main()