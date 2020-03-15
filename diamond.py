from newbuff import newBuff

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
