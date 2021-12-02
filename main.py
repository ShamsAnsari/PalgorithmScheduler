import tkinter as tk
import tkinter.ttk
from pickler import Pickler
from AccountManager import AccountManager
from user import User
from event import Event
# from (python file name) import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.userID, self.password = tk.StringVar(), tk.StringVar()
        self.title("De Anza College Scheduler")
        self.geometry("500x500+300+200")

        #self.p = Pickler() #create pickler
        #self.user = None
        #if self.p.file_exists:
        #    self.am = self.p.load() #load account manager
        #else:
        self.am = AccountManager()

        self.frame = None
        self.welcome_screen()

    def welcome_screen(self):
        frame = tk.Frame(self)
        tk.Label(frame,
                 text="Welcome to the De Anza College Scheduler!\n").pack()

        tk.Button(frame, text='Login', command=self.login).pack()
        tk.Button(frame, text='Register', command=self.register).pack()
        tk.Button(frame, text='Exit', command=exit).pack()
        self.change_frame(frame)

    def register(self):
        frame = tk.Frame(self)

        reg = dict()
        tk.Label(frame, text="WELCOME TO REGISTER PAGE\n - please enter your preferred Name, ID, and PASSWORD")
        tk.Label(frame, text="Name: ").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(frame, text="Username: ").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(frame, text="Password: ").grid(row=2, column=0, padx=10, pady=10)
        
        reg['name'] = tk.Entry(frame)
        reg['name'].grid(row=0, column=1, padx=10, pady=10)
        reg['user'] = tk.Entry(frame)
        reg['user'].grid(row=1, column=1, padx=10, pady=10)
        reg['pass'] = tk.Entry(frame)
        reg['pass'].grid(row=2, column=1, padx=10, pady=10)

        command = lambda: self.reg_callback(reg)
        self.bind('<Return>', command)
        tk.Button(frame, text="REGISTER", command=command).grid(row=3, column=1, padx=10, pady=10)

        self.change_frame(frame)
    
    def reg_callback(self, reg):
        self.user = User(reg['name'].get(), reg['user'].get(), reg['pass'].get())
        self.am.add_user(self.user)
        self.main_menu()
        

    def log_callback(self, log):
        frame = tk.Frame(self)
        frame.pack()
        id, pwd = log['user'].get(), log['pass'].get()
        if self.am.check_credentials(id, pwd):
            self.user = self.am.get_user(id, pwd)
            self.main_menu()
        else:
            tk.Label(frame, text="Please re-check your user ID/ Password").pack()

    def login(self):
        frame = tk.Frame(self)
        log = dict()
        tk.Label(frame, text="Username: ").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(frame, text="Password: ").grid(row=1, column=0, padx=10, pady=10)
        log['user'] = tk.Entry(frame)
        log['user'].grid(row=0, column=1, padx=10, pady=10)
        log['pass'] = tk.Entry(frame, show='*')
        log['pass'].grid(row=1, column=1, padx=10, pady=10)

        command = lambda: self.log_callback(log)
        self.bind('<Return>', command)
        tk.Button(frame, text="Login", command=command).grid(row=2, column=1, padx=10, pady=10)

        self.change_frame(frame)

    def main_menu(self):
        frame = tk.Frame(self)
        tk.Label(frame,
                  text="Welcome to the De Anza College Scheduler!\n").pack()
        tk.Button(frame,
                  text="ADD the schedule",
                  command=self.add_schedule).pack()
        tk.Button(frame,
                  text="DELETE the schedule",
                  command=self.delete_schedule).pack()
        tk.Button(frame,
                  text="DISPLAY the schedule",
                  command=self.display_schedule).pack()
        tk.Button(frame, text="Logout", command=self.logout).pack()
        self.change_frame(frame)
    
    def logout(self):
        self.p.save(self.am)
        self.welcome_screen()

    def add_schedule(self):
        frame = tk.Frame(self)
        
        add = dict()
        add['name'] = tk.Entry(frame, text='name')
        add['day'] = tk.Entry(frame, text='day')
        add['start'] = tk.Entry(frame, text='start')
        add['end'] = tk.Entry(frame, text='end')
        add['description'] = tk.Entry(frame, text='description')

        for i in add.values():
            i.pack()
        
        command = lambda : self.schedule_callback(add)
        self.bind('<Return>', command)
        tk.Button(frame, text="Add", command=command).pack()
        tk.Button(frame, text="Back to main", command=self.main_menu).pack()
        self.change_frame(frame)
        print("ADDED SOMETHING")
    
    def schedule_callback(self, add):
        event = Event(add['name'], add['day'], add['start'], add['end'], add['description'])
        self.user.schedule.add_event(event)
        self.main_menu()

    def delete_schedule(self):
        frame = tk.Frame(self)
        entry = tk.Entry(frame)
        entry.pack()
        command = lambda: self.delete_callback(entry, frame)
        self.bind('<Return>', command)
        tk.Button(frame, text="Delete", command=command).pack()
        tk.Button(frame, text="Back to main", command=self.main_menu).pack()
        self.change_frame(frame)
        print("DELETED SOMETHING")

    def delete_callback(self, entry, frame):
        name = entry.get()
        for i in self.user.schedule.events:
            if name.lower() == i.name.lower():
                self.user.schedule.delete_event(i)
                self.main_menu()
        tk.Label(frame, text='Could not find event').pack()

    def display_schedule(self):
        frame = tk.Frame(self)
        tk.Label(frame, text="--------------User Schedule--------------")
        
        # lbl = tkinter.Label(frame, text="-----Weekly Schedule-----")
        # lbl.pack()
        # treeview = tkinter.ttk.Treeview(root, columns=["one", "two","three","four","five","six", "seven"], displaycolumns=["one","two","three","four","five","six", "seven"])
        # treeview.pack()

        # treeview.column("#0", width=100,)
        # treeview.heading("#0", text="index")

        # treeview.column("#1", width=100, anchor="center")
        # treeview.heading("one", text="Sunday", anchor="center")

        # treeview.column("#2", width=100, anchor="center")
        # treeview.heading("two", text="Monday", anchor="center")

        # treeview.column("#3", width=100, anchor="center")
        # treeview.heading("three", text="Tuesday", anchor="center") 

        # treeview.column("#4", width=100, anchor="center")
        # treeview.heading("four", text="Wednesday", anchor="center")

        # treeview.column("#5", width=100, anchor="center")
        # treeview.heading("five", text="Thursday", anchor="center")

        # treeview.column("#6", width=100, anchor="center")
        # treeview.heading("six", text="Friday", anchor="center")
        
        # treeview.column("#7", width=100, anchor="center")
        # treeview.heading("seven", text="Saturday", anchor="center")

        # treelist = [("math", 1,1,1,1,1,1), ("math", 1,1,1,1,1,1),("math", 1,1,1,1,1,1),("math", 1,1,1,1,1,1),("math", 1,1,1,1,1,1)] #schedule list data

        # for i in range(len(treelist)):
        #   treeview.insert('', 'end', text=i, values=treelist[i], iid=str(i))
          
        tk.Label(frame, text=str(self.user.schedule)).pack()
        tk.Button(frame, text="Back to main", command=self.main_menu).pack()
        self.change_frame(frame)
        print("DISPLAY SOMETHING")
        # frame.bind(self, exitButton)

    def change_frame(self, frame):
        if self.frame:
            self.frame.pack_forget()
            self.frame.destroy()
        frame.pack()
        self.frame = frame


def main():
    print("it worked")
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    main()
