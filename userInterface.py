
# Palgorithm Fall 2021 project (calender)
from event import Event
from user import User
# welcome_screen() : int
# register_screen() : User
# login_screen() : userid password
# main_manu() : int
# display_schedule(schedule)
# event_manager_screen() : int
# add_event_menu() : Event
# delete_event_menu(schedule) : str
# display_users(List<User>)

class UserInterface:
    def __init__(self):
        pass
        # super().__init__()
        # self.title(" De Anza College Schedule and calender")
        # self.geometry("400x300+200+200")
        # button = tk.Button(self, text="Pie Chart Graph",
        #                    command=lambda: self.graph.getPieGraph()).pack()
        # self.welcome_screen()

    def welcome_screen(self):
        print("============================================================")
        print("       Welcome to DeAnza College student's Calender")
        print("============================================================")
        print('-1: exit\n1: login\n2: register')
        return int(input(''))

    def register_screen(self):
        name = input('Name --> ')
        username = input("Enter username --> ")
        password = input("Enter password --> ")
        return User(name, username, password)


    def login_screen(self):
        return input('Username: '), input('Password: ')
        '''username_found = False
        password_found = False
        # check username
        for username_count in range(4, 0, -1):
            self.username = input("Enter Your Username: ")
            if self.username in self.userpass.keys():
                print("User Found")
                username_found = True
                break
            else:
                print(f"User not found. {username_count - 1} tries remaining")
        # check password
        if username_found:
            for password_count in range(4, 0, -1):
                self.userpassword = input("Enter Your password: ")
                if self.userpass.get(self.username) == self.userpassword:
                    print("Success! You are Logged in to the system")
                    password_found = True
                    break
                else:
                    print(f"Incorrect Password. {password_count - 1} tries remaining")

        if (username_found == True) and (password_found == False):
            print("Your account has been locked.")
            exit(100)'''

    def main_menu(self):
        print('-1: Logout\n1: display schedule\n2: event manager screen')
        return int(input(''))

    def display_schedule(self, schedule):
        print(schedule)

    def event_manager_screen(self):
        print('-1: back\n1: add event\n2: delete event')

    def add_event_menu(self):
        print('---------------Create event---------------')
        return Event(input('name: '), input('day: '), input('start: '), input('end: '))

    def delete_event_menu(self, schedule):
        print('---------------Delete event---------------')
        event = input('name: ')
        for i in schedule.events:
            if i.name == event:
                return i

    # def display_users(self, users:list):
    #     pass

# def main():
#     uif = UserInterface()
#     uif.welcome_screen()
#     userChoice = int(input("Press the number \n 1: Sing up (new account) \n 2: Sing in \n ---> "))
#     while True:
#         if userChoice == 1:
#             uif.register_screen()
#             break
#         elif userChoice == 2:
#             uif.login_screen()
#             break
#         else:
#             print("Please choose number between 1 and 2")
#             userChoice = input("Press the number \n 1: Sing up (new account) \n 2: Sing in \n ---> ")


# if __name__ == "__main__":
#     main()