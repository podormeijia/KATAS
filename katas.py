#String ends with
def solution(string, ending):
    return ending in string[-len(ending):]

#Breaking chocolate problem
def breakChocolate(n, m):
    return (n-1) + n*(m-1) if n and m else 0
def breakChocolate(n, m):
    return max(n*m-1,0)

#Jaden Casing Strings
def toJadenCase(string):
    return ' '.join([word.capitalize() for word in string.split(None)])
import string
def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)

#boolean value
def bool_to_word(bool):
    return 'Yes' if bool else 'No'
bool_to_word = lambda x: ['No', 'Yes'][x] #Boolean in Python is a subtype of Integer.

#function return function
def always(n=0):
    def three():
        return n
    return three
def always(n=0):
    return lambda: n

#shorter concat [reverse longer]
def shorter_reverse_longer(a,b):
	if (len(a) >= len(b)):
		a,b = b,a
	return a+b[::-1]+a
def shorter_reverse_longer(a,b):
  return a+b[::-1]+a if len(b)>len(a) else b+a[::-1]+b

#Calculate the function f(x) for a simple linear sequence
def get_function(sequence):
  m = sequence[0]
  n = sequence[1] - m
  if [n*x+m for x in range(5)] != sequence:
      return 'Non-linear sequence'
  return 'f(x) = {}'.format(format_function(n, m))
def format_function(n, m):
  if not n:
      return m
  n_string = '{}{}x'.format('-' if n < 0 else '', abs(n) if abs(n) != 1 else '')
  m_string = ' {} {}'.format('+' if m > 0 else '-', abs(m)) if m else ''
  return ''.join([n_string, m_string])

def get_function(sequence):
  first, dist = sequence[0], sequence[1] - sequence[0]
  valid = all(x == dist * i + first for i, x in enumerate(sequence))
  dist = 'x' if dist == 1 else '-x' if dist == -1 else '' if dist == 0 else str(dist) + 'x'
  first = str(first) if len(dist) == 0 else '' if first == 0 else ' - ' + str(first * -1) if first < 0 else ' + ' + str(first)
  return 'f(x) = ' + dist + first if valid else 'Non-linear sequence'

#Calculate the function f(x) for a simple linear sequence
def get_function(sequence):
    m = sequence[0]
    n = sequence[1] - m
    if [n*x + m for x in range(5)] != sequence:
        return 'Non-linear sequence'
    return lambda x : n*x + m

def get_function(seq):
    f = lambda x: seq[0] + (seq[1] - seq[0]) * x
    return 'Non-linear sequence' if f(2) != seq[2] else f

#Remove anchor from URL
def remove_url_anchor(url):
  return url.split('#')[0]

remove_url_anchor = lambda s: __import__('re').sub('(.*)\\#.*', '\\1', s)

#Factorial Factory
def factorial(n):
    if n < 0:
        return None
    result = 1
    for x in range(1, n+1):
        result *= x
    return result

factorial = lambda n: reduce(lambda a, b: a * b, range(1, n + 1), 1) if n >= 0 else None

#Tic-Tac-Toe Checker
def isSolved(board):
  for i in range(0,3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
      return board[i][0]
    elif board[0][i] == board[1][i] == board[2][i] != 0:
      return board[0][i]

  if board[0][0] == board[1][1] == board[2][2] != 0:
    return board[0][0]
  elif board[0][2] == board[1][1] == board[2][0] != 0:
    return board[0][0]

  elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
    return 0
  else:
    return -1

def some(f, xs):
  return reduce(lambda x,y: x or f(y), xs, False)

def every(f, xs):
  return reduce(lambda x,y: x and f(y), xs, True)

def wins(player, line):
  return every(lambda x: x == player, line)
def isSolved(board):
  rows = board
  cols = zip(*board)
  diag = [board[i][i] for i in range(3)]
  anti = [board[i][2-i] for i in range(3)]

  lines = rows + cols + [diag, anti]

  for i in (1,2):
    if some(lambda line: wins(i, line), lines):
      return i

  if some(lambda line: some(lambda y: y == 0, line), lines):
    return -1
  else:
    return 0

#The Descent
while True:
    max_height = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > max_height:
            imax, max_height = i, mountain_h
    print(imax)

while True:
    print(max([(int(input()),x) for x in range(8)])[1])
