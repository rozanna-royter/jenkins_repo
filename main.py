import os
import sys
from time import sleep

if __name__ == "__main__":
    num = int(os.environ['NUM'])
    for i in range(num):
        print(str(i) + ' ' + str(i*i))
        sleep(1)
