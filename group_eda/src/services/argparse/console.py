#---
'''
TODO @leosanchezsoler
'''
#---
import os, sys, argparse
#import server.start_server

#get the relative path to run the file with an import from a parallel directory
directorio = os.path.dirname(__file__)
for i in range(4):
    directorio = os.path.dirname(directorio)
    sys.path.append(directorio)
    print('Dirname\n', directorio)

sys.path.append('../../../../../')
sys.path.append('../../../')
sys.path.append('../../../../')

print(sys.path)
#python -m pkg.api.server
from src.services.api.test1 import give_json
# print(__file__)
# print('os.getcwd():,' ,os.getcwd())
# print(os.path.dirname('...'))
#import the json file that contains the data

'''
# TO RUN:
# RUN ON TERMINAL
#python + absolute-path

# 1
# python or python3
# 2
# route to the file
# 3
# arg(s): introduce the argument(s) and its value
# --help: provides information about the arguments

# 'python' 'route' 'args'
'''
class Console():
    def __init__(self, password=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('-j','--j', type=int, help='the password')
        args = vars(parser.parse_args())

        print('####################\n')
        print(type(args))
        print(args)

        password = args['j']

        if password == 18:
            give_json('Iran', 'Netherlands', 'Spain', 'Brazil', 'Mexico')

        #here goes the function that downloads the json file

        else:
            print('\nIncorrect password.' +
            '\nPlease, check if you have the correct password.' +
            '\nIf the error persists, please contact @RMolleda, @alfonsogarcia-git or @leosanchezsoler.')

        #print('\nThe final data is' + str(data))
        print('\n####################')


Console()