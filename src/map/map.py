import os


class Map:
    def __init__(self, filename, tilesize):
        self.data = []
        with open(os.path.join(filename), "rt") as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * tilesize
        self.height = self.tileheight * tilesize
