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
