from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.mutable import MutableList

from model.base import Base


class Stack(Base):
    __tablename__ = "stacks"
    __table_args__ = {"schema": "rpn"}

    id = Column(Integer, autoincrement=True, primary_key=True)
    items = Column(MutableList.as_mutable(ARRAY(Integer)), default=[])
