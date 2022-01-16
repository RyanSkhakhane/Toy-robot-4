import unittest
from world import obstacles as world_obstacles
from world.text.world import *



class TestWorld(unittest.TestCase):
    world_obstacles.random.randint = lambda a,b : 1
    world_obstacles.create_obs()

    def test_created_obstacle(self):
        world_obstacles.create_obs()
        self.assertEqual([(1,1),(5,1),(5,5),(1,5)],world_obstacles.obstacles[0])


    def test_len_created_obstacles(self):
        world_obstacles.random.randint = lambda a,b : 19
        self.assertEqual(3,len(world_obstacles.obstacles))


    def test_is_position_allowed(self):
        self.assertEqual(False, is_position_allowed(105,2))
        self.assertEqual(True,is_position_allowed(-3,-2))
        self.assertEqual(True,is_position_allowed(3,2))


    def test_update_position(self):
        self.assertEqual((True,True),update_position(0,1))
        self.assertEqual((True,True),update_position(0,1))
        self.assertEqual((True,True),update_position(0,10))
        self.assertEqual((True,True),update_position(0,0))
    

    
   



if __name__ == "__main__":
    unittest.main()
