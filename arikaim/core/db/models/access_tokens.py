from typing import Optional
from sqlmodel import Field, SQLModel

class AccessTokens(SQLModel, table = True):
    __tablename__ = 'access_tokens'

    id: int = Field(unique = True, primary_key = True)
    uuid: str = Field(unique = True)
    token: str = Field(unique = True)
    status: int
    type: int
    user_id: int
    date_created: Optional[int] = None
    date_expired: Optional[int] = None
 