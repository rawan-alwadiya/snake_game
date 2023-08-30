# this code to be used in replit.com

# # import modules necessary for the game
# import random
# import curses

# # initialize the cuses liberary to create our screen
# screen = curses.initscr()

# # hide the mouse curser
# curses.curs_set(0)

# # getmax screen height and width
# screen_height, screen_width= screen.getmaxyx()

# # create a new window
# window= curses.newwin(screen_height,screen_width,0,0)

# # allow window to recieve input from the keyboard => 1 means true
# window.keypad(1)

# # set the delay for updating the screen
# window.timeout(125)

# # set the x,y coordinates of the initial position of the snake head
# # using int division by // to return int result

# snk_x = screen_width // 4
# snk_y = screen_height // 2

# # define the initial position for the snake body
# # the snake will be list of the head and body and tail
# snake=[
#   [snk_y,snk_x],
#   [snk_y,snk_x-1],
#   [snk_y,snk_x-2]
# ]

# # create the food in the middle of the window
# food=[screen_height//2 , screen_width//2]

# # add the food by using PI character in the curses module
# window.addch(food[0],food[1],curses.ACS_PI)

# # set initial movement direction to right
# key= curses.KEY_RIGHT

# # create game loop that loops forever until the player loses or quits the game and get the next key that will be presses by the user
# # if the user dosn't input anything, key reamains the same. else key will be set to the new key pressed
# # it returns -1 if there is no input
# # check if the snake colided with the walls or itself 
# # if it colides close the window and exit the program
# # set the new position of the snake head besed on the direction the user pressed
# # when increase the y +1 it will go down to the bottom till we reach the maximum height and -1 it will go up to the top till we reach 0 and when we increase x +1 it will go to the right and when we decrease x -1 it will go to the left
# # insert the new head to the first position in the snake list
# # check if the snake ate the food
# # remove food if snake ate it
# # while food is removed, generate a new food in random place on screen
# # when we generate a new food we made the random position from 1 to screen height or width -1 because we dont want the food te be exactly on the wall
# # set the food to the new food if the new food is not generated in the snake body and add it to the screen
# # otherwise remove the last segment of snake body
# # update the position of the snake on the screen

# while True:
#   next_key = window.getch()
#   key = key if next_key == -1 else next_key
#   # if next_key==-1:
#   #   key = key
#   # else:
#   #   key = next_key
#   if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1:]:
#     curses.endwin() #closing the window
#     quit() #exit the program
#   new_head= [snake[0][0],snake[0][1]]

#   if key == curses.KEY_DOWN:
#     new_head[0] += 1
#   if key == curses.KEY_UP:
#     new_head[0] -= 1
#   if key == curses.KEY_RIGHT:
#     new_head[1] += 1
#   if key == curses.KEY_LEFT:
#     new_head[1] -= 1

#   snake.insert(0, new_head)

#   if snake[0] == food:
#     food = None
#     while food is None:
#       new_food = [
#         random.randint(1,screen_height - 1),
#         random.randint(1,screen_width - 1)
#       ]
#       food = new_food if new_food not in snake else None
#     window.addch(food[0],food[1], curses.ACS_PI)  
#   else:
#     tail= snake.pop()
#     window.addch(tail[0],tail[1],' ')

#   window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)