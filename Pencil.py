

class Pencil(object):
    def __init__(self, point_durability=100, length=3):
        self.start_point_durability = point_durability
        self.point_durability = point_durability
        self.length = length

    def write(self, paper, string_to_write):

        for letter in string_to_write:
            # If we have no point durability left, simply write a space
            if self.point_durability <= 0:
                paper.text += ' '
                continue

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
        empty_string = ' ' * len(string_to_erase)
        string_position = paper.text.rfind(string_to_erase)

        paper.text = empty_string.join(paper.text.rsplit(string_to_erase, 1))
