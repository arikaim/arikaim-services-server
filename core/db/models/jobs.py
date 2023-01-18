from peewee import *
from core.container import di

class Jobs(Model):     
    id = BigAutoField(unique = True, primary_key = True)
    uuid = CharField(unique = True)
    status = IntegerField()
    name = CharField(unique = True)
    handler_class = CharField()
    recuring_interval = CharField()
    extension_name = CharField()
    priority = IntegerField()
    executed = IntegerField()
    type = CharField()
    service_name = CharField()
    date_created = IntegerField()
    schedule_time = IntegerField()
    date_executed = IntegerField()
    config = TextField()
    queue = CharField()

    class Meta:
        table_name = 'jobs'
        database = di.get('db').peewee