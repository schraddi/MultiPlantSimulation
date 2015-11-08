class PlacingUnit(object):
    def __init__(self, fiberAreaWeight):
        self.fiberAreaWeight = fiberAreaWeight
        self.occupied = False

    def getTrayFromShelf(self, shelfTrolley):
        tray = shelfTrolley.getNextTray()
        workingTime = 7
        self.workingOn(tray)

    def workingOn(self, tray):
        part = tray.part
        plyToPlace = part.getNextPly()
        if plyToPlace.fiberAreaWeight != self.fiberAreaWeight:
            passOn

    def passOnTray(self, tray, shelfTrolley):
        workingTime = 7



