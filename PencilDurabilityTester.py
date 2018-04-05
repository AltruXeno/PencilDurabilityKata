import unittest
from Pencil import Pencil
from Paper import Paper


class TestPencilDurability(unittest.TestCase):

    # Tests if singular string is correctly written to piece of paper
    def test_write_one_string(self):
        pencil = Pencil()
        paper = Paper()
        string_to_write = "which"

        pencil.write(paper, string_to_write)

        self.assertEqual(paper.text, string_to_write)


if __name__ == "__main__":
    unittest.main()
