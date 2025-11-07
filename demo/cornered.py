import sys.path as pth
pth.append('../AsciiLIB/')

import AsciiLIB as asl

game = asl.Game(8, 8, CharLib["MAIN"]["BLOCK"], "Cornered")