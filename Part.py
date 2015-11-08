import copy

class Part(object):
    def __init__(self):
        self.plys = []
        self.placed = False

    def getNextPly(self):
        if self.placed:
            return None
        for ply in self.plys:
            if not ply.placed:
                return ply

    def addPly(self, plyList):
        for ply in plyList:
            self.plys.append(copy.deepcopy(ply))
