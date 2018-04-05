
class Pencil(object):
    def __init__(self):
        self.point_durability = 1000

    def write(self, paper, string_to_write):

        for letter in string_to_write:
            paper.text += letter
            self.point_durability -= 1
