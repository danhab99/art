import sys
import argparse

def newBuff(leg, F):
  return [[F for i in range(leg)] for j in range(leg)]

def printBuff(buff):
  for y in buff:
    for x in y:
      print(x, end=' ')
    print('')

def diamond(leg, T, F=' '):
  buff = newBuff(leg, F)

  def put(x, y, i):
    buff[y][x] = i
  
  midp = int(leg / 2)
  o = [i * (1 if i % 2 else -1) for i in range(leg * 2)]

  def R(y):
    l = [midp + i for i in o[:y]]
    r = [midp - i for i in o[:y]]
    return list(set(l + r))

  for y in range(midp):
    r = R(y)
    for x in r:
      put(x, y, T)

  for yp, yn in zip(range(midp, leg), range(midp, 0, -1)):
    r = R(yn)
    for x in r:
      put(x, yp, T)

  return buff

def circle(leg, T, F=' '):
  buff = newBuff(leg, F)
  h = int(leg / 2)
  r2 = h ** 2
  for y in range(-h, h):
    for x in range(-h, h):
      c2 = (x ** 2) + (y ** 2)
      buff[x + h][y + h] = T if c2 < r2 else F
      # printBuff(buff)
  return buff

if __name__ == '__main__':

  parser = argparse

  s = int(sys.argv[1]) | 1
  # d = diamond(s, '@', '-')
  d = circle(s, 'O', ' ')
  printBuff(d)