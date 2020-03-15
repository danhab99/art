
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
