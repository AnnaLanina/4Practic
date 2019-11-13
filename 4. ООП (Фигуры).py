class Figure():
    def __init__(self, perimeter=None, space=None):
        self.perimeter = perimeter
        self.space = space
        self.infoFig = []

    def calcPerimeter(self):
        pass

    def calcSpace(srlf):
        pass

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('периметр = %s площадь = %s' % (p, s))


class Rectangle(Figure):
    def __init__(self, x, y, w, h):
        Figure.__init__(self)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def calcPerimeter(self):
        perimeter = self.w * 2 + self.h * 2
        return perimeter

    def calcSpace(self):
        space = self.x * self.y
        return space

    def figInfo(self):
        p = self.calcPerimeter()
        s = self.calcSpace()
        print('У прямоугольника периметр = %s площадь = %s' % (p, s))


if __name__ == '__main__':
    fig1 = Rectangle(5, 5, 10, 10)
    fig2 = Rectangle(-3, -4, 5, 7)
    array = [fig1, fig2]
    for f in array:
        f.figInfo()
Zen26, Для
круга
и
треугольника
попробуйте
сами
написать
по
а