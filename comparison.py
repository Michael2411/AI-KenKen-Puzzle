from backtracking import *
from forward import *
from Generate import *
from time import time

file = open('comparison.txt','w')
board_size=3
for i in range(5):
    file.write(f'\nBoard size = {board_size}\n')
    for j in range(11):
        file.write(f'\nBoard number {j}\n')
        g= kenken_generate()
        grid, arc=g.generate(board_size)

        time_taken_back = time()
        game = kenken_backtracking()
        result=game.backtracking(grid)
        time_taken_back = time()-time_taken_back
        print(result)
        print(time_taken_back)
        file.write(f'Time taken by backward tracking = {time_taken_back}\n')

        time_taken_forward = time()
        game = kenken_forward()
        result=game.forward_checking(grid)
        time_taken_forward = time()-time_taken_forward
        file.write(f'Time taken by forward checking  = {time_taken_forward}\n')
        print(result)
        print(time_taken_forward)
    board_size = board_size+1

    

    

  
