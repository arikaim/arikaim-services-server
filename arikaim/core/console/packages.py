import click
from arikaim.core.app import app
from arikaim.core.packages import *

@click.group()
def packages():
    pass

@click.command()
def install():
    # boot server
    app.boot_console()
    install_packages(app)

packages.add_command(install)