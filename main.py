from typing import Union

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel
from app.database.config import engine, Base, Session
from app.database.models.url import URL, User
from app.validators.all import URLModel
from config import BASE_URL

app = FastAPI()

# Database initialization
Base.metadata.create_all(bind=engine)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/v1/shorten")
def shorten(url: URLModel) -> URLModel:
    return JSONResponse({"url": url.long_url})

@app.get("/{short_code}")
def redirect(short_code):
    url = Session().query(URL).filter(URL.short_code==short_code).first()
    if url is None:
        return JSONResponse({"message": "Not Found"}, status_code=404)
    return RedirectResponse(url.long_url)


@app.get("/user/{user_id}")
def fetch_user(user_id: int):
    try:
        user = Session().query(User).filter(User.id == user_id).first()
        if user is None:
            return JSONResponse({"message": "User not found"}, status_code=404)
        return JSONResponse({"user": user.email}, status_code=200)
    except Exception as error:
        return JSONResponse({"error": str(error)}, status_code=500)
