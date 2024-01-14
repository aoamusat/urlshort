from app.database.models.url import URL
import string
import uuid
from config import BASE_URL
from sqlalchemy.orm import Session

def base62_encode(url_count:int)->str:
    base_string = string.digits + string.ascii_letters
    hash_str = ""
    while url_count > 0:
        hash_str += base_string[url_count % 62]
        url_count //= 62
    return hash_str

def generate_short_code()->str:
    unique_id = uuid.uuid4()
    short_url = str(unique_id.hex)[:6]
    return short_url

def create_url(db: Session, long_url: str)->str:
    short_code = generate_short_code()
    new_url = URL(long_url=long_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)  # Get the updated record with ID
    return f"{BASE_URL}" + new_url.short_code