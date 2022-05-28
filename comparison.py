from backtracking import *
from forward import *
from Generate import *
from time import time
import xlwt
from xlwt import Workbook

file = open('comparison.txt','w')
board_size=3

wb = Workbook()
sheet =wb.add_sheet('Results')

## styles for the font while writing in excel sheet
style_header = xlwt.easyxf('font: bold 1 ,italic 1, color red; align: horiz center')
style_content = xlwt.easyxf('font: bold 1, color blue;align: horiz center')

sheet.write(0,1,'Board Size',style_header)
sheet.write(0,2,'Backward Tracking',style_header)
sheet.write(0,3,'Forward Checking',style_header)
sheet.write(0,4,'Arc Consistency',style_header)
row = 1 #we start writing from row number 1
number=1 #board number

for i in range(4):
    file.write(f'\nBoard size = {board_size}\n')
    for j in range(15):
        file.write(f'\nBoard number {number}\n')
        sheet.write(row,0,f'Board Number {number}',style_header)
        sheet.write(row,1,f'{board_size}x{board_size}',style_content)

        ##generating a board for all algorithms
        g= kenken_generate()
        grid, arc=g.generate(board_size)

        ##backward tracking
        time_taken_back = time()
        game = kenken_backtracking()
        result=game.backtracking(grid)
        time_taken_back = time()-time_taken_back
        file.write(f'Time taken by backward tracking = {time_taken_back}\n')
        sheet.write(row,2,time_taken_back,style_content)
        print(result)
        

        ##forward checking
        time_taken_forward = time()
        game = kenken_forward()
        result=game.forward_checking(grid)
        time_taken_forward = time()-time_taken_forward
        file.write(f'Time taken by forward checking  = {time_taken_forward}\n')
        sheet.write(row,3,time_taken_forward,style_content)

        row+=1
        number+=1
    board_size = board_size+1

wb.save('comparions.xls')
    

    

  
