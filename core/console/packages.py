import click
from core.server import ArikaimServer
from core.packages import *

@click.group()
def packages():
    pass

@click.command()
def install():
    # boot server
    ArikaimServer.app().boot_console()
    install_packages(ArikaimServer.app())

packages.add_command(install)