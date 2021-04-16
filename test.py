import unittest

class test_game_stats(unittest.TestCase):
    """Tests for game stats"""

    def test_reset_stats(self):
        pass



class test_unicorn_invasion(unittest.TestCase):
    """Test for unicorn_invasion.py"""

    def test_run_game(self):
        pass



def sum(a, b):
    return a + b
class ScorePointsTest(unittest.TestCase):
    """Should earn 50 points once you hit candy"""
    def setUp(self):
        self.a = 25
        self.b = 2

    def test_point_score_1(self):
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)

    def test_point_score_2(self):
        # Act
        result = sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)

class test_unicorn(unittest.TestCase):
    """Test for unicorn.py"""

    def test_update(self):
        pass

if __name__ == '__main__':
    unittest.main()