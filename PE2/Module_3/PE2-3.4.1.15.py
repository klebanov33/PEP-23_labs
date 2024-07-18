import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._X1 = x
        self._Y1 = y

    def getx(self):
        return self._X1

    def gety(self):
        return self._Y1

    def distance_from_xy(self, x, y):
        self._X2 = x
        self._Y2 = y

        self._culc_X = self._X1 - self._X2
        self._culc_Y = self._Y1 - self._Y2
        self._dist_xy = math.hypot(self._culc_X, self._culc_Y)
        return self._dist_xy

    def distance_from_point(self, point):
        self._Ax = point.getx()
        self._Ay = point.gety()

        self._culc_X = self._X1 - self._Ax
        self._culc_Y = self._Y1 - self._Ay
        self._dist_point = math.hypot(self._culc_X, self._culc_Y)
        return self._dist_point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__obj1 = vertice1
        self.__obj2 = vertice2
        self.__obj3 = vertice3
        self.__lst_point = [Point.getx(vertice1), Point.gety(vertice1), Point.getx(vertice2), Point.gety(vertice2), Point.getx(vertice3), Point.gety(vertice3)]

    def perimeter(self):
        self.Perim = self.__obj1.distance_from_point(self.__obj2) + self.__obj2.distance_from_point(self.__obj3) + self.__obj1.distance_from_point(self.__obj3)
        return self.Perim

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

