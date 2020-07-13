import os
import sys

epoch=10

for i in range(epoch-1):
    os.system('call ./scripts/train.bat')
    os.system('timeout /T 10 /NOBREAK')
