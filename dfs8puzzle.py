goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def get_neighbours(state):
    neighbours = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbours.append(tuple(new_state))

    return neighbours


def dfs(start):
    stack = [(start, [])]
    visited = {start}

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path + [state]

        neighbours = get_neighbours(state)

        for neighbour in reversed(neighbours):
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append((neighbour, path + [state]))

    return None


start = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = dfs(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print_board(step)
else:
    print("No solution found")
