from arikaim.core.db.models.users import Users
from arikaim.core.db.models.access_tokens import AccessTokens
from arikaim.core.access.user import AuthUser
from arikaim.core.db.db import db
from sqlmodel import Session, select
from sqlalchemy.exc import SQLAlchemyError

class TokenAuthProvider:
    
    def authenticate(self, credentails):

        if "Authorization" not in credentails.headers:
            return False
        try:
            token = credentails.headers["Authorization"]
      
            with Session(db.engine) as session:
                statement = select(AccessTokens).where(AccessTokens.token == token)
                access_tokens = session.exec(statement).first()
            
                statement = select(Users).where(Users.id == access_tokens.user_id)
                user = session.exec(statement).first()
                session.close()
                
                return AuthUser(id = user.id, uuid = user.uuid, username = user.user_name, email = user.email)
        except SQLAlchemyError as e:
            print(e)
            return False