import sys
import pandas as pd
import numpy as np




def main(args):
    print args
    if len(args) < 1: return
    file = pd.read_excel(args[0], "Sheet1")
    print file

if __name__ == '__main__':
    main(sys.argv[1:])