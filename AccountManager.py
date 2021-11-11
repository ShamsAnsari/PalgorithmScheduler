'''
Created by Shams
Last updated: 11/10/2021
'''
class AccountManager:
    def __init__(self):
        self.users = []
        pass

    def add_user(self, user):
        '''
        Add user to account manager
        '''
        self.users.append(user)
        pass

    def check_credentials(self, userid, password):
        '''
        check if userid and password match. If no one with userid is found, returns false.
        '''
        user = self.get_user(userid)
        return user is not None and user.password == password
        
    def get_user(self, userid):
        '''
        Gets user whose userid matches, if none match, returns None
        '''
        for user in self.users:
            if user.userid == userid:
                return user
        return None
