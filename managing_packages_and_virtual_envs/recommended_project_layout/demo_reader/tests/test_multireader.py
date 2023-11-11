import unittest

import demo_reader.multireader

class TestMultireader(unittest.TestCase):
    def test_initialization(self):
        demo_reader.multireader.MultiReader('test_file.txt')
