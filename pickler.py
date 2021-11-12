import os
import pickle

from AccountManager import *

class Pickler:
    def __init__(self):
        self.file_exists = self.doesFileExist()
        self.path = os.getcwd()

    def save(self, account_manager):
        pickle.dump(account_manager, open("acc.pickle", "wb"))

    def load(self):
        if self.doesFileExist():
            return pickle.load(open( "acc.pickle", "rb" ))
        return AccountManager()
    
    def doesFileExist(self):
        try:
            pickle.load(open( "acc.pickle", "rb" ))
            return True
        except FileNotFoundError:
            return False
        
