# Personal Maze Generator

A Python project that generates and solves mazes based on user identity information.

## Overview

This project takes a user's personal information as input, generates a deterministic seed, and then creates a random-looking maze with a fixed structure.  
It also solves the maze using both BFS and DFS, compares their performance, and visualizes the solution path.

## Features

- Generate a maze from user input
- Create a deterministic random seed
- Adjust maze size based on phone number
- Solve the maze using:
  - BFS (Breadth-First Search)
  - DFS (Depth-First Search)
- Compare the number of steps and running time
- Display the maze and solution path in the terminal

## How It Works

### 1. Identity Module
The `Identity` class reads user information such as:

- Name
- Student ID
- Birthday
- Email
- Phone number

It then generates:

- A numeric seed
- Maze dimensions

### 2. Maze Generator
The `Maze` class uses depth-first carving to generate the maze.

- `#` represents walls
- `' '` represents open paths
- `S` marks the start point
- `E` marks the end point

### 3. Solver Module
The `Solver` class provides two search methods:

- **BFS**: finds the shortest path
- **DFS**: explores deeper paths first

The project also records:

- Number of steps
- Execution time

### 4. Visualization
The solution path is marked with the first letter of the user's name.

## Tech Stack

- Python 3
- `random`
- `collections.deque`
- `time`

## File Structure

```text
py-study/
└── personal-maze-generator/
    └── main.py
