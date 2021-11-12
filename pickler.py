import os
import pickle

class Pickler:
    def __init__(self):
        self.path = os.getcwd()

    def save(self, account_manager):
        pickle.dump(account_manager, open("acc.pickle", "wb"))

    def load(self):
        try:
            file = pickle.load(open( "acc.pickle", "rb" ))
            return file
        except FileNotFoundError:
            print("File does not exist in the CWD")
    
    def doesFileExist(self):
        try:
            pickle.load(open( "acc.pickle", "rb" ))
            return True
        except FileNotFoundError:
            return False
        
