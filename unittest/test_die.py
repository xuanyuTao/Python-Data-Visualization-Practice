import unittest
from die import Die


class TestDie(unittest.TestCase):
    """Tests for the class Die."""

    def setUp(self):
        """
        Create a die and a list of values for use in all test methods.
        """
        num_sides = 8
        self.my_die = Die(num_sides)
        self.values = list(range(1, num_sides + 1))

    def test_roll_die_once(self):
        """Test rolling the die once and the result is correct."""
        result = self.my_die.roll()
        self.assertIn(result, self.values)

    def test_roll_die_three_times(self):
        """Test rolling the die three times and the results are correct."""
        results = []
        for roll_num in range(3):
            result = self.my_die.roll()
            results.append(result)
        for result in results:
            self.assertIn(result, self.values)


if __name__ == '__main__':
    unittest.main()
