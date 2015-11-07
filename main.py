import Ply
import Part
import ShelfTrollley
import Tray

if __name__ == '__main__':

    # define plys
    ply0 = Ply.Ply(0, 600, 50)
    ply90 = Ply.Ply(90, 300, 52)
    ply45 = Ply.Ply(45, 150, 136)
    plyM45 = Ply.Ply(-45, 150, 136)

    # define a part
    part1 = Part.Part()

    # add plylist to part
    plyList = [ply45, plyM45] + 8 * [ply90] +  [plyM45, ply45]
    part1.addPly(plyList)

    # put part on tray
    tray1 = Tray.Tray(part1)

    # generating a ShelfTrolley
    shelfTrolley1 = ShelfTrollley.Shelftrolley(tray1)

    shelfTrolley1.shelfs[0].part.getNextPly().placed = True
    print(shelfTrolley1.shelfs[0].part.getNextPly())
    print()
    print(shelfTrolley1.shelfs[19].part.getNextPly())
    print()
    print(shelfTrolley1.shelfs[0] is shelfTrolley1.shelfs[19])
    print(shelfTrolley1.shelfs[0].part is shelfTrolley1.shelfs[19].part)
