import click
from rich import print
from arikaim.core.server import ArikaimServer
from arikaim.core.console.config import config
from arikaim.core.console.packages import packages
from arikaim.core.utils import call
from arikaim.core.logger import logger

@click.group()
def main():
    print("")
    print("[blue]Arikaim Services Server")
    print("[green]version [white]" + ArikaimServer.app().version)
    print("")
  

@click.command()
@click.argument('name', required = False)
def run(name = None):
    if name == 'queue':
        # run queue server
        ArikaimServer.app().system_init()
        ArikaimServer.app().run_queue_worker()
    else:  
        # run server
        ArikaimServer.app().boot()
        ArikaimServer.app().run()

@click.command()
@click.argument('service-name')
@click.argument('module-name')
def cli(service_name: str, module_name: str):
    ArikaimServer.app().boot_console()
    logger.info('Service: ' + service_name + ' load console commands ...')
    module = ArikaimServer.app().load_console_commands(service_name,module_name)
    call(module,'main')
  
main.add_command(run)
main.add_command(cli)
main.add_command(packages)
main.add_command(config)