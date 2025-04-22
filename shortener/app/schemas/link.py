from pydantic import BaseModel


class LinkBase(BaseModel):
    base_url: str


class LinkCreate(LinkBase):
    ...


class LinkDB(LinkBase):
    id: int

    class Config:
        orm_mode = True
