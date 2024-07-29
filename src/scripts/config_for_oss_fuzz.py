#!/usr/bin/env python3

"""
(C) 2024 Jack Lloyd

Botan is released under the Simplified BSD License (see license.txt)

Setup script for OSS-Fuzz
"""

import sys
import subprocess

if len(sys.argv) != 3:
    print("Expected args: %s <cxx> <cxxflags>" % (sys.argv[0]))
    sys.exit(1)

cxx = sys.argv[1]
cxxflags = sys.argv[2]

args = [
    "--cc-bin=%s" % (cxx),
    "--cc-abi-flags=%s" % (cxxflags),
    "--without-documentation",
    "--disable-shared",
    "--disable-modules=locking_allocator",
    "--unsafe-fuzzer-mode",
    "--build-fuzzers=libfuzzer",
    "--build-targets=static",
    "--without-os-features=getrandom,getentropy",
    "--with-fuzzer-lib=FuzzingEngine",
]

if cxxflags.find("-fsanitize=memory") > 0:
    args.append('--disable-asm')

subprocess.run(["configure.py"] + args)
