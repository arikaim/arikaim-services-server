from rich import print
from rich.prompt import Prompt
import click
from arikaim.core.app import app
from arikaim.core.services import services
from arikaim.core.packages import save_package_descriptor,load_package_descriptor


@click.group(name = 'services')
def services_group():
    pass

@click.command(name = 'enable')
def enable_service():
    print('Enable service')
    print('')
    service_name = get_service_name()
    if service_name == False:
        return
    
    descriptor = load_package_descriptor(service_name)
    descriptor['disabled'] = False
    save_package_descriptor(service_name,descriptor)
    print('[green]Done')
    

@click.command(name = 'disable')
def disable_service():
    print('Disable service')
    print('')
    service_name = get_service_name()
    if service_name == False:
        return
    
    descriptor = load_package_descriptor(service_name)
    descriptor['disabled'] = True
    save_package_descriptor(service_name,descriptor)
    print('[green]Done')
    
def get_service_name():
    service_name = Prompt.ask("Service name")
    if not service_name:
        print('[red]Service name is required')
        return False
    
    services.scan_services()
    if service_name not in services:
        print('[red]Service not exist')
        return False

    return service_name

@click.command(name = 'list')
def list_services():
    services.scan_services()
    print('')
    print('Services list')
   
    for name, item in services.services.items():
        print('')
        print(item["title"], end = " ")
        if item['disabled'] == True:
            print('[red] disabled',end = " ")
        else:
            print('[green] enabled',end = " ")
    
    print('')
    print('')


services_group.add_command(list_services)
services_group.add_command(enable_service)
services_group.add_command(disable_service)