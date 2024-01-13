from typing import Union, Optional
from pydantic import BaseModel

class URLModel(BaseModel):
    long_url: str
    short_code : Optional[str] = ""
