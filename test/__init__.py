import models

async def clear_db():
    await models.TagModel.all().delete()


async def get_tag(**kwargs):
    data = {
        "name": "demo",
        "create_time": "2021-01-01 00:00:00",
    }

    for k, v in kwargs.items():
        data[k] = v

    record = models.TagModel(**data)
    await record.save()
    return record
