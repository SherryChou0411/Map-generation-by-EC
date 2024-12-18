# Map generation using evolutionary strategy
## Objective
Design the map to have a valley with a river flowing though it.
## Method
- Tile type
  EMPTY = '0'
  WALL = '1'
  RIVER = '4'
  TREE = '3'
- Fitness function
  Fitness = 5 * number of river tiles + 3 * number of empty tiles + 2 * number of wall tiles
