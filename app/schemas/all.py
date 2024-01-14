from pydantic import BaseModel


class URLCreate(BaseModel):
    long_url: str
