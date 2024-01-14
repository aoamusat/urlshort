from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    long_url: HttpUrl
