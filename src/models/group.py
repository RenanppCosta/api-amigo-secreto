from tortoise.models import Model
from tortoise import fields

class Group(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=120)
    date = fields.DatetimeField()
    created_by = fields.ForeignKeyField("models.User", related_name="groups")
    
    @property
    def formatted_date(self):
        """Retorna a data no formato DD/MM/AAAA."""
        return self.date.strftime("%d/%m/%Y")
