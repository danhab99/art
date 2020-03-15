import sys

from diamond import diamond
from circle import circle

if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(description='Draws art')
  parser.add_argument('program', help='Choose the program', choices=['circle', 'diamond'])
  parser.add_argument('size', help='The size of the art', default=17, type=int)
  parser.add_argument('-o', '--out', help='Output to a file', type=argparse.FileType('w+'), default=sys.stdout)
  parser.add_argument('-f', '--filled', help='Character to use to fill a point', default='X')
  parser.add_argument('-e', '--empty', help='Character to use to fill empty points', default=' ')
  parser.add_argument('-w', '--width', help='Number of -e characters to put between points', default=1, type=int)
  parser.add_argument('-l', '--line-height', help='Number of newlines between each line', default=1, type=int)

  args = parser.parse_args()

  end = args.empty * args.width

  if (args.program == 'circle'):
    d = circle(args.size, args.filled, args.empty)

  if (args.program == 'diamond'):
    d = diamond(args.size, args.filled, args.empty)

  def p(c):
    print(c, end='', file=args.out, flush=True)

  for y in d:
    for x in y:
      p(x + end)
    p('\n' * args.line_height)