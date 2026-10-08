CAP_A = 4
CAP_B = 3

Goal = 2

def print_state(state):
    print("Jug A:",state[0],"Litres")
    print("Jug B:",state[1],"Litres")
    print()

def get_neighbours(state):
    neighbours = []
    a,b = state

    if a < CAP_A:
        neighbours.append(((CAP_A,b),"Fill Jug A"))

    if b <CAP_B:
        neighbours.append(((a,CAP_A),"Fill Jug B"))

    if a > 0:
        neighbours.append(((0,b),"Empty Jug A"))

    if b > 0:
        neighbours.append(((a,0),"Empty Jug B"))

    amount = min(a,CAP_B - b)

    if amount > 0:
        neighbours.append(
            ((a -amount,b + amount),
             "Pour Jug A -> Jug B")
            )
    amount = min(b,CAP_A - a)

    if amount > 0:
        neighbours.append(
            ((a + amount,b - amount),
             "Pour Jug B ->Jug A")
            )
    return neighbours

def bfs(start):
    queue = [(start, [])]
    visited = set()

    while queue:

        state, path = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        if state[0] == Goal or state[1] ==Goal:
            return path + [(state, "Goal Reached")]

        for neighbours, action in get_neighbours(state):
            if neighbours not in visited:
                queue.append(
                    (neighbours,path +[(neighbours,action)])
                    )
    return None

start = (0,0)

solution = bfs(start)

if solution:

    print("Solution found in",len(solution)-1,"moves:\n")
    print("Initial State:")
    print_state(start)

    for state,action in solution:
        print(action)
        print_state(state)

else:
    print("No solution found")
