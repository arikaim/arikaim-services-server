import click
from rich import print
from core.server import ArikaimServer
from core.console.config import config
from core.console.packages import packages


@click.group()
def main():
    print("")
    print("[blue]Arikaim Services Server")
    print("[green]version [white]" + ArikaimServer.app().version)
    print("")
  

@click.command()
def run():
    # boot server
    ArikaimServer.app().boot()
    # run server
    ArikaimServer.app().run()


@click.command()
@click.argument('service-name')
@click.argument('module-name')
def cli(service_name: str, module_name: str):
    module = ArikaimServer.app().load_service_console_commands(service_name,module_name)
    main.add_command(module.commands)
    module.main()

main.add_command(run)
main.add_command(cli)
main.add_command(packages)
main.add_command(config)