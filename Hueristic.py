goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


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


def heuristic_search(start):
    current = start
    path = [current]
    visited = set()

    while current != goal:

        visited.add(current)

        neighbours = get_neighbours(current)

        new_neighbours = []

        for n in neighbours:
            if n not in visited:
                new_neighbours.append(n)

        if not new_neighbours:
            return None

        current = min(new_neighbours, key=heuristic)

        path.append(current)

    return path


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)


solution = heuristic_search(start)


if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print_board(step)
else:
    print("No Solution found")
