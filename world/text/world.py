from world.obstacles import *

# variables tracking position and direction
position_x = 0
position_y = 0


gen_obs = []


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

directions = ['forward', 'right', 'back', 'left']

def create_obstacles():
    """
    Creates obstacles
    """
    global gen_obs

    gen_obs = get_obs()

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

    global position_x, position_y
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

