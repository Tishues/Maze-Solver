from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(win)
    cell.draw(150,200, 200,250)
    cell = Cell(win)
    cell.draw(200,200, 250,250)
    cell = Cell(win)
    cell.draw(250,200, 300,250)
    cell = Cell(win)
    cell.draw(200,150, 250,200)
    cell = Cell(win)
    cell.draw(200,250, 250,300)
    cell = Cell(win)
    cell.draw(200,300, 250,350)
    cell = Cell(win)
    cell.draw(100,100, 350,400)
    cell = Cell(win)
    #l = Line(Point(50, 50), Point(400,400))
    #win.draw_line(l, "black")
    win.wait_for_close()



main()

