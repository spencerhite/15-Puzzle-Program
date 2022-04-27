from search import *
import time
import tracemalloc






#Pulled a copy of EightPuzzla from search.py
class FifteenPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 15 on a 4x4 board, where one of the
    squares is a blank. A state is represented as a tuple of length 16, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)
        #intialized game baord
    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
            #finds indexed states of blank spaces
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """
        #defines the possible actions of
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)
        #indexes all blank squares
        if index_blank_square % 4 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 4:
            possible_actions.remove('UP')
        if index_blank_square % 4 == 3:
            possible_actions.remove('RIGHT')
        if index_blank_square > 11:
            possible_actions.remove('DOWN')
        #blank square indexing with modulus==number of rows
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -4, 'DOWN': 4, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))

def main():


    initial = (1, 0, 2, 4, 5, 7, 3, 8, 9, 6, 11, 12, 13, 10, 14, 15)

    puzzle = FifteenPuzzle(initial)
    #initializes the board with class problem
    start_time = time.perf_counter() #starts runtime timer
    tracemalloc.start() #starts tracking memory usage
    result = breadth_first_graph_search(puzzle) #assigns algo result to variable
    current, peak = tracemalloc.get_traced_memory() #collects memory usage of peak and current usage
    end_time = time.perf_counter()  # ends run time counter
    solution = result[0].solution()
    #displays output
    print("Searching Strategy: Breadth First Search")
    print("\nMoves to solve puzzle: ", solution)
    print("\nNumber of Nodes expanded: ",result[1])
    print("\nTime taken (seconds): ",end_time - start_time)
    print(f"\nPeak Memory Usage was {peak / 10 ** 3}KB")
    tracemalloc.stop()

    print("\n|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")

    puzzle = FifteenPuzzle(initial) #initializes the board with class problem
    start_time = time.perf_counter() #starts runtime timer
    tracemalloc.start() #starts tracking memory usage
    result = iterative_deepening_search(puzzle) #assigns algo result to variable
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.perf_counter()  # ends run time counter
    solution = result[0].solution()
    # displays output
    print("\nSearching Strategy: Depth First Search")
    print("\nMoves to solve puzzle: ", solution)
    print("\nNumber of Nodes expanded: ", result[1])
    print("\nTime taken (seconds): ", end_time - start_time)
    print(f"\nPeak Memory Usage was {peak / 10 ** 3}KB")
    tracemalloc.stop()
main()
