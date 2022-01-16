import unittest
from world import obstacles as world_obstacles


class TestObstacles(unittest.TestCase):
    world_obstacles.random.randint = lambda x,y:1
    world_obstacles.create_obs()
    world_obstacles.gen_possible_obs()

    def test_co_or_range(self):
        output = world_obstacles.coord_range()
        self.assertIsInstance(output,tuple)
        self.assertEqual(len(output),2)
    

    def test_create_obstacles(self):
        self.assertTrue(len(world_obstacles.obstacles) >= 0)
        self.assertIsInstance(world_obstacles.obstacles, list)


    def test_all_possible_obstacles(self):
        self.assertTrue(len(world_obstacles.obs_coords) >= 0)
        self.assertIsInstance(world_obstacles.obs_coords,list)


    def test_is_position_blocked(self):

        output = world_obstacles.is_position_blocked(0,0)
        self.assertEqual(False,output)
        output2 = world_obstacles.is_position_blocked(1,1)
        self.assertEqual(True,output2) 


    def test_is_path_blocked(self):
        output = world_obstacles.is_path_blocked(0,0,10,20)
        self.assertEqual(False,output)
        output2 = world_obstacles.is_path_blocked(world_obstacles.obs_coords[0][0],10,world_obstacles.obs_coords[0][0],world_obstacles.obs_coords[0][1])
        self.assertEqual(True,output2)


if __name__ == "__main__":
    unittest.main()
