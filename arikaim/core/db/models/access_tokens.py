from peewee import *
from arikaim.core.db.db import db

class AccessTokens(Model):
    id = BigAutoField(unique = True, primary_key = True)
    uuid = CharField(unique = True)
    token = CharField(unique = True)
    status = IntegerField()
    type = IntegerField()
    user_id = IntegerField()
    date_created = IntegerField()
    date_expired = IntegerField()

    class Meta:
        table_name = 'access_tokens'
        database = db.peewee
    