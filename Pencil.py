
class Pencil(object):
    def __init__(self):
        self.point_durability = 1000

    def write(self, paper, string_to_write):

        for letter in string_to_write:
            paper.text += letter

            # Don't degrade the pencil if the letter is a specified whitespace
            if letter == ' ' or letter == '\n':
                continue

            if letter.isupper():
                self.point_durability -= 2
            else:
                self.point_durability -= 1
