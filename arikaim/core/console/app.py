import click
from rich import print
from rich import pretty
import sys

from arikaim.core.server import arikaim_server
from arikaim.core.services import services
from arikaim.core.app import app
from arikaim.core.console.config import config
from arikaim.core.console.install import install
from arikaim.core.console.packages import packages
from arikaim.core.console.services import services_group
from arikaim.core.console.queue import queue_group
from arikaim.core.logger import logger
from arikaim.core.path import Path

@click.group(invoke_without_command = True)
@click.pass_context
def main(ctx):
    pretty.install()

    print("")
    print("[blue]Arikaim Services Server")
    print("[green]version [white]" + arikaim_server.version)
    print("")

    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help())

@click.command()
@click.argument('mode', required = False)
@click.option('--path', required = False)
def run(mode = None, path = None):
    # run server
    if mode == 'dev':
        mode = True
 
    arikaim_server.run(mode,path)

# load service console commands
def load_services_commands():
    app.system_init()
    services.scan_services()

    for service in services.services:
        logger.info('Service: ' + service + ' load console commands ...')
        app.load_console_commands(service)

@click.command()
def info():
    logger.info('Base Bath ' + Path.base(False)) 
    logger.info('Python Version ' + sys.version) 
   
main.add_command(run)
main.add_command(services_group)
main.add_command(packages)
main.add_command(config)
main.add_command(install)
main.add_command(info)
main.add_command(queue_group)