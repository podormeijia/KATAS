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

