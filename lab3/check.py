from graph import *

def triangle(x, y, c):
    brushColor(c)
    polygon([(x, y), (x, y - 60),
             (x + 100, y), (x,y)])

triangle(100, 100, "red")
triangle(200, 100, "green")
triangle(200, 160, "blue")

run()