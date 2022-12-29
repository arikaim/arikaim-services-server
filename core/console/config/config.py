import typer
import os
from rich import print
from core.path import Path
from core.console.templates .config_file import content

config_commands = typer.Typer()

@config_commands.command('create')
def config_create():
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
          