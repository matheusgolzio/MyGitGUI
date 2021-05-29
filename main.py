from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

main_window = Tk()


class System():
    def verificationRepo(self):
        self.is_started = open("config/is_started.txt", "r")
        self.content = self.is_started.readlines()
        for self.line in self.content:
            if self.line == f"Diretorio: {self.path} | Inicado: Sim":
                self.gitadd["state"] = NORMAL
                self.gitcommit["state"] = NORMAL
                self.gitstatus["state"] = NORMAL
                self.gitlog["state"] = NORMAL
                self.addremote["state"] = NORMAL
                self.is_started.close()
            
            else:
                self.gitinit["state"] = NORMAL
                self.is_started.close()
    

    def verificationRemote(self):
        self.is_radded = open("config/is_radded.txt", "r")
        self.content_radded = self.is_radded.readlines()
        for self.line_radded in self.content_radded:
            if self.line_radded == f"Repositorio local: {self.path} | Repo remoto adicionado: Sim":
                self.gitpull["state"] = NORMAL
                self.gitpush["state"] = NORMAL
                self.is_radded.close()

            else:
                self.is_radded.close()


    def startRepo(self):
        try:
            os.system(f"cd {self.path} && git init")
        except:
            messagebox.showerror(title="Error", message="Não pude inciar repositório local")
        else:
            messagebox.showinfo(title="Inciado", message="Repositório local inciado!")
            self.is_started = open("config/is_started.txt", "w")
            self.is_started.write(f"Diretório: {self.path} | Inicado: Sim")
            self.is_started.close()

        self.gitadd["state"] = NORMAL
        self.gitcommit["state"] = NORMAL
        self.gitstatus["state"] = NORMAL
        self.gitlog["state"] = NORMAL
        self.addremote["state"] = NORMAL
    
    
    def showStatus(self):
        os.system(f"cd {self.path} && git status")
    

    def gitAdd(self):
        os.system(f"cd {self.path} && git add .")
        messagebox.showinfo(title="Adicionado", message="Todas as alterações foram adicionadas!")
    

    def gitCommit(self):
        self.commit_window = Toplevel()
        self.commit_window.title("Commit")
        self.commit_window.geometry("300x200")

        # Widgets
        self.message_c_label = Label(self.commit_window, text="Mensagem", font=("Verdana", 20))
        self.message_c_label.pack(side=TOP)

        
        self.message_commit = Entry(self.commit_window, relief=FLAT)
        self.message_commit.pack(side=TOP, ipadx=80, ipady=20)

        self.commit_ok = Button(self.commit_window, text="Ok", relief=FLAT, bg="#F05030", fg="white", command=self.commit)
        self.commit_ok.pack(side=LEFT, padx=50)

        self.commit_cancel = Button(self.commit_window, text="Cancelar", relief=FLAT, bg="#F05030", fg="white", command=lambda :self.commit_window.destroy())
        self.commit_cancel.pack(side=RIGHT, padx=40)
    
    def commit(self):
        os.system(f'cd {self.path} && git commit -m "{self.message_commit.get()}"')
        messagebox.showinfo(title="Commit Realizado", message="Todas as alterações foram commitadas, você poderá ver todas depois!")
        self.commit_window.destroy()
    

    def gitLog(self):
        os.system(f"cd {self.path} && git log")
    

    def infoRemote(self):
        self.remote_window = Toplevel()
        self.remote_window.title("Adicionar Repositório Remoto")
        self.remote_window.geometry("300x200")

        # Widgets
        self.url_r_label = Label(self.remote_window, text="URL", font=("Verdana", 20))
        self.url_r_label.pack(side=TOP)

        
        self.url_remote = Entry(self.remote_window, relief=FLAT)
        self.url_remote.pack(side=TOP, ipadx=80, ipady=20)

        self.remote_ok = Button(self.remote_window, text="Ok", relief=FLAT, bg="#F05030", fg="white", command=self.addRemote)
        self.remote_ok.pack(side=LEFT, padx=50)

        self.remote_cancel = Button(self.remote_window, text="Cancelar", relief=FLAT, bg="#F05030", fg="white", command=lambda :self.remote_window.destroy())
        self.remote_cancel.pack(side=RIGHT, padx=40)
    

    def addRemote(self):
        os.system(f"cd {self.path} && git remote add origin {self.url_remote.get()}.git")
        self.is_radded = open("config/is_radded.txt", "w")
        self.is_radded.write(f"Repositorio local: {self.path} | Repo remoto adicionado: Sim")
        self.is_radded.close()
        messagebox.showinfo(title="Adicionado", message="Repositório local adicionado com sucesso!")
    

    def gitPushWin(self):
        self.push_window = Toplevel()
        self.push_window.title("Enviar arquivos")
        self.push_window.geometry("300x200")

        # Widgets
        self.branch_r_label = Label(self.push_window, text="Branch", font=("Verdana", 20))
        self.branch_r_label.pack(side=TOP)

        self.branch_remote = Entry(self.push_window, relief=FLAT)
        self.branch_remote.pack(side=TOP, ipadx=80, ipady=20)

        self.push_ok = Button(self.push_window, text="Ok", relief=FLAT,bg="#F05030", fg="white", command=self.addRemote)
        self.push_ok.pack(side=LEFT, padx=50)

        self.push_cancel = Button(self.push_window, text="Cancelar", relief=FLAT,bg="#F05030", fg="white", command=lambda: self.push_window.destroy())
        self.push_cancel.pack(side=RIGHT, padx=40)
    

    def gitPush(self):
        os.system(f"cd {self.path} && git push -u origin {self.branch_remote.get()}")
        messagebox.showinfo(title="Arquivos Enviados", message="Os arquivos foram enviados para o repositório com sucesso!")
    

    def gitPullWin(self):
        self.pull_window = Toplevel()
        self.pull_window.title("Coletar Arquivos")
        self.pull_window.geometry("300x200")

        # Widgets
        self.branch_p_label = Label(self.pull_window, text="Branch", font=("Verdana", 20))
        self.branch_p_label.pack(side=TOP)

        self.branch_pull = Entry(self.pull_window, relief=FLAT)
        self.branch_pull.pack(side=TOP, ipadx=80, ipady=20)

        self.pull_ok = Button(self.pull_window, text="Ok", relief=FLAT,bg="#F05030", fg="white", command=self.gitPull)
        self.pull_ok.pack(side=LEFT, padx=50)

        self.pull_cancel = Button(self.pull_window, text="Cancelar", relief=FLAT,bg="#F05030", fg="white", command=lambda: self.pull_window.destroy())
        self.pull_cancel.pack(side=RIGHT, padx=40)
    

    def gitPull(self):
        os.system(f"cd {self.path} && git pull origin {self.branch_pull.get()}")
        messagebox.showinfo(title="Arquivos Coletados", message="Os arquivos foram coletados do repositório com sucesso!")


class Application(System):
    def __init__(self):
        self.main_window = main_window
        self.screen_mw()
        main_window.mainloop()


    def ask_dir(self):
        self.path = filedialog.askdirectory()
        self.dir["text"] = self.path
        self.verificationRepo()
        self.verificationRemote()

    
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

        self.add_dir = Button(self.main_window, text="Adicionar diretório", relief=FLAT, bg="#F05030", bd=2, fg="white", command=self.ask_dir)
        self.add_dir.place(relx=0.39, rely=0.3)

        self.dir = Label(self.main_window, text="Diretório não selecionado", bg="#d3d3d3", font=("Verdana", 15), fg="#3F2C00")
        self.dir.pack(side=TOP, pady=120)

        # Repository Control
        self.gitinit = Button(self.main_window, text="Inciar diretório", bg="#F05030", relief=FLAT, fg="white", state=DISABLED, command=self.startRepo)
        self.gitinit.place(relx=0.1, rely=0.55)

        self.addremote = Button(self.main_window, text="Adicionar diretório remoto", bg="#F05030", relief=FLAT, fg="white", state=DISABLED)
        self.addremote.place(relx=0.3, rely=0.55)

        self.gitadd = Button(self.main_window, text="Adicionar alterações", bg="#F05030", relief=FLAT, fg="white",state=DISABLED, command=self.gitAdd)
        self.gitadd.place(relx=0.63, rely=0.55)

        self.gitcommit = Button(self.main_window, text="Commitar mudanças", bg="#F05030", relief=FLAT, fg="white",state=DISABLED, command=self.gitCommit)
        self.gitcommit.place(relx=0.1, rely=0.68)

        self.gitlog = Button(self.main_window, text="Ver todos os commits", bg="#F05030", relief=FLAT, state=DISABLED, fg="white", command=self.gitLog)
        self.gitlog.place(relx=0.37, rely=0.68)

        self.gitpull = Button(self.main_window, text="Puxar arquivos", bg="#F05030", relief=FLAT, fg="white",state=DISABLED)
        self.gitpull.place(relx=0.65, rely=0.68)

        self.gitpush = Button(self.main_window, text="Enviar arquivos", bg="#F05030", relief=FLAT, fg="white",state=DISABLED)
        self.gitpush.place(relx=0.1, rely=0.8)

        self.gitstatus = Button(self.main_window, text="Status", bg="#F05030", relief=FLAT, fg="white",state=DISABLED, command=self.showStatus)
        self.gitstatus.place(relx=0.3, rely=0.8)


Application()
