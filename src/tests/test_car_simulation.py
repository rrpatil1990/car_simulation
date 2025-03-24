import unittest
from ..main.car_simulation import rotate_left, rotate_right, move_forward, run_commands

class TestCarSimulationFunctions(unittest.TestCase):

    def test_rotate_left(self):
        self.assertEqual(rotate_left('N'), 'W')
        self.assertEqual(rotate_left('E'), 'N')
        self.assertEqual(rotate_left('S'), 'E')
        self.assertEqual(rotate_left('W'), 'S')

    def test_rotate_right(self):
        self.assertEqual(rotate_right('N'), 'E')
        self.assertEqual(rotate_right('E'), 'S')
        self.assertEqual(rotate_right('S'), 'W')
        self.assertEqual(rotate_right('W'), 'N')

    def test_move_forward(self):
        self.assertEqual(move_forward(1, 1, 'N', 10, 10), (1, 2))
        self.assertEqual(move_forward(1, 1, 'E', 10, 10), (2, 1))
        self.assertEqual(move_forward(1, 1, 'S', 10, 10), (1, 0))
        self.assertEqual(move_forward(1, 1, 'W', 10, 10), (0, 1))

        self.assertEqual(move_forward(0, 0, 'W', 10, 10), (0, 0))
        self.assertEqual(move_forward(0, 0, 'S', 10, 10), (0, 0))
        self.assertEqual(move_forward(9, 9, 'E', 10, 10), (9, 9))
        self.assertEqual(move_forward(9, 9, 'N', 10, 10), (9, 9))

    def test_run_commands(self):
        car = ('A', 1, 2, 'N', 'FFRFFFFRRL')
        self.assertEqual(run_commands(car, 10, 10), (5, 4, 'S'))

        car2 = ('B', 0, 0, 'S', 'FFF')  # Starting at (0, 0) facing South
        self.assertEqual(run_commands(car2, 10, 10), (0, 0, 'S'))


if __name__ == '__main__':
    unittest.main()
