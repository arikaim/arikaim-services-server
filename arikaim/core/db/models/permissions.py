from typing import Optional
from sqlmodel import Field, SQLModel

class Permissions(SQLModel, table = True):
    __tablename__ = 'permissions'

    id: int = Field(unique = True, primary_key = True)
    uuid: str = Field(unique = True)
   
    name: str = Field(unique = True)
    slug: str = Field(unique = True)
    title: str
    extension_name: str
    description: str
    deny: int
