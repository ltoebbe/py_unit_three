import unittest
import assignment_three


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(52, assignment_three.calculate_total_surface_area(3, 2, 4))


if __name__ == '__main__':
    unittest.main()
