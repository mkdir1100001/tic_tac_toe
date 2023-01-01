import tkinter as tki
from random import randint

BACKGROUND_COLOR = "#F5F6E8"
player_shape, bot_shape = None, None
game_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
window = tki.Tk()
window.title("TIC TAC TOE")
window.config(width=600, height=600, padx=50, pady=50, background=BACKGROUND_COLOR)

welcome_message = tki.Label(
    text="Press X or O",
    font=("Arial", 16, "normal"),
    background=BACKGROUND_COLOR)
welcome_message.pack()

canvas = tki.Canvas(window,  width=400, height=400, background=BACKGROUND_COLOR, highlightthickness=False)
background_img = tki.PhotoImage(file="images/board_image.png")
canvas.create_image(200, 225, image=background_img)
canvas.pack(anchor='nw', fill='both', expand=1)

def key_event(event):
    global player_shape, bot_shape
    if welcome_message["text"] == "Press X or O":
        if event.char.upper() == "X":
            print("x chosen")
            welcome_message.config(text="Make a move.")
            player_shape = "x"
            bot_shape = "o"
        if event.char.upper() == "O":
            print("o chosen")
            welcome_message.config(text="Make a move.")
            player_shape = "o"
            bot_shape = "x"

def draw_shape(x, y, shape):
    x = 35 + x * 115
    y =  90 + y * 115
    shape_img = tki.PhotoImage(file=f"images/{shape}_img.png")

    label1 = tki.Label(image=shape_img)
    label1.image = shape_img
    label1.place(x=x, y=y)
    
def bot_move(shape):
    global game_matrix
    
    x, y = randint(0, 2), randint(0, 2)
    while game_matrix[y][x] != 0:
        x, y = randint(0, 2), randint(0, 2)
    print(f"Bot choice : {x}, {y}")
    game_matrix[y][x] = shape
    x = 35 + x * 115
    y =  90 + y * 115
    shape_img = tki.PhotoImage(file=f"images/{shape}_img.png")

    label1 = tki.Label(image=shape_img)
    label1.image = shape_img
    label1.place(x=x, y=y)

def mouse_event(event):
    column, row = None, None
    if welcome_message["text"] == "Make a move.":
        column_coordinates = [(0, 25, 145,), (1, 145, 255), (2, 255, 360)]
        for element in column_coordinates:
            left_border, right_border = element[1], element[2]
            if left_border < event.x < right_border:
                column = element[0]
        
        row_coordinates = [(0, 60, 170,), (1, 170, 280), (2, 280, 390)]
        for element in row_coordinates:
            left_border, right_border = element[1], element[2]
            if left_border < event.y < right_border:
                row = element[0]
        
        if (column != None and row != None):
            if game_matrix[row][column] == 0:
                game_matrix[row][column] = player_shape
                draw_shape(column, row, shape=player_shape)
                winner = check_winner()
                if winner:
                    welcome_message.config(text= f"'{winner.upper()}' won the game!")
                else:
                    bot_move(bot_shape)
                    winner = check_winner()
                    if winner:
                        welcome_message.config(text= f"'{winner.upper()}' won the game!")
                print(game_matrix)
            

def check_winner():
    global game_matrix
    
    for row in game_matrix:
        if 0 not in row and len(set(row)) == 1:
            return row[0]
    
    for i in range(3):
        element_set = [ game_matrix[i][0] ]
        for element in game_matrix:
            element_set.append(element[i])
        
        if 0 not in element_set and len(set(element_set)) == 1:
            return game_matrix[i][0]

    diagonal_1 = [game_matrix[i][i] for i in range(3)]
    diagonal_2 = [game_matrix[i][2 - i] for i in range(3)]
    if len(set(diagonal_1)) == 1 and diagonal_1[0] != 0:
        return diagonal_1[0]
    elif len(set(diagonal_2)) == 1 and diagonal_2[0] != 0:
        return diagonal_2[0]
    else:
        return False

window.bind("<Key>", key_event)
window.bind("<Button-1>", mouse_event)

window.mainloop()