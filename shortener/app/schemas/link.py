from pydantic import BaseModel, HttpUrl, field_validator


class LinkBase(BaseModel):
    base_url: str


class LinkCreate(LinkBase):
    base_url: HttpUrl

    @field_validator('base_url', mode='before')
    def convert_url(cls, v):
        return str(v) if v else v


class LinkDB(LinkBase):
    id: int

    class Config:
        orm_mode = True
