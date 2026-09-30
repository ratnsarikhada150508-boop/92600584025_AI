CAP_A = 4
CAP_B = 3

GOAL = 2


def print_state(state):
    print("Jug A:", state[0], "Liters")
    print("Jug B:", state[1], "Liters")
    print()


def get_neighbors(state):
    neighbors = []
    a, b = state

    if a < CAP_A:
        neighbors.append(((CAP_A, b), "Fill Jug A"))

    if b < CAP_B:
        neighbors.append(((a, CAP_B), "Fill Jug B"))

    if a > 0:
        neighbors.append(((0, b), "Empty Jug A"))

    if b > 0:
        neighbors.append(((a, 0), "Empty Jug B"))

    amount = min(a, CAP_B - b)
    if amount > 0:
        neighbors.append(
            ((a - amount, b + amount), "Pour Jug A -> Jug B")
        )

    amount = min(b, CAP_A - a)
    if amount > 0:
        neighbors.append(
            ((a + amount, b - amount), "Pour Jug B -> Jug A")
        )

    return neighbors


# BFS
def bfs(start):
    queue = [(start, [])]
    visited = set()

    while queue:
        state, path = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        if state[0] == GOAL or state[1] == GOAL:
            return path + [(state, "Goal Reached")]

        for neighbor, action in get_neighbors(state):
            if neighbor not in visited:
                queue.append(
                    (neighbor, path + [(neighbor, action)])
                )

    return None


start = (0, 0)
solution = bfs(start)

if solution:
    print("Solution Found In", len(solution) - 1, "Moves:\n")

    print("Initial State:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("No Solution Found")
