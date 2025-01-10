from pydantic import BaseModel, PositiveInt, Field, validator
from typing import List, Dict

class Add(BaseModel):
    name: str = Field("", title="内容")

class Edit(Add):
    id: int = Field(title="ID")

class SearchForm(BaseModel):
    page: PositiveInt = 1
    page_size: PositiveInt = 10000
    keyword: str = Field("", title="关键词")

class Detail(BaseModel):
    id: int = Field(title="ID")
    name: str = Field("", title="内容")
    create_time: str = Field(title="创建时间")

class SearchList(BaseModel):
    result_list: List[Detail] = []
    total: int = 0
