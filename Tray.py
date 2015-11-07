import copy

class Tray(object):
    def __init__(self, part=None):
        self.part = copy.copy(part)

    def empty(self):
        if self.part == None:
            return True
        return False
