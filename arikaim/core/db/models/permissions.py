from peewee import *
from arikaim.core.db.db import db

class Permissions(Model):
    id = BigAutoField(unique = True, primary_key = True)
    uuid = CharField(unique = True)
    name = CharField(unique = True)
    slug = CharField(unique = True)
    title = CharField()
    extension_name = CharField()
    description = CharField()
    deny = IntegerField()

    class Meta:
        table_name = 'permissions'
        database = db.peewee