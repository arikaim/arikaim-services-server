from typing import Optional
from sqlmodel import Field, SQLModel, select

class Drivers(SQLModel, table = True):
    __tablename__ = 'drivers'

    id: int = Field(unique = True, primary_key = True)
    uuid: str = Field(unique = True)
    name: str = Field(unique = True)
    title: str
    description: str
    version: str
    config: str
   
    @staticmethod
    def get_config(session, name):
        stm = select(Drivers).where(Drivers.name == name)
        model = session.exec(stm).first()
        
        if not model:
            return None
        else:    
            return model.config
