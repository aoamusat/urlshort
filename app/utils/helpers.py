# Example: Creating a new URL record
from app.database.models.url import URL
def create_url(db, long_url, short_code):
    new_url = URL(long_url=long_url, short_code=short_code)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)  # Get the updated record with ID
    return new_url
