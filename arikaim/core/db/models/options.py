from peewee import *
from arikaim.core.db.db import db

class Options(Model):     
    id = BigAutoField(unique = True, primary_key = True)
    key = CharField(null = False, unique = True)
    value = TextField(null = False)
  
    @staticmethod
    def save_option(key, value):
        model = (Options
            .select(Options.value)
            .where(Options.key == key)
            .get_or_none())
        
        if model == None:
            return Options.create(
                key = key,
                value = value
            )
        else:
            model.value = value
            return model.save()
            
    @staticmethod
    def get_option(key, default = None):

        model = (Options
            .select(Options.value)
            .where(Options.key == key)
            .get_or_none())
        
        if not model:
            return default
        
        return model.value


    @staticmethod
    def increment(key, value = 1):

        model, created = Options.get_or_create(
            key = key,
            defaults = {
                'value': 1
            }
        )

        if not created:
            return (Options.update(value = Options.value + 1)
                .where(Options.key == value)
                .execute())

 
    class Meta:
        table_name = 'options'
        database = db.peewee
