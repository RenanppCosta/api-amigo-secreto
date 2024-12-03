from tortoise.models import Model
from tortoise import fields

class Participant(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=120)
    email = fields.CharField(max_length=200)
    group = fields.ForeignKeyField("models.Group", related_name="participants")
    

