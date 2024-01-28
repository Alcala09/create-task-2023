# Game of Life

# imports

import random
import time

# variable constants/initialization

grid_size = int(input("grid size: "))
life_grid = []
alive_cell = "  ⬛"
dead_cell = "  ⬜"
letter_size = 15
generation_number = 0

# functions


def change_color(color):
  ## CHANGING THE COLOR FOR THE CELL

  if color == "black":
    cell = "  ⬛"
    life_grid[i] = update_cell(i, grid_size, life_grid)

  elif color == "white":
    cell = "  ⬜"
  elif color == "red":
    cell = "  🟥"
  elif color == "orange":
    cell = "  🟧"
  elif color == "yellow":
    cell = "  🟨"
  elif color == "green":
    cell = "  🟩"
  elif color == "blue":
    cell = "  🟦"
  elif color == "purple":
    cell = "  🟪"
  elif color == "turtle":
    cell = "  🐢"

  return cell


def print_lifegrid():
  global generation_number
  row_number = 0  # printing grid

  for i in range(grid_size):

    for i in range(grid_size):
      if life_grid[i + (row_number * grid_size)] == 0:
        print(dead_cell, end="")
      elif life_grid[i + (row_number * grid_size)] == 1:
        print(alive_cell, end="")

    print("")
    row_number += 1

  # printing statistics

  generation_number += 1
  print("Generation: " + str(generation_number))
  print("Alive Cells: " + str(life_grid.count(1)))
  print("Dead Cells: " + str(life_grid.count(0)))
  print("Alive/Dead Ratio: " +
        str(round(life_grid.count(1) / life_grid.count(0), 2)))


def update_cell(index, grid_size, list):

  if list[index] != 9:
    neighboring_cells = [
      index - grid_size - 1, index - grid_size, index - grid_size + 1,
      index - 1, index + 1, index + grid_size - 1, index + grid_size,
      index + grid_size + 1
    ]

    neighbors = 0
    for i in neighboring_cells:  # iterating through each neighboring cell
      if list[i] == 1:
        neighbors += 1

    if ((list[index] == 1) and
        (neighbors == 2 or neighbors == 3)) or ((list[index] == 0) and
                                                (neighbors == 3)):
      return 1  # selects cell to be alive if met requirements

    else:
      return 0  # if cell can't meet requirements, return dead
  else:
    return 9  # returns wall if the selected index is a wall


## GENERATING THE LIST GRID FOR THE FIRST TIME

for i in range(grid_size):  #  9 <- wall, 0 <- dead cell, 1 <- alive cell
  life_grid.append(9)  # making top wall

for i in range(grid_size - 2):
  life_grid.append(9)  # left wall

  for i in range(grid_size - 2):  # making empty space
    life_grid.append(random.randint(0, 1))  # appends random cells

  life_grid.append(9)  # right wall

for i in range(grid_size):
  life_grid.append(9)  # making bottom wall

generation_time = float(input("Time Between Generations: "))  # refresh rate

alive_cell = change_color(
  input("Color for Alive Cell: "))  # color for alive cells
dead_cell = change_color(
  input("Color for Dead Cell: "))  # color for dead cells

while True:  # code running loop

  print_lifegrid()  # printing grid

  for i in range(grid_size**2):
    life_grid[i] = update_cell(i, life_grid, life_grid)  # check and update each cell

  time.sleep(generation_time)  # wait
