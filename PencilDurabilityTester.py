import unittest
from Pencil import Pencil
from Paper import Paper


class TestPencilDurability(unittest.TestCase):

    # Setup initial object creation
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()

    # Tests if single string is correctly written to piece of paper
    def test_write_one_string(self):
        string_to_write = "which"

        self.pencil.write(self.paper, string_to_write)

        self.assertEqual(self.paper.text, string_to_write)

    # Test is multiple strings are correctly written to piece of paper
    def test_write_multiple_strings(self):
        string_to_write_1 = "which "
        string_to_write_2 = "wrist"

        self.pencil.write(self.paper, string_to_write_1)
        self.pencil.write(self.paper, string_to_write_2)

        self.assertEqual(self.paper.text, string_to_write_1 + string_to_write_2)

    # Test to determine if pencil point durability degrades when writing
    def test_pencil_point_durability_degradation(self):
        string_to_write = "which"
        point_durability = self.pencil.point_durability

        self.pencil.write(self.paper, string_to_write)

        self.assertEqual(self.pencil.point_durability, point_durability - len(string_to_write))

    # Test to make sure whitespaces don't degrade pencil point durability
    def test_pencil_point_durability_ignores_whitespaces(self):
        string_to_write = "which wrist watches are swiss wrist watches?"
        point_durability = self.pencil.point_durability

        # Remove the specified whitespaces from the string and see how many characters remain
        string_without_whitespaces = string_to_write.replace(' ', '').replace('\n', '')
        number_of_characters = len(string_without_whitespaces)

        self.pencil.write(self.paper, string_to_write)

        self.assertEqual(self.pencil.point_durability, point_durability - number_of_characters)


if __name__ == "__main__":
    unittest.main()
