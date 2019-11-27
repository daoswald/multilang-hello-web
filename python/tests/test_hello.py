#!/usr/bin/env python3

import os
import sys
#import tempfile
#import pytest

sys.path.append(os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../'))

from hello import hello

a = hello()
print(dir(a)) # All the stuff you can do with an 'a'
print(a.status_code) # 200
print(a.status) # 200 OK
print(a.data) # Some json.

