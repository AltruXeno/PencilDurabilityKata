import unittest
from Pencil import Pencil
from Paper import Paper


class TestPencilDurability(unittest.TestCase):

    # Setup initial object creation
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()

    def determine_expected_score(self, string_to_write):
        score = 0

        # Remove the specified whitespaces from the string and see how many characters remain
        string_without_whitespaces = string_to_write.replace(' ', '').replace('\n', '')

        # Determine the score -- capital letters are worth 2 while lowercase letters are worth 1.
        # Non-alphanumeric characters were not specified and will be worth one point as well.
        for character in string_without_whitespaces:
            if character.isupper():
                score += 2
            else:
                score += 1

        return score

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
        expected_score = self.determine_expected_score(string_to_write)

        self.pencil.write(self.paper, string_to_write)

        self.assertEqual(self.pencil.point_durability, point_durability - expected_score)

    def test_pencil_point_durability_degradation_character_case(self):
        string_to_write = "Which wrist watches are Swiss wrist watches?"
        point_durability = self.pencil.point_durability

        expected_score = self.determine_expected_score(string_to_write)

        self.pencil.write(self.paper, string_to_write)

        self.assertEqual(self.pencil.point_durability, point_durability - expected_score)


if __name__ == "__main__":
    unittest.main()
