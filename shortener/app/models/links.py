from sqlalchemy import Column, Text

# Импортируем базовый класс для моделей.
from app.core.db import Base


class Link(Base):
    base_url = Column(Text, nullable=False)
