from tortoise.fields import (
    BooleanField,
    DatetimeField,
    DateField,
    TimeField,
    IntField,
    CharField,
    BigIntField,
    TextField,
    FloatField,
    JSONField,
    CharEnumField,
    IntEnumField,
    ForeignKeyRelation,
    ForeignKeyField,
    ReverseRelation,
    SET_NULL,
    ManyToManyField,
    ManyToManyRelation,
)
from .exceptions import ModelException

from tortoise.models import Model
from .fields import MyCharField, TimestampField


class BaseModel(Model):
    id = IntField(pk=True, description="ID")
    create_time = TimestampField(null=True, description="创建时间")

    class Meta:
        abstract = True

    def to_dict(self):
        result = {}
        for column, value in self:
            result[column] = value
        return result


class TagModel(BaseModel):
    name = MyCharField(100, null=False, description="名称")

    class Meta:
        table = "my_tag"
