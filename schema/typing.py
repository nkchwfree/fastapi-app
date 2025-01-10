from pydantic import constr
from datetime import datetime
import re

Str_10 = constr(strip_whitespace=True, max_length=10)
Str_64 = constr(strip_whitespace=True, max_length=64)
Str_40 = constr(strip_whitespace=True, max_length=40)
Str_32 = constr(strip_whitespace=True, max_length=32)
Str_16 = constr(strip_whitespace=True, max_length=16)
Str = constr(strip_whitespace=True)
Str_50_No_Empty = constr(strip_whitespace=True, min_length=1, max_length=50)
Str_100_No_Empty = constr(strip_whitespace=True, min_length=1, max_length=100)
Str_200_No_Empty = constr(strip_whitespace=True, min_length=1, max_length=200)


class DateTime(str):
    # default = time.strftime("%Y-%m-%d", time.localtime())
    default = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v == "" or v is None or v == "null":
            return cls.default

        try:
            datetime.strptime(v, "%Y-%m-%d %H:%M:%S")
            return v
        except(TypeError, ValueError):
            raise ValueError("参数不是时间类型")


class Date(str):
    # default = time.strftime("%Y-%m-%d", time.localtime())
    default = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v == "" or v is None or v == "null":
            return cls.default

        try:
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except(TypeError, ValueError):
            raise ValueError("参数不是日期类型")
