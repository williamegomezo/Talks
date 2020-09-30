import math


class RoundPeg:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


class SquarePeg:
    def __init__(self, width):
        self.width = width

    def getWidth(self):
        return self.width


class RoundHole:
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def fits(self, peg):
        return self.getRadius() >= peg.getRadius()


class SquarePegAdapter:
    def __init__(self, peg):
        self.peg = peg

    def getRadius(self):
        return self.peg.getWidth() * math.sqrt(2) / 2


hole = RoundHole(5)
rpeg = RoundPeg(5)
small_sqpeg = SquarePeg(5)
large_sqpeg = SquarePeg(10)

if hole.fits(rpeg):
    print(
        f'Rounded peg of radius {rpeg.getRadius()} fits in hole of radius {hole.getRadius()}')
else:
    print(
        f'Rounded peg of radius {rpeg.getRadius()} does not fit in hole of radius {hole.getRadius()}')

try:
    hole.fits(small_sqpeg)
except:
    print('Incompatible types')

small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

if hole.fits(small_sqpeg_adapter):
    print(
        f'Squared peg of radius {small_sqpeg_adapter.getRadius()} fits in hole of radius {hole.getRadius()}')
else:
    print(
        f'Squared peg of radius {small_sqpeg_adapter.getRadius()} does not fit in hole of radius {hole.getRadius()}')

if hole.fits(large_sqpeg_adapter):
    print(
        f'Squared peg of radius {large_sqpeg_adapter.getRadius()} fits in hole of radius {hole.getRadius()}')
else:
    print(
        f'Squared peg of radius {large_sqpeg_adapter.getRadius()} does not fit in hole of radius {hole.getRadius()}')
