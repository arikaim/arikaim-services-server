import uuid
import secrets
from typing import Optional
from sqlmodel import Field, SQLModel
from arikaim.core.db.db import db

class Users(SQLModel):    
    __tablename__ = 'users'

    id: int = Field(unique = True, primary_key = True)
    uuid: str = Field(unique = True)
    user_name: str = Field(unique = True)
    email: str = Field(unique = True)
    password: str = Field(unique = False)
    status: int = Field()
    date_login: Optional[int] = None
    date_created: Optional[int] = None
    date_deleted: Optional[int] = None

    @staticmethod
    def find_user_or_create(email, user_name = None):
        user = Users.find_by_email(email)

        if not user:
            # create
            Users.create(
                uuid = str(uuid.uuid4()),
                email = email,
                user_name = user_name,
                status = 1,
                password = secrets.token_hex(32)  
            )

            return Users.find_by_email(email)
        else:
            return user
      
    
    @staticmethod
    def find_by_email(email):
        return (Users
            .select()
            .where(
                Users.email == email
            )
            .get_or_none())
        
    @staticmethod
    def find_user(id):
        return (Users
            .select()
            .where(
                (Users.id == id) |
                (Users.uuid == id)
            )
            .where(Users.status == 1)
            .where(Users.date_deleted == None)
            .get_or_none())
    
   