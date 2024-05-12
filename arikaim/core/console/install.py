import click
import os
from rich import print
from arikaim.core.path import Path
from arikaim.core.container import di
from arikaim.core.db.db import load_model_class
from arikaim.core.app import app

@click.command()
def install():
    app.system_init()

    print('')
    print('Install ')
    print('')
    print('Create folders ')

    folders = [
        'config',
        'storage',
        'services'
    ]

    for item in folders:
        path = os.path.join(Path.arikaim(),item)

        if (os.path.exists(path) == False):
            os.mkdir(path) 
            print('Create path [green]' + path)

    print('[green]Done.')
    print('')

    print('Create db tables ')
    Users = load_model_class('Users','users')

    di.get('db').peewee.create_table(Users)
