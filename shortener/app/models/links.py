from sqlalchemy import Column, Text

from app.core.db import Base


class Link(Base):
    base_url = Column(Text, nullable=False)
