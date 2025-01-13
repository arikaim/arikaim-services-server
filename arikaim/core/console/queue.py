import click
from rich import print
from arikaim.core.path import Path
from arikaim.core.console.templates.config_file import content
from arikaim.core.app import app
from arikaim.core.queue.queue import queue
from arikaim.core.services import services

@click.group(name = 'queue')
def queue_group():
    pass

@click.command()
def run():
    app.system_init()
    services.scan_services()
   
    queue.run()

@click.command()
def jobs():
   
    print(queue.jobs)

queue_group.add_command(run)
queue_group.add_command(jobs)