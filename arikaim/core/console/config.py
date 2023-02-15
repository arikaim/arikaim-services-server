import click
import os
from rich import print
from arikaim.core.path import Path
from arikaim.core.console.templates .config_file import content

@click.group()
def config():
    pass

@click.command()
def create():
    print('')
    print('Create config file')
    print('')

    file_name = Path.config('config.py')

    if (os.path.exists(file_name) == True):
        print('[red]Config file exist')
        print('')
        return False
    
    with open(file_name,'w') as config_file:  
        config_file.write(content)
          

config.add_command(create)
