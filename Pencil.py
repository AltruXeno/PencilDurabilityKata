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

        # Ensure no spaces are missing if the string_to_insert is shorter than the previously erased string
        for i in range(space_count):
            if len(string_to_insert) > i:
                self.write(paper, string_to_insert[i])
            else:
                paper.text += ' '

        if len(paper_text_pieces) > 1:
            remaining_text = ' ' + paper_text_pieces[1].strip()
            # If we have more letters than spaces allotted
            if len(string_to_insert) > space_count:
                remaining_string = string_to_insert[space_count:]
                # For every remaining letter, check to see if we can write it (there is a space), or there is a
                # conflict (there is already another character there)
                for i in range(len(remaining_string)):
                    if remaining_text[i].isspace():
                        self.write(paper, remaining_string[i])
                    else:
                        self.write(paper, '@')
                paper.text += remaining_text[len(remaining_string):]
            else:
                paper.text += remaining_text

