import xlrd
import matplotlib.pyplot as plt
import numpy as np

# Give the location of the file
loc = ("comparisons.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
back=[]
forward=[]
arc=[]
arc_sol=[]
count=0
cell1=0
cell2=0
cell3=0
cell4=0

for j in range(sheet.nrows-1):
    cell1=cell1+sheet.cell_value(j+1,2)
    cell2=cell2+sheet.cell_value(j+1,3)
    cell3=cell3+sheet.cell_value(j+1,4)
    cell4=cell4+sheet.cell_value(j+1,5)
    count+=1
    if count==15:
        back.append(cell1/15)
        forward.append(cell2/15)
        arc.append(cell3/15)
        arc_sol.append(cell4/15)
        count=0
        cell1=0
        cell2=0
        cell3=0
        cell4=0

x_axis=[3,4,5,6,7,8,9]
plt.plot(x_axis,back,label='backtracking')
plt.plot(x_axis,forward,label='forward checking')
plt.plot(x_axis,arc,label='arc consistency')
plt.plot(x_axis,arc_sol,label='arc solution only')
plt.legend()
plt.savefig('comparisons_graph.png',dip=100)
plt.show()