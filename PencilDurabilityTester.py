import unittest
import random
import string
import math
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

    # Returns a string of random letters of length character_count
    def get_randomized_string(self, character_count):
        # Fill the string with random characters
        randomized_string = ""
        for i in range(character_count):
            randomized_string += random.choice(string.ascii_lowercase)

        return randomized_string

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

    # Test to see if uppercase letters cost 2 point durability and lowercase letters cost 1
    def test_pencil_point_durability_degradation_character_case(self):
        string_to_write = "Which wrist watches are Swiss wrist watches?"
        point_durability = self.pencil.point_durability

        expected_score = self.determine_expected_score(string_to_write)

        self.pencil.write(self.paper, string_to_write)

        self.assertEqual(self.pencil.point_durability, point_durability - expected_score)

    # Test to ensure that pencils can't write when their point durability is 0
    def test_pencils_cannot_write_with_zero_durability(self):
        self.pencil = Pencil(10)
        number_of_characters = 20

        # Fill the string with random characters
        string_to_write = self.get_randomized_string(number_of_characters)

        self.pencil.write(self.paper, string_to_write)

        paper_text_count = len(self.paper.text.strip())

        self.assertEqual(paper_text_count, number_of_characters - self.pencil.start_point_durability)

    # Test that makes sure the point durability is reset when pencil is sharpened
    def test_pencil_sharpening_resets_point_durability(self):
        self.pencil = Pencil(10)
        number_of_characters = 10

        string_to_write = self.get_randomized_string(number_of_characters)

        self.pencil.write(self.paper, string_to_write)

        self.pencil.sharpen()

        self.assertEqual(self.pencil.start_point_durability, self.pencil.point_durability)

    # Test to ensure that pencil cannot be sharpened when length is zero
    def test_pencil_sharpening_decreases_pencil_length(self):
        pencil_length = self.pencil.length
        times_to_sharpen = 2

        for i in range(times_to_sharpen):
            self.pencil.sharpen()

        self.assertEqual(self.pencil.length, pencil_length - times_to_sharpen)

    # Test to ensure that pencil cannot be sharpened when length is zero
    def test_pencil_zero_length_prohibits_sharpen(self):
        pencil_length = self.pencil.length
        string_to_write = self.get_randomized_string(10)

        for i in range(pencil_length):
            self.pencil.sharpen()

        self.pencil.write(self.paper, string_to_write)

        self.pencil.sharpen()

        self.assertNotEqual(self.pencil.start_point_durability, self.pencil.point_durability)

    # Test erasing a word from the page text
    def test_erase_single_word_from_text(self):
        string_to_write = "which wrist watches"
        string_to_erase = "wrist"

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)

        self.assertEqual(self.paper.text.find(string_to_erase), -1)

    # Test that erasing a word chooses the last written word if more than one
    def test_erase_last_written_word_if_duplicates(self):
        string_to_write = "which wrist watches are swiss wristwatches"
        string_to_erase = "wrist"

        self.pencil.write(self.paper, string_to_write)
        last_word_position = self.paper.text.rfind(string_to_erase)
        self.pencil.erase(self.paper, string_to_erase)

        self.assertNotEqual(last_word_position, self.paper.text.rfind(string_to_erase))
        # A second assert to ensure that we haven't actually deleted all instances of string_to_erase
        self.assertNotEqual(self.paper.text.rfind(string_to_erase), -1)

    # Test to see erasing characters decreases eraser durability
    def test_erase_text_decreases_eraser_durability(self):
        string_to_write = "which wrist watches are swiss wrist watches"
        string_to_erase = "wrist"
        eraser_durability = self.pencil.eraser_durability

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)

        self.assertEqual(self.pencil.eraser_durability, eraser_durability - len(string_to_erase))

    # Test to ensure that eraser cannot erase if eraser durability is zero
    def test_eraser_cannot_erase_when_durability_zero(self):
        test_durability = 3
        self.pencil = Pencil(eraser_durability=test_durability)
        string_to_write = "wrist"
        string_to_erase = "wrist"

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)

        self.assertEqual(self.paper.text.count(' '), test_durability)

    # Test to ensure that eraser durability not decreased when "erasing" whitespace
    def test_eraser_durability_ignores_whitespaces(self):
        string_to_write = "which wrist watches are swiss"
        string_to_erase = "wrist watches are"
        eraser_durability = self.pencil.eraser_durability

        # Remove the specified whitespaces from the string and see how many characters remain
        expected_score = len(string_to_erase.replace(' ', ''))

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)

        self.assertEqual(self.pencil.eraser_durability, eraser_durability - expected_score)

    # Test to ensure that characters are erased from right to left
    def test_eraser_erases_characters_right_to_left(self):
        test_durability = 3
        self.pencil = Pencil(eraser_durability=test_durability)
        string_to_write = "which"
        string_to_erase = "which"

        expected_string = string_to_write[:-test_durability]
        expected_string += ' ' * test_durability

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)

        self.assertEqual(self.paper.text, expected_string)

    # Test to ensure pencils can edit previously erased text
    def test_pencil_edit_inserts_at_previously_erased_text(self):
        string_to_write = "which wrist watches"
        string_to_erase = "wrist"
        string_to_insert = "ankle"

        expected_string = string_to_write.replace(string_to_erase, string_to_insert)

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)
        self.pencil.edit(self.paper, string_to_insert)

        self.assertEqual(self.paper.text, expected_string)

    # Test to make sure that it isn't a magic pencil and editing text costs point durability
    def test_pencil_edit_decreases_point_durability(self):
        string_to_write = "which wrist watches"
        string_to_erase = "watches"
        string_to_insert = "anklets"

        self.pencil.write(self.paper, string_to_write)
        point_durability = self.pencil.point_durability
        self.pencil.erase(self.paper, string_to_erase)
        self.pencil.edit(self.paper, string_to_insert)

        self.assertEqual(self.pencil.point_durability, point_durability - len(string_to_insert))

    # Test to determine if spaces are missing if edited (inserted) text is smaller than allotted space
    def test_pencil_edit_cannot_shift_text_left(self):
        string_to_write = "which wrist watches"
        string_to_erase = "wrist"
        string_to_insert = "toe"

        text_pieces = string_to_write.split(string_to_erase)
        expected_string = text_pieces[0]
        expected_string += string_to_insert
        expected_string += ' ' * (len(string_to_erase) - len(string_to_insert))
        expected_string += text_pieces[1]

        self.pencil.write(self.paper, string_to_write)
        self.pencil.erase(self.paper, string_to_erase)
        self.pencil.edit(self.paper, string_to_insert)

        self.assertEqual(self.paper.text, expected_string)


if __name__ == "__main__":
    unittest.main()
