from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database.config import engine, Base, Session
from app.database.models.url import URL
from app.schemas.all import URLCreate
from fastapi.staticfiles import StaticFiles
from app.utils.helpers import create_url

app = FastAPI()

# Database initialization
Base.metadata.create_all(bind=engine)

# Template configuration
templates = Jinja2Templates(directory="templates")

# Static files configuration
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/v1/shorten", response_class=JSONResponse)
def shorten(url: URLCreate):
    try:
        long_url = url.long_url
        db = Session()
        short_url = create_url(db, long_url=long_url)
        return JSONResponse(
            {"short_url": short_url, "long_url": long_url}, status_code=201
        )
    except Exception as e:
        return JSONResponse({"message": str(e)}, status_code=500)


@app.get("/{short_code}")
def redirect(short_code):
    url = Session().query(URL).filter(URL.short_code == short_code).first()
    if url is None:
        return JSONResponse({"message": "Not Found"}, status_code=404)
    return RedirectResponse(url.long_url)
