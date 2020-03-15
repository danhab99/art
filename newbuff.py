def printBuff(buff):
  for y in buff:
    for x in y:
      print(x, end=' ')
    print('')

def newBuff(leg, F):
  return [[F for i in range(leg)] for j in range(leg)]