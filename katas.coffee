# http://www.oschina.net/news/72854/10-coffeescript-oneline-code

#Even or Odd
even_or_odd = (number) ->
  if number%2 then 'Odd' else 'Even'
even_or_odd = (number) ->
  ['Even', 'Odd'][number%2]


#Number of People in the Bus
number = (peopleListInOut) ->
  total = 0
  for people in peopleListInOut
      total += people[0]
      total -= people[1]
      if 0 > total
        return "didn't work for #{peopleListInOut}"
  total

number = (peopleListInOut) ->
  peopleListInOut.map(([a,b]) -> a - b).reduce((x,y) -> x + y)

#Sum without highest and lowest number
sumArray = (arr) ->
  arr.sort((a, b) -> x < y)[1..-2].reduce((x, y) -> x + y)

sumArray = (arr) ->
  arr.sort((a, b) -> a < b)[1..-2].reduce((x, y) -> x + y)

#Sum without highest and lowest number
sumArray = (arr) ->
  if arr and arr.length > 2 then arr.sort((a, b) -> a - b)[1..-2].reduce((x, y) -> x + y) else 0

#Complementary DNA
DNAStrand = (dna) ->
  dna.split('')
     .map((x) ->
        switch x
          when 'A' then 'T'
          when 'T' then 'A'
          when 'G' then 'C'
          when 'C' then 'G'
     ).join('')

syms = {G:'C',C:'G',T:'A',A:'T'}
DNAStrand = (dna) -> (syms[s] for s in dna).join('')


#Count the Digit
nbDig = (n, d) ->
  [0..n].map((a) -> a ** 2).join('').split(d).length - 1


#Mumbling
accum = (s) ->
  (ss.toUpperCase() + ss.toLowerCase().repeat(i) for ss, i in s).join('-')
accum = (s) ->
  s.split('').map((letter, time) ->
    letter.toUpperCase() + [0...time].map(() ->
      letter.toLowerCase()).join('')).join('-')
