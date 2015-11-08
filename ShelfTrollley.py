import copy

class Shelftrolley(object):
    def __init__(self, tray=None, numberOfShefs=20):
        self.shelfs = []
        self.numberOfShelfs = numberOfShefs
        self.fillShelfs(tray)

    def fillShelfs(self, tray):
        if self.empty():
            for shelf in range(self.numberOfShelfs):
                self.shelfs.append(copy.deepcopy(tray))

    def empty(self):
        for tray in self.shelfs:
            if tray is not None:
                return False
        return True

    def getNextTray(self):
        for tray in self.shelfs:
            if not shelf.part.placed:
                return tray
