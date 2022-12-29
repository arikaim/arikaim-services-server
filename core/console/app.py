import typer
from rich import print
from core.server import ArikaimServer
from core.console.config.config import *
from core.container import di

# console app commands
console = typer.Typer(no_args_is_help = True)
# add config commands
console.add_typer(config_commands, name = 'config')

di.add('console',console)

def run_console_app(version):
    print("")
    print("[blue]Arikaim Services Server")
    print("[green]version [white]" + version)
    print("")
    console()

@console.command('run')
def run():
    # boot server
    ArikaimServer.app().boot()
    # run server
    ArikaimServer.app().run()


@console.command()
def cli():
    # boot server
    ArikaimServer.app().boot_console()

    for group in di.get('console').registered_groups:
        print(group.name)
        
    for cmd in di.get('console').registered_commands:
        print(cmd.cls)
        #print(di.get('console').registered_commands)

   # di.get('console').run('text_rank')

    while exit is not False:
        command = typer.prompt("")
        t = di.get('console')
        group = di.get('console').get_group_from_info(command)
        print(group)