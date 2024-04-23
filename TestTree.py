import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def test_find_existing_data(self):
        # Create a simple binary search tree
        copac = Tree()
        copac.add(5)
        copac.add(3)
        copac.add(7)
        copac.add(2)
        copac.add(4)
        copac.add(6)
        copac.add(8)

        result = copac._find(4, copac.getRoot())
        self.assertIsNotNone(result)

        self.assertEqual(result.data, 4)

    def test_find_non_existing_data(self):
        copac = Tree()
        copac.add(5)
        copac.add(3)
        copac.add(7)
        copac.add(2)
        copac.add(4)
        copac.add(6)
        copac.add(8)
        result = copac._find(9, copac.getRoot())

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()