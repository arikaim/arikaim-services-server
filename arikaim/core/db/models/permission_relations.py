from typing import Optional
from sqlmodel import Field, SQLModel

class PermissionRelations(SQLModel, table = True):
    __tablename__ = 'permission_relations'

    id: int = Field(unique = True, primary_key = True)
    uuid: str = Field(unique = True)
    read: int
    write: int
    delete: int
    execute: int
    permission_id: int
    relation_id: int
    relation_type: str
