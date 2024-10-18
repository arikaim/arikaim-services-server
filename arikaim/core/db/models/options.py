from typing import Optional
from sqlmodel import Field, SQLModel, select

class Options(SQLModel, table = True):     
    __tablename__ = 'options'

    id: int = Field(unique = True, primary_key = True)
    key: str
    value: str | None
  
    @staticmethod
    def save_option(session, key, value):
        stm = (
            select(Options.value).where(Options.key == key)
        )
        model = session.exec(stm).first()
        
        if model == None:
            option = Options(
                key = key,
                value = value
            )
            session.add(option)
            session.commit()
        else:
            model.value = value
            return model.save()
            

    @staticmethod
    def get_option(session, key, default = None):
        stm = select(Options.value).where(Options.key == key)
        model = session.exec(stm).first()
        
        if not model:
            return default
        
        return model.value


    @staticmethod
    def increment(session, key, value = 1):

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
        