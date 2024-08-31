import os
from arikaim.core.path import Path


def create_storage_path(path: str, mode = 0o666):
    storage_path = Path.storage(path)
    
    if os.path.isdir(storage_path) == False:
        os.mkdir(storage_path,mode) 
        return os.path.isdir(storage_path)
    else:
        return True