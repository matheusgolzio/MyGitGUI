from tkinter import *


main_window = Tk()


class Application:
    def __init__(self):
        self.main_window = main_window
        self.screen()
        main_window.mainloop()

    
    # The configurations of the main window
    def screen(self):
        self.main_window.title("Git GUI")
        self.main_window.resizable(False, False)
        self.main_window.configure(background="#d3d3d3")
        self.main_window.geometry('500x300')


Application()
