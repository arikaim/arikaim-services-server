from peewee import *
from arikaim.core.db.db import db

class PermissionRelations(Model):
    id = BigAutoField(unique = True, primary_key = True)
    uuid = CharField(unique = True)
    read = IntegerField()
    write = IntegerField()
    delete = IntegerField()
    execute = IntegerField()
    permission_id = IntegerField()
    relation_id = IntegerField()
    relation_type = CharField()

    class Meta:
        table_name = 'permission_relations'
        database = db.peewee