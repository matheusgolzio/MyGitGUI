from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


main_window = Tk()


class System():
    def startRepo(self):
        os.system(f"cd {self.path}")
        os.system("git init")
        messagebox.showinfo(title="Started", message="The local repository was successfully created!")


class Application(System):
    def __init__(self):
        self.main_window = main_window
        self.screen_mw()
        main_window.mainloop()


    def ask_dir(self):
        self.path = filedialog.askdirectory()
        self.dir["text"] = self.path
        self.gitinit["state"] = NORMAL

    
    # Main window
    def screen_mw(self):
        # Screen configurations
        self.main_window.title("Git GUI")
        self.main_window.resizable(False, False)
        self.main_window.configure(background="#d3d3d3")
        self.main_window.geometry('500x300')

        # Widgets
        self.title = Label(self.main_window, text="GIT GUI", fg="#3F2C00", bg="#d3d3d3", font=("Verdana", 26))
        self.title.place(relx=0.35, rely=0.06)

        self.add_dir = Button(self.main_window, text="Add Directory", relief=FLAT, bg="#F05030", bd=2, fg="white", command=self.ask_dir)
        self.add_dir.place(relx=0.41, rely=0.3)

        self.dir = Label(self.main_window, text="No path selected", bg="#d3d3d3", font=("Verdana", 15), fg="#3F2C00")
        self.dir.pack(side=TOP, pady=120)

        # Repository Control
        self.gitinit = Button(self.main_window, text="Start Local Repository", bg="#F05030", relief=FLAT, fg="white", state=DISABLED, command=self.startRepo)
        self.gitinit.place(relx=0.1, rely=0.55)

        self.addremote = Button(self.main_window, text="Add Remote Repository", bg="#F05030", relief=FLAT, fg="white", state=DISABLED)
        self.addremote.place(relx=0.37, rely=0.55)

        self.gitadd = Button(self.main_window, text="Git Add Changes", bg="#F05030", relief=FLAT, fg="white",state=DISABLED)
        self.gitadd.place(relx=0.66, rely=0.55)

        self.gitlog = Button(self.main_window, text="See all commits", bg="#F05030", relief=FLAT, state=DISABLED)
        self.gitlog.place(relx=0.1, rely=0.68)

        self.gitpull = Button(self.main_window, text="Pull files", bg="#F05030", relief=FLAT, fg="white",state=DISABLED)
        self.gitpull.place(relx=0.3, rely=0.68)

        self.gitpush = Button(self.main_window, text="Push files", bg="#F05030", relief=FLAT, fg="white",state=DISABLED)
        self.gitpush.place(relx=0.43, rely=0.68)


Application()
