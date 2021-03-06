from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Submit(Base):
    __tablename__ = "submits"

    id = Column(Integer, primary_key=True)
    password = Column(String(1024))
    src = Column(String(1024))
    error = Column(String(1024))

    done = relationship("Done", back_populates="submit")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("submits.id"), primary_key=True)
    message = Column(String(1024))

    submit = relationship("Submit", back_populates="done")