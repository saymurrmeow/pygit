# manage data in pygit direcory
import os

GIT_DIR = '.pygit'

def init(_):
    try: 
        pygit_dir = f'{os.getcwd()}/{GIT_DIR}'
        os.makedirs(GIT_DIR)
        os.makedirs(f'{GIT_DIR}/objects')
        print('Initialize empty git repositoty in ', pygit_dir) 

    except FileExistsError: 
        print('repository is non empty') 
