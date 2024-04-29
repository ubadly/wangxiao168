from enum import Enum

from spider.common.datetypes import SchoolType


class School(Enum):
    """
    学校枚举
    """
    xatu: SchoolType = SchoolType(url="https://xatu.168wangxiao.com/")
    xawl: SchoolType = SchoolType(url="https://xawl.168wangxiao.com/")
    nwu: SchoolType = SchoolType(url="https://nwu.168wangxiao.com/")

