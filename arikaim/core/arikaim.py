
from pathlib import Path
import arikaim.core.globals as globals

globals.ARIKAIM_PATH = Path(__file__).parent.absolute()

from arikaim.core.server import ArikaimServer
from arikaim.core.console.app import main

if __name__ == '__main__':  
    main()