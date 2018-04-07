import re

class Pencil(object):
    def __init__(self, point_durability=100, length=3, eraser_durability=100):
        self.start_point_durability = point_durability
        self.point_durability = point_durability
        self.eraser_durability = eraser_durability
        self.length = length

    def write(self, paper, string_to_write):

        for letter in string_to_write:
            # If we have no point durability left, simply write a space
            if self.point_durability <= 0:
                paper.text += ' '
                break

            paper.text += letter

            # Don't degrade the pencil if the letter is a specified whitespace
            if letter == ' ' or letter == '\n':
                continue

            if letter.isupper():
                self.point_durability -= 2
            else:
                self.point_durability -= 1

    def sharpen(self):
        if self.length <= 0:
            return

        self.point_durability = self.start_point_durability
        self.length -= 1

    def erase(self, paper, string_to_erase):
        # Simple check to make sure that the string_to_erase is in paper.text
        if paper.text.find(string_to_erase) == -1:
            return

        paper_text_pieces = paper.text.rsplit(string_to_erase, 1)
        refactored_string = paper_text_pieces[0]

        erased_characters = ''
        for letter in string_to_erase[::-1]:

            # If the eraser durability is 0 or the letter is a whitespace, write the letter and continue
            if self.eraser_durability <= 0 or letter.isspace():
                erased_characters = letter + erased_characters
                continue

            erased_characters = " " + erased_characters
            self.eraser_durability -= 1

        refactored_string += erased_characters

        if len(paper_text_pieces) > 1:
            refactored_string += paper_text_pieces[1]

        paper.text = refactored_string

    def edit(self, paper, string_to_insert):
        match = re.search(r'\W\W+', paper.text)

        # Make sure that something has previously been erased before we allow any editing
        if not match:
            return

        # Get the number of spaces we have to write the new word with, taking into account leading and trailing spaces
        space_count = len(match.group(0)) - 2
        paper_text_pieces = re.split(r'\W\W+', paper.text, 1)

        paper.text = paper_text_pieces[0].strip() + ' '

        for letter in string_to_insert:
            self.write(paper, letter)

        if len(string_to_insert) < space_count:
            paper.text += ' ' * (space_count - len(string_to_insert))

        if len(paper_text_pieces) > 1:
            paper.text += ' ' + paper_text_pieces[1].strip()

