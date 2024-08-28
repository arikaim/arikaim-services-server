import click
from rich import print
from rich import pretty

from arikaim.core.server import arikaim_server
from arikaim.core.services import services
from arikaim.core.app import app
from arikaim.core.console.config import config
from arikaim.core.console.install import install
from arikaim.core.console.packages import packages
from arikaim.core.logger import logger

@click.group(invoke_without_command = True)
@click.pass_context
def main(ctx):
    pretty.install()

    print("")
    print("[blue]Arikaim Services Server")
    print("[green]version [white]" + arikaim_server.version)
    print("")

    #load_services_commands()
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
        

main.add_command(run)
main.add_command(packages)
main.add_command(config)
main.add_command(install)