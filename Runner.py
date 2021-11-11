import argparse
from pickler import Pickler
from AccountManager import AccountManager
from UserInterface import welcome_screen, login_screen, main_menu, display_schedule, event_manager_screen, add_event_menu, delete_event_menu, register_screen
from User import User

class Runner:
    def __init__(self, args):
        self.args = args
        p = Pickler() #create pickler
        if p.file_exists:
            self.am = p.load() #load account manager
        else:
            self.am = AccountManager()
    
    def main_loop(self):
        id, pwd = self.args.user, self.args.pwd
        user = None
        if not self.args.no_gui: #command line logic
            if self.args.exists: #account exists
                if not self.am.check_credentials(id, pwd): #account doesn't exist
                    raise ValueError('no_gui. Wrong id/password!!')
            else:
                #make new user
                user = User(self.args.name,
                            id,
                            pwd)
        else:
            while True:
                exists = welcome_screen() #1 for login, 2 for register
                if exists == 1:
                    id, pwd = login_screen()
                    if self.am.check_credentials(id, pwd):
                        break
                    continue
                elif exists == 2:
                    user = register_screen()
                    break
                else:
                    raise ValueError('welcome screen returned wrong values')
        
        if user:
            self.am.add_user(user)
        user = self.am.get_user(id, pwd)
        while item := main_menu() != -1:
            options = {1 : lambda x : display_schedule(x.schedule),
                       2 : self.emloop} #general options
            options[item](user)
        p.save(self.am)
    
    def emloop(user):
        emoptions = {1 : lambda x : x.add_event(add_event_menu()),
                     2 : lambda x : delete_event_menu(x.schedule)} #event manager options #delete should return event obj not a string?
        while item := event_manager_screen(user.schedule) != -1:
            emoptions[item]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='College Scheduler')
    parser.add_argument('--no_gui', '-ng', type=bool, default=False, help='run without gui')
    parser.add_argument('--exists', '-e', type=bool, default=True, help='flag to register account')
    parser.add_argument('--name', '-u', type=str, default=None, help='person name, only required on account creation')
    parser.add_argument('--user', '-u', type=str, default=None, help='username')
    parser.add_argument('--pwd', '-p', type=str, default=None, help='password')
    args = parser.parse_args()
    r = Runner(args)
    r.main_loop()