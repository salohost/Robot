class Field
  constructor: (width, height) ->
    for i in [0..width]
      for j in [0..height]
        @map[i][j]


reverseSide = (side) ->
  return switch side
    when 'n' then 's'
    when 's' then 'n'
    when 'w' then 'e'
    when 'e' then 'w'

borderSideString = (side) ->
  return switch side
    when 'n' then 'top_bord'
    when 's' then 'bottom_bord'
    when 'w' then 'left_bord'
    when 'e' then 'right_bord'

addBord = (field, i, j, side) ->
  switch side
    when 'n' then if i isnt 0
      addBorder field.map[i-1][j], 'bottom_bord'
    when 's' then if i isnt field.map.length
      addBorder field.map[i+1][j], 'top_bord'
    when 'w' then if j isnt 0
      addBorder field.map[i][j-1], 'left_bord'
    when 'e' then if j isnt field.map[i].lenght
      addBorder field.map[i][j+1], 'right_bord'

addBorder = (el, borderSide) ->
  el.className += ' ' + borderSide
