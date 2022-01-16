import random

obstacles = []
obs_coords = []

def coord_range():
    """
    Generates x and y coordinates in range of the safe zone
    """
    x = random.randint(-100,100)
    y = random.randint(-200,200) 
    return x,y


def create_obs():
    """
    Creates obstacles
    """
    for i in range(random.randint(1,10)):
        x,y = coord_range()
        obstacle = []
    
        if x == 0 and y == 0:
            continue
        
        obstacle.append((x,y))
        obstacle.append((x+4,y))
        obstacle.append((x+4,y+4))
        obstacle.append((x,y+4))

        obstacles.append(obstacle)



def gen_possible_obs():
    """
    Generates every possible obstacle coordinate
    from the given corners
    """

    for obstacle in obstacles:
        for co_ord in obstacle:
            if obstacle.index(co_ord) == 0:
                obs_coords.append((co_ord[0] + 1,co_ord[1]))
                obs_coords.append((co_ord[0] + 2,co_ord[1]))
                obs_coords.append((co_ord[0] + 3,co_ord[1]))
                obs_coords.append((co_ord[0] + 4,co_ord[1]))
            
            elif obstacle.index(co_ord) == 1:
                obs_coords.append((co_ord[0],co_ord[1] +1))
                obs_coords.append((co_ord[0],co_ord[1] +2))
                obs_coords.append((co_ord[0],co_ord[1] +3))
                obs_coords.append((co_ord[0],co_ord[1] +4))

            elif obstacle.index(co_ord) == 2:
                obs_coords.append((co_ord[0] - 1,co_ord[1]))
                obs_coords.append((co_ord[0] - 2,co_ord[1]))
                obs_coords.append((co_ord[0] - 3,co_ord[1]))
                obs_coords.append((co_ord[0] - 4,co_ord[1]))

            elif obstacle.index(co_ord) == 3:
                obs_coords.append((co_ord[0],co_ord[1] -1))
                obs_coords.append((co_ord[0],co_ord[1] -2))
                obs_coords.append((co_ord[0],co_ord[1] -3))
                obs_coords.append((co_ord[0],co_ord[1] -4))

gen_possible_obs()



def is_position_blocked(x,y):
    """
    Checks if a specific position is blocked then returns a boolean
    """
    if (x,y) in obs_coords:
        return True
    else:
        return False


def is_path_blocked(x1,y1,x2,y2):
    """
    Checks if the path is blocked then returns a boolean
    """
    for obstacle in obstacles:
        for co_ord in obstacle[0:1]:
            if x1 == x2 and x1 in range(co_ord[0],co_ord[0] + 5):
                if y1 < co_ord[1] and y2 >= co_ord[1]:
                    return True
                elif y1 > co_ord[1] and y2 <= co_ord[1]:
                    return True
            elif y1 == y2 and y1 in range(co_ord[1],co_ord[1] + 5):
                if x1 < co_ord[0] and x2 >= co_ord[0]:
                    return True
                elif x1 > co_ord[0] +4 and x2 <= co_ord[0] + 4:
                    return True
    return False


def get_obs():
    """
    Returns a list of all the obstacle
    """
    global obstacles

    obstacles = []
    create_obs()

    return obstacles
