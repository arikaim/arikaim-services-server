
from pathlib import Path
import core.globals as globals

globals.ARIKAIM_PATH = Path(__file__).parent.absolute()

from core.server import ArikaimServer
from core.console.app import main

#def main():
    #run_console_app(ArikaimServer.app().version)

if __name__ == '__main__':  
    main()