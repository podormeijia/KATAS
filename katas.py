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
