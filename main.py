from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(50,50, 100,100)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_right_wall = False
    cell2.draw(100,50, 150,100)

    cell1.draw_move(cell2)

    cell3 = Cell(win)
    cell3.has_left_wall = False
    cell3.has_bottom_wall = False
    cell3.draw(150,50, 200,100)

    cell2.draw_move(cell3)

    cell4 = Cell(win)
    cell4.has_top_wall = False
    cell4.has_left_wall = False
    cell4.draw(150,100, 200,150)

    cell3.draw_move(cell4)

    cell5 = Cell(win)
    cell5.has_right_wall = False
    cell5.has_left_wall = False
    cell5.draw(100,100, 150,150)

    cell4.draw_move(cell5)

    cell6 = Cell(win)
    cell6.has_right_wall = False
    cell6.draw(50,100, 100,150)

    cell5.draw_move(cell6, True)

    win.wait_for_close()



main()

