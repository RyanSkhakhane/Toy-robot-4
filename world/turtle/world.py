import turtle
from world.obstacles import *

cy = turtle.Turtle()

min_y, max_y = -200, 200
min_x, max_x = -100, 100

gen_obs = []



def create_obstacles():
    """
    Creates obstacles
    """
    global gen_obs

    gen_obs = get_obs()
    


def create_boundary():
    """
    Draws the safe zone
    """
    cy.pensize(1)
    cy.speed(5)
    cy.shape("turtle")
    cy.penup()
    cy.fd(101)
    cy.pendown()
    cy.lt(90)
    cy.fd(201)
    cy.lt(90)
    cy.fd(202)
    cy.lt(90)
    cy.fd(402)
    cy.lt(90)
    cy.fd(202)
    cy.lt(90)
    cy.fd(201)
    cy.penup()
    # cy.speed(3)


def draw_obstacles():
    """
    Draws all obstacles
    """

    
    cy.speed(0)
    cy.pensize(1)
    cy.hideturtle()
    cy.penup()

    for obstacle in gen_obs:
        cy.goto(obstacle[0])
        cy.pendown()
        cy.color("cyan")

        cy.begin_fill()
        for i in range(4):
            cy.forward(4)
            cy.left(90)
        cy.end_fill()
        cy.showturtle()
        cy.penup()
        cy.goto(0,0)
        cy.setheading(90)


position_x = 0
position_y = 0


directions = ['forward', 'right', 'back', 'left']


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position is inside the safe zone then reutrns a boolean
    -
    
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')


def update_position(current_direction_index,steps):
    """
    Updates the current x and y positions with regard to direction and specific number of steps
    -
    
    :param steps:
    :return: True if the position was updated, else False
    
    """
    global position_x,position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y) and is_path_blocked(position_x,position_y,new_x,new_y) == False:
        position_x = new_x
        position_y = new_y
        return True,True
    elif is_position_allowed(new_x, new_y) and is_path_blocked(position_x,position_y,new_x,new_y) == True:
        return True,False
    elif is_position_allowed(new_x, new_y) == False and is_path_blocked(position_x,position_y,new_x,new_y) == False:
        return False,True


create_boundary()
# draw_obstacles()

# cy = turtle.Turtle()
# cy.penup()
# cy.home()
# cy.color("white")
# cy.left(90)
