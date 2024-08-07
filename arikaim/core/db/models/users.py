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

    class Meta:
        table_name = 'users'
        database = db.peewee