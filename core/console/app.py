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
def cli(service_name: str):
    # boot server   
    ArikaimServer.app().boot_console(service_name)
    print(service_name)


main.add_command(run)
main.add_command(cli)
main.add_command(packages)
main.add_command(config)