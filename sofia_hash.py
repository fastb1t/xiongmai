#!/usr/bin/python3

import hashlib
import sys

def sofia_hash(msg):
    h = ""
    m = hashlib.md5()
    m.update(msg.encode('utf-8'))
    msg_md5 = m.digest()
    for i in range(8):
        n = (msg_md5[2*i] + msg_md5[2*i+1]) % 0x3e
        if n > 9:
            if n > 35:
                n += 61
            else:
                n += 55
        else:
            n += 0x30
        h += chr(n)
    return h


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("How to use: python3 sofia_hash.py <hash>\n")
        sys.exit(1)

    print(sofia_hash(sys.argv[1]))

