import argparse
#from pickler import Pickler

class Runner:
    def __init__(self, args):
        pass
    
    def main_loop():



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='College Scheduler')
    parser.add_argument('--no_gui', '-ng', type=bool, default=False, help='run without gui')
    parser.add_argument('--user', '-u', type=str, default='default', help='username')
    args = parser.parse_args()
    r = Runner(args)
    r.main_loop()