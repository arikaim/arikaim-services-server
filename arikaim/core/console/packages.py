import click
from arikaim.core.app import app
from arikaim.core.packages import *

@click.group()
def packages():
    app.system_init()
    pass

@click.command()
def install():
    app.system_init()

    install_packages(app)

packages.add_command(install)