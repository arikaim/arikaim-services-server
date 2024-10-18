import uuid
import secrets
from typing import Optional
from sqlmodel import Field, SQLModel, select

class Users(SQLModel, table = True):    
    __tablename__ = 'users'

    id: int = Field(unique = True, primary_key = True)
    uuid: str = Field(unique = True)
    user_name: str = Field(unique = True)
    email: str = Field(unique = True)
    password: str = Field(unique = False)
    status: int
    date_login: Optional[int] = None
    date_created: Optional[int] = None
    date_deleted: Optional[int] = None

    @staticmethod
    def find_user_or_create(session, email, user_name = None):
        user = Users.find_by_email(session,email)

        if not user:
            # create
            user = Users(
                uuid = str(uuid.uuid4()),
                email = email,
                user_name = user_name,
                status = 1,
                password = secrets.token_hex(32)  
            )
            session.add(user)
            session.commit()
            
            return Users.find_by_email(email)
        else:
            return user
      
    
    @staticmethod
    def find_by_email(session, email):
        stm = select(Users).where(Users.email == email)
        return session.exec(stm).first()
    

    @staticmethod
    def find_user(session,id):
        stm = (
            select(Users)
            .where(
                (Users.id == id) |
                (Users.uuid == id)
            )
            .where(Users.status == 1)
            .where(Users.date_deleted == None)
        )

        return session.exec(stm).first()
    