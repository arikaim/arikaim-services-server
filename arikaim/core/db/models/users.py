import uuid
import secrets
from peewee import *
from arikaim.core.db.db import db

class Users(Model):     
    id = BigAutoField(unique = True, primary_key = True)
    uuid = CharField(unique = True)
    user_name = CharField(unique = True)
    email = CharField(unique = True)
    password = CharField(unique = False)
    status = IntegerField()
    date_login = IntegerField()
    date_created = IntegerField()
    date_deleted = IntegerField()

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
    
    class Meta:
        table_name = 'users'
        database = db.peewee