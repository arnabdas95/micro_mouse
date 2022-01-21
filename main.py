# Micro mouse by Arnab Das
def mouse(grid, i, j,start_i,start_j):

    route = []
    p_queue = [[i, j]]
    while len(p_queue) != 0:
        current = p_queue.pop(0)
        i, j = current[0], current[1]

        # down
        try:
            if math.isnan(grid[i + 1][j]) :
                grid[i + 1][j] = grid[i][j] + 1
                p_queue.append([i + 1, j])
                route.append([i + 1, j])
        except:
            pass

        # up
        try:
            if math.isnan( grid[i - 1][j] ) and (i - 1) >= 0:
                grid[i - 1][j] = grid[i][j] + 1
                p_queue.append([i - 1, j])
                route.append([i - 1, j])
        except:
            pass

            # right
        try:
            if math.isnan(grid[i][j + 1]):
                grid[i][j + 1] = grid[i][j] + 1
                p_queue.append([i, j + 1])
                route.append([i, j + 1])
        except:
            pass

        # left
        try:
            if math.isnan(grid[i][j - 1]) and (j - 1) >= 0:
                grid[i][j - 1] = grid[i][j] + 1
                p_queue.append([i, j - 1])
                route.append([i, j - 1])
        except:
            pass

#get all the path from start to goal
    for item in reversed(route):

        if grid[item[0]][item[1]] < grid[start_i][start_j]:
            break
        else:
            route.remove(item)
    cc = []
    for item in reversed(route):
        if item[0]== start_i +1 and item[1] == start_j and item[0] !=0:
            cc.append(item)
            start_i = item[0]
            start_j = item[1]
        elif  item[0]== start_i -1 and item[1] == start_j and start_i !=0:
            cc.append(item)
            start_i = item[0]
            start_j = item[1]
        elif  item[1]== start_j +1 and item[0] == start_i and item[1] !=0:
            cc.append(item)
            start_i = item[0]
            start_j = item[1]
        elif  item[1]== start_j -1 and item[0] == start_i and start_j !=0:
            cc.append(item)
            start_i = item[0]
            start_j = item[1]
        else:
            pass
    return (grid,route,cc)



import numpy as np
import functools
from tkinter import  *
import random
import copy
import math


def row_col():
# asking for row and column
    start = Tk()
    start.title('select row col')
    start.geometry('300x150')
    row_label = Label(start, text="Enter Row/Column (3-15)")
    row = Entry(start,width=50)
    row.insert(0,"5")

    ready_button = Button(start, text="ENTER", command=lambda: tk_display(start,row))
    row_label.grid()
    row.grid()
    ready_button.grid()

def about():
    about_game = Tk()
    about_game.title('About')
    about_game.geometry('350x150')

    # Create label
    l = Label(about_game, text="MICRO MOUSE GAME\n This game is developed using Python.\n"
                               " The GUI is created by Tkinter.\nDeveloped by Arnab Das ,January, 2022  ", padx=20)
    l.config(font=("Courier", 10))
    l.pack()

def help():
    helps = Tk()
    helps.title('Help')
    helps.geometry('620x200')

    # Create label
    l = Label(helps, text="MICRO MOUSE GAME\n 1. Enter row number.\n2. Row must be 4-15 \n 3. After that Click the left mouse button to add obstacles\n4."
                          " Then click on goal and click left mouse button on grid to select goal.\n5. Then click left mouse to select start"
                               " \n6.Then the path cost and path will come.\n\n\n Developed by Arnab Das ,January, 2022  ", padx=20)
    l.config(font=("Courier", 10))
    l.pack()
#call the starting
row_col()
def new():
    global root

    global obs_state
    obs_state = 1
    root.destroy()
    root = Tk()
    root.title('MICRO_MOUSE BY ARNAB DAS')
    root.resizable(height=False, width=False)
    root.geometry('700x750')
    root.iconbitmap(r'logo.ico')
    # menubar
    menubar = Menu(root)
    root.config(menu=menubar)

    # create menu item
    menubar.add_command(label=" New", command=new)
    menubar.add_command(label=" About", command=about)
    menubar.add_command(label=" Help", command=help)

    row_col()

# main windows
root =Tk()
root.title('MICRO_MOUSE BY ARNAB DAS')
root.resizable(height = False, width = False)
root.geometry('700x750')
root.iconbitmap(r'logo.ico')
#menubar
menubar = Menu(root)
root.config(menu= menubar)
#create menu item
menubar.add_command(label = " New", command= new)
menubar.add_command(label = " About", command= about)
menubar.add_command(label = " Help", command= help)

obs_state = 1




def tk_display(start,row):
    global row_no, col_no,obs_state,next, grid, button_store
    button_store =[]
    row_no = int(row.get())

    if row_no<2 or row_no>15:
        row_no =5
    col_no = row_no
    # main arrqy initialize
    grid= np.empty(row_no*col_no)
    grid.fill(None)
    grid = np.reshape(grid, (row_no,col_no))



    start.destroy()
    count = 0

    for i in range(row_no):
        for j in range(col_no):
            temp = 'b'+ str(count)
            temp = (Button(root, text='O', font="calibri 13", bg='#FEECE9', fg='black', height=int(27 / row_no),
                           width=int(70 / col_no), relief='solid'))
            button_store.append(temp)
            b = temp
            b.configure(command = lambda b=b:  create_obstracle(b))
            temp.grid(row=i, column=j)
            count +=1

    next = (Button(root, text='Goal', font="calibri 13", bg='#FED1EF', fg='black',relief='solid',command = goal))
    next.grid(row=row_no,column=0)

def create_obstracle(b):
    global obs_state, grid, row_no, col_no,g_i,g_j

    if obs_state == 1:
        b['state'] = "disabled"

        b['bg'] = '#2F3A8F'
        b['text'] = "X"

    elif obs_state == 0 :
        b['state'] = "disabled"
        b['bg'] = '#FE7E6D'
        b['text'] = "G"
        next["text"] = 'start'
        obs_state = -1

    elif obs_state == -1:
        b['state'] = 'disabled'
        b['bg'] = '#93FFD8'
        b['text'] = 'S'
        obs_state = 100
        next["text"] = 'play'
    else:
        pass

    # get row and col number from the button and put -1 for blocked item and 1 for goal
    b_number = str(b)
    number = ''
    for item in b_number:
        if item.isdigit():
            number = number + item
    if number == '':
        number = '1'
    g_row = (int(number)-1)//row_no
    g_col = (int(number)-1) % row_no
    if obs_state == 1:
        grid[g_row][g_col] = int(-1)
    if obs_state == -1:
        grid[g_row][g_col] = int(0)
        g_i = g_row
        g_j = g_col

    if  obs_state == 100:
        start_i = g_row
        start_j = g_col
        grid = mouse(grid, g_i, g_j,start_i,start_j)
        route = grid[1]
        cc = grid[2]
        grid= grid[0]



        path(grid,cc)
       # route_path(route)



def goal():
    global obs_state, next
    if obs_state == 1:
        obs_state = 0
        next['text'] = "start"

def path(grid,cc):
    global row_no,col_no, button_store
    c = 0

    for i in range (row_no):
        for j in range (col_no):
            button_store[c]["text"] = grid[i][j]
            if  math.isnan(grid[i][j]) :
                button_store[c]["bg"]  = 'pink'
            if [i,j] in cc:
                root.after(1000,lambda c=c:  update(c))
                #button_store[c]["bg"] = 'yellow'
            c +=1

def update(c):
    button_store[c]["bg"] = 'yellow'
root.mainloop()