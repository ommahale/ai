from queue import PriorityQueue

# Class to represent a state of the puzzle
class PuzzleState:
    def __init__(self, puzzle, parent=None, move=None, cost=0):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move
        self.cost = cost
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Function to get the coordinates of the blank space (0)
    def find_blank(self):
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] == 0:
                    return i, j

    # Function to generate possible successor states
    def generate_successors(self):
        successors = []
        i, j = self.find_blank()

        # Generate successor by moving the blank space left
        if j > 0:
            new_puzzle = [row[:] for row in self.puzzle]
            new_puzzle[i][j], new_puzzle[i][j - 1] = new_puzzle[i][j - 1], new_puzzle[i][j]
            successors.append(PuzzleState(new_puzzle, self, "LEFT", self.cost + 1))

        # Generate successor by moving the blank space right
        if j < len(self.puzzle[i]) - 1:
            new_puzzle = [row[:] for row in self.puzzle]
            new_puzzle[i][j], new_puzzle[i][j + 1] = new_puzzle[i][j + 1], new_puzzle[i][j]
            successors.append(PuzzleState(new_puzzle, self, "RIGHT", self.cost + 1))

        # Generate successor by moving the blank space up
        if i > 0:
            new_puzzle = [row[:] for row in self.puzzle]
            new_puzzle[i][j], new_puzzle[i - 1][j] = new_puzzle[i - 1][j], new_puzzle[i][j]
            successors.append(PuzzleState(new_puzzle, self, "UP", self.cost + 1))

        # Generate successor by moving the blank space down
        if i < len(self.puzzle) - 1:
            new_puzzle = [row[:] for row in self.puzzle]
            new_puzzle[i][j], new_puzzle[i + 1][j] = new_puzzle[i + 1][j], new_puzzle[i][j]
            successors.append(PuzzleState(new_puzzle, self, "DOWN", self.cost + 1))

        return successors

    # Function to calculate the heuristic (Manhattan distance) for the current state
    def calculate_heuristic(self):
        distance = 0
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                if self.puzzle[i][j] != self.goal[i][j] and self.puzzle[i][j] != 0:
                    x, y = divmod(self.puzzle[i][j] - 1, len(self.puzzle))
                    distance += abs(x - i) + abs(y - j)
        return distance

    # Function to check if the current state is the goal state
    def is_goal(self):
        return self.puzzle == self.goal

    # Function to get the path from the initial state to the current state
    def get_path(self):
        path = []
        current_state = self
        while current_state.parent is not None:
            path.insert(0, current_state.move)
            current_state = current_state.parent
        return path

    # Function to compare states based on their costs and heuristics
    def __lt__(self, other):
        return self.cost + self.calculate_heuristic() < other.cost + other.calculate_heuristic()

# Function to solve the 8-puzzle problem using A* algorithm
def solve_8_puzzle(initial_state):
    open_list = PriorityQueue()
    open_list.put(initial_state)

    while not open_list.empty():
        current_state = open_list.get()

        if current_state.is_goal():
            return current_state.get_path()

        successors = current_state.generate_successors()
        for successor in successors:
            open_list.put(successor)

    return None

# Main function
def main():
    # Get user input for the initial state of the puzzle
    initial_puzzle = []
    print("Enter the initial state of the puzzle (use 0 to represent the blank space):")
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_puzzle.append(row)

    # Create the initial state
    initial_state = PuzzleState(initial_puzzle)

    # Solve the 8-puzzle problem using A* algorithm
    solution = solve_8_puzzle(initial_state)

    # Print the solution path
    if solution is not None:
        print("Solution found!")
        print("Moves:", solution)
    else:
        print("No solution found!")

# Run the main function
main()