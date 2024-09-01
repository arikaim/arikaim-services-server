from peewee import *
from arikaim.core.db.db import db

class Drivers(Model):
    id = BigAutoField(unique = True, primary_key = True)
    uuid = CharField(unique = True)
    name = CharField(unique = True)   
    title = CharField(null = True)
    description = TextField(null = True)
    version = CharField(null = True)   
    config = TextField(null = True)
   
    @staticmethod
    def get_config(name):
        model = (Drivers
            .select(Drivers.config)
            .where(Drivers.name == name)
            .get_or_none()
        )
        if not model:
            return None
        else:    
            return model.config

    class Meta:
        table_name = 'drivers'
        database = db.peewee

    