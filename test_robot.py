import unittest
from io import StringIO
from unittest.mock import patch
from world import obstacles as world_obstacles
from robot import *

class TestRobot(unittest.TestCase):

    def setUp(self) -> None:
        """
        Special function that runs before every test function
        """

        history = []
        self.robot_name = "HAL"
        self.maxDiff = 10000
        self.terminal_output = StringIO()
        sys.stdout = self.terminal_output

    def tearDown(self) -> None:
        """
        Special function that runs after every test function
        """

        sys.stdout = sys.__stdout__
        self.terminal_output.close()


    world_obstacles.random.randint = lambda x,y:1

    @patch("sys.stdin", StringIO("HAL\noff"))
    def test_print_obstacles(self):
        robot_start()
        expected_output = """What do you want to name your robot? HAL: Hello kiddo!
There are some obstacles:
- At position 1,1 (to 5,5)
HAL: What must I do next? HAL: Shutting down.."""
        self.assertEqual(expected_output,self.terminal_output.getvalue().strip())


    def test_split_command_input_type(self):
        value = split_command_input("replay silent")
        self.assertIsInstance(value,tuple)
        self.assertEqual(len(value),2)

    
    def test_split_command_input(self):
        test_output = split_command_input("forward 10")
        self.assertEqual(test_output,("forward","10"))
        test_output2 = split_command_input("replay 2")
        self.assertEqual(test_output2,("replay","2"))
        test_output3 = split_command_input("replay")
        self.assertEqual(test_output3,("replay",""))


    def test_valid_command(self):
        test_output = valid_command("replay")
        self.assertEqual(True,test_output)
        test_output2 = valid_command("replay silent")
        self.assertEqual(True,test_output2)
        test_output3 = valid_command("replay reversed")
        self.assertEqual(True,test_output3)

    
    def test_do_help_type(self):
        test_output = do_help()
        self.assertIsInstance(test_output,tuple)
        self.assertEqual(len(test_output),2)

    
    def test_do_help_type(self):
        test_output = do_help()
        expected_output = (True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
""")
        self.assertEqual(test_output,expected_output)

if __name__ == "__main__":
    unittest.main()
