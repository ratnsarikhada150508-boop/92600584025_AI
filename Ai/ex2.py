from collections import deque

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

    # Fill Jug A
    if a < CAP_A:
        neighbors.append(((CAP_A, b), "Fill Jug A"))

    # Fill Jug B
    if b < CAP_B:
        neighbors.append(((a, CAP_B), "Fill Jug B"))

    # Empty Jug A
    if a > 0:
        neighbors.append(((0, b), "Empty Jug A"))

    # Empty Jug B
    if b > 0:
        neighbors.append(((a, 0), "Empty Jug B"))

    # Pour A -> B
    amount = min(a, CAP_B - b)
    if amount > 0:
        neighbors.append(
            ((a - amount, b + amount), "Pour Jug A -> Jug B")
        )

    # Pour B -> A
    amount = min(b, CAP_A - a)
    if amount > 0:
        neighbors.append(
            ((a + amount, b - amount), "Pour Jug B -> Jug A")
        )

    return neighbors


def bfs():
    start = (0, 0)

    queue = deque()
    queue.append(start)

    visited = {start}

    # Store parent and action for reconstructing the solution
    parent = {start: None}
    action = {start: None}

    while queue:
        state = queue.popleft()

        # Check whether either jug contains the goal
        if state[0] == GOAL or state[1] == GOAL:

            # Reconstruct path
            path = []
            current = state

            while current is not None:
                path.append((current, action[current]))
                current = parent[current]

            path.reverse()
            return path

        # Explore neighbors
        for next_state, move in get_neighbors(state):

            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)

                parent[next_state] = state
                action[next_state] = move

    return None


# Run BFS
solution = bfs()

if solution:
    print("Solution found!\n")

    for state, move in solution:
        if move:
            print(move)
        print_state(state)
else:
    print("No solution found.")
