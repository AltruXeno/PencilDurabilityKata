

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
        for letter in string_to_erase:
            if self.eraser_durability <= 0:
                refactored_string += letter
                continue

            refactored_string += " "
            self.eraser_durability -= 1

        if len(paper_text_pieces) > 1:
            refactored_string += paper_text_pieces[1]

        paper.text = refactored_string
