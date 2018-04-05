import unittest
from Pencil import Pencil
from Paper import Paper


class TestPencilDurability(unittest.TestCase):

    # Tests if single string is correctly written to piece of paper
    def test_write_one_string(self):
        pencil = Pencil()
        paper = Paper()
        string_to_write = "which"

        pencil.write(paper, string_to_write)

        self.assertEqual(paper.text, string_to_write)

    # Test is multiple strings are correctly written to piece of paper
    def test_write_multiple_strings(self):
        pencil = Pencil()
        paper = Paper()
        string_to_write_1 = "which "
        string_to_write_2 = "wrist"

        pencil.write(paper, string_to_write_1)
        pencil.write(paper, string_to_write_2)

        self.assertEqual(paper.text, string_to_write_1 + string_to_write_2)


if __name__ == "__main__":
    unittest.main()
