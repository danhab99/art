import sys

# def printBuff(buff, end, gap, lh, F, out=sys.stdout):


def newBuff(leg, F):
  return [[F for i in range(leg)] for j in range(leg)]