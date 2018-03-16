from Model.BaseModel import BaseModel, EnumField
from peewee import IntegerField, CharField, PrimaryKeyField


class Course(BaseModel):
    id = PrimaryKeyField()
    presentation = EnumField(choices=["practical", "theoretic"])
    type = EnumField(choices=["professional", "basic", "prime", "public"])
    status_prerequisite = EnumField(choices=["yes", "no"])
    name = CharField(30)
    unit_number = IntegerField(30)
    price = IntegerField(30)
    list_prerequisite = CharField()

    class Meta:
        db_table = "course"
