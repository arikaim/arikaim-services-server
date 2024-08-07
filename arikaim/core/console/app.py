import click
from rich import print
from rich import pretty

from arikaim.core.server import arikaim_server
from arikaim.core.app import app
from arikaim.core.console.config import config
from arikaim.core.console.install import install
from arikaim.core.console.packages import packages
from arikaim.core.utils import call
from arikaim.core.logger import logger

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

@click.command()
@click.pass_context
@click.argument('service-name', required = False)
@click.argument('module-name', required = False)
def cli(ctx, service_name: str, module_name: str):
    app.system_init()

    if not service_name:
        app.scan_services()
        for service in app.services:
            logger.info('Service: ' + service + ' load console commands ...')
            app.load_console_commands(service)
        
        click.echo(ctx.get_help())
    else:
        logger.info('Service: ' + service_name + ' load console commands ...')
        module = app.load_console_commands(service_name,module_name)
        call(module,'main')
  
main.add_command(run)
main.add_command(cli)
main.add_command(packages)
main.add_command(config)
main.add_command(install)