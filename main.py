from window import Window
from maze import Maze

def main():
    win = Window(810, 610)

    maze = Maze(5, 5, 12, 16, 50, 50, win)  
    maze.solve()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()