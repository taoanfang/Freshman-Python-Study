import random
from collections import deque
import time


# =========================
# Identity Module
# =========================
class Identity:
    def __init__(self, name, student_id, birthday, email, phone):
        self.name = name
        self.student_id = student_id
        self.birthday = birthday
        self.email = email
        self.phone = phone

    def generate_seed(self):
        seed = (sum(ord(c) for c in self.name)
            + int(self.student_id[-4:])
            + int(self.birthday.replace("-", ""))
        ) % 100000
        return seed

    def maze_size(self):
        rows = 15 + int(self.phone[:2]) % 8
        cols = 15 + int(self.phone[-2:]) % 8
        return rows, cols


# =========================
# Maze Generator
# =========================
class Maze:
    def __init__(self, rows, cols, seed):
        self.rows = rows
        self.cols = cols
        self.seed = seed
        random.seed(seed)

        self.grid = [['#'] * (cols * 2 + 1) for _ in range(rows * 2 + 1)]

        self.start = (1, 1)
        self.end = (rows * 2 - 1, cols * 2 - 1)

    def generate(self):
        visited = [[False] * self.cols for _ in range(self.rows)]

        def carve(r, c):
            visited[r][c] = True
            self.grid[r * 2 + 1][c * 2 + 1] = ' '

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and not visited[nr][nc]:
                    wall_r = r * 2 + 1 + dr
                    wall_c = c * 2 + 1 + dc
                    self.grid[wall_r][wall_c] = ' '
                    carve(nr, nc)

        carve(0, 0)

        self.grid[self.start[0]][self.start[1]] = 'S'
        self.grid[self.end[0]][self.end[1]] = 'E'

    def display(self):
        for row in self.grid:
            print("".join(row))


# =========================
# Solver Module
# =========================
class Solver:
    def __init__(self, maze):
        self.maze = maze
        self.grid = maze.grid
        self.start = maze.start
        self.end = maze.end

    def bfs(self):
        queue = deque([(self.start, [])])
        visited = set()
        steps = 0

        while queue:
            (r, c), path = queue.popleft()
            steps += 1

            if (r, c) == self.end:
                return path + [(r, c)], steps

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                if self.grid[nr][nc] != '#' and (nr, nc) not in visited:
                    queue.append(((nr, nc), path + [(r, c)]))

        return None, steps

    def dfs(self):
        stack = [(self.start, [])]
        visited = set()
        steps = 0

        while stack:
            (r, c), path = stack.pop()
            steps += 1

            if (r, c) == self.end:
                return path + [(r, c)], steps

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr, c + dc
                if self.grid[nr][nc] != '#' and (nr, nc) not in visited:
                    stack.append(((nr, nc), path + [(r, c)]))

        return None, steps


# =========================
# Visualization
# =========================
def mark_path(grid, path, marker):
    new_grid = [row[:] for row in grid]

    for r, c in path:
        if new_grid[r][c] == ' ':
            new_grid[r][c] = marker

    return new_grid


def display_grid(grid):
    for row in grid:
        print("".join(row))


# =========================
# Main
# =========================
def main():
    print("=== Personal Maze Generator ===")

    name = input("Name: ")
    student_id = input("Student ID: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    email = input("Email: ")
    phone = input("Phone: ")

    identity = Identity(name, student_id, birthday, email, phone)

    seed = identity.generate_seed()
    rows, cols = identity.maze_size()

    print(f"\nGenerated Seed: {seed}")
    print(f"Maze Size: {rows} x {cols}")

    maze = Maze(rows, cols, seed)
    maze.generate()

    print("\nGenerated Maze:")
    maze.display()

    solver = Solver(maze)

    print("\nRunning BFS...")
    start_time = time.time()
    bfs_path, bfs_steps = solver.bfs()
    bfs_time = time.time() - start_time

    print("Running DFS...")
    start_time = time.time()
    dfs_path, dfs_steps = solver.dfs()
    dfs_time = time.time() - start_time

    print("\n=== Performance Comparison ===")
    print(f"BFS Steps: {bfs_steps}, Time: {bfs_time:.6f}s")
    print(f"DFS Steps: {dfs_steps}, Time: {dfs_time:.6f}s")

    marker = name[0].upper()

    print("\nBFS Solution:")
    display_grid(mark_path(maze.grid, bfs_path, marker))


if __name__ == "__main__":
    main()