from backtracking import *
from forward import *
from Generate import *
from time import time
import xlwt
from xlwt import Workbook
from kenken_arc import * 

board_size=3
wb = Workbook()
sheet =wb.add_sheet('Results')

## styles for the font while writing in excel shee
style_header = xlwt.easyxf('font: bold 1 ,italic 1, color red; align: horiz center')
style_content = xlwt.easyxf('font: bold 1, color blue;align: horiz center')

sheet.write(0,1,'Board Size',style_header)
sheet.write(0,2,'Backtracking',style_header)
sheet.write(0,3,'Forward Checking',style_header)
sheet.write(0,4,'Arc Consistency',style_header)
sheet.write(0,5,'Arc Consistency sol_only',style_header)
row = 1 #we start writing from row number 1
number=1#board number

for i in range(7):
    for j in range(15):
        sheet.write(row,0,f'Board Number {number}',style_header)
        sheet.write(row,1,f'{board_size}x{board_size}',style_content)

        ##generating a board for all algorithms
        g= kenken_generate()
        grid, arc=g.generate(board_size)  

        ##backward tracking
        print('back')
        time_taken_back = time()
        game = kenken_backtracking()
        result=game.backtracking(grid)
        time_taken_back = time()-time_taken_back
        sheet.write(row,2,time_taken_back,style_content)
    
        ##forward checking
        print('forward')
        time_taken_forward = time()
        game = kenken_forward()
        result=game.forward_checking(grid)
        time_taken_forward = time()-time_taken_forward
        sheet.write(row,3,time_taken_forward,style_content)
        
        ##arc checking
        print('arc')
        time_taken_arc= time()
        game = InitializeArc()
        result,t= game.getCorrectValues(board_size, grid, arc)
        time_taken_arc= time()-time_taken_arc
        sheet.write(row,4,time_taken_arc,style_content)
        sheet.write(row,5,time_taken_arc-t,style_content)

        print(f'board {number}')
        row+=1
        number+=1
        wb.save('comparions.xls')
        #print(f'board number{number} done')
    board_size = board_size+1


    

    

  
