import click
import os
from rich import print
from arikaim.core.path import Path


@click.command()
def install():
    print('')
    print('Install ')
    print('')
    print('Create folders ')

    folders = [
        'arikaim',
        'arikaim/config',
        'arikaim/storage',
        'arikaim/services'
    ]

    for item in folders:
        if (os.path.exists(item) == False):
            print(item)

    print('[green]Done.')
    print('')