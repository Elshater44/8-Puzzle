# 8-Puzzle Solver using A* Algorithm

## Overview

This Python project implements an 8-puzzle solver using the A* search algorithm. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one blank space. The objective is to rearrange the tiles from a given arbitrary starting arrangement to a target configuration by sliding them one at a time into the blank space.

## Features

- **A* Algorithm**: Utilizes the A* search algorithm to efficiently find the optimal solution to the 8-puzzle problem.
- **Heuristic Function**: Implements the Manhattan distance heuristic to estimate the cost of reaching the goal state from any given state.
- **Solvable Check**: Determines whether a given initial state of the puzzle is solvable or not based on the number of inversions.
- **Solution Visualization**: Displays the sequence of moves required to solve the puzzle from the initial state to the goal state.
- **Input**: Allows users to input the initial state of the puzzle and the goal state manually.

## Usage

1. **Run the Program**: Execute the Python script `puzzle.py` using any Python interpreter.

    ```bash
    python puzzle.py
    ```

2. **Input**: Follow the prompts to enter the initial state of the puzzle and the goal state. The input should be provided as a 3x3 grid with numbers representing the tiles, where 0 represents the blank space.

3. **View Solution**: Once the input is provided, the program will display the sequence of moves required to solve the puzzle, as well as the final arrangement of the tiles.
