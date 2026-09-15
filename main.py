puzzle = [ [] for i in range(0, 9, 1) ]

def print_puzzle (puzzle):

    for i in range(0, 9 , 1):
        for j in range(0, 9 , 1):
            puzzle[i].append(0)

    for i in range (0, 9 , 1):
        print(puzzle[i] )
        print('\n')


print_puzzle(puzzle)

