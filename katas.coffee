#Even or Odd
even_or_odd = (number) ->
  if number%2 then 'Odd' else 'Even'
even_or_odd = (number) ->
  ['Even', 'Odd'][number%2]
