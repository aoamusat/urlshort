"""
FastAPI URL Shortener

This file defines a FastAPI application for a simple URL shortener.
It includes routes for rendering an HTML homepage, shortening URLs via API, 
and redirecting to the original URLs using short codes.
"""
import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from app.utils.helpers import create_url
from app.database.config import engine, Base, Session
from app.database.models.url import URL
from app.schemas.all import URLCreate
from config import SENTRY_DSN

logging.basicConfig(level=logging.INFO)

sentry_sdk.init(
    dsn=f"{SENTRY_DSN}",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    integrations=[LoggingIntegration(level=logging.INFO, event_level=logging.INFO)],
)

app = FastAPI()

# Database initialization
Base.metadata.create_all(bind=engine)

# Template configuration
templates = Jinja2Templates(directory="templates")

# Static files configuration
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """
    Render the HTML homepage.

    Args:
        request (Request): The incoming request object.

    Returns:
        HTMLResponse: The HTML response containing the rendered template.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/v1/shorten", response_class=JSONResponse)
def shorten(url: URLCreate):
    """
    Shorten a given URL and return the short and original URLs in a JSONResponse.

    Args:
        url (URLCreate): The data model for creating a new URL.

    Returns:
        JSONResponse: The response containing the short URL and original URL.
            - Status Code 201: URL successfully shortened.
            - Status Code 500: Internal Server Error if an exception occurs during the process.
    """
    try:
        long_url = str(url.long_url)
        db = Session()
        short_url = create_url(db, long_url=long_url)
        db.close()  # return the connection back to the pool
        return JSONResponse(
            {"short_url": short_url, "long_url": long_url}, status_code=201
        )
    except SQLAlchemyError as e:
        logging.error("Internal Server Error: %s", str(e))
        return JSONResponse({"message": "Internal Server Error!"}, status_code=500)


@app.get("/{short_code}")
def redirect(short_code: str):
    """
    Redirect to the original URL or return a JSONResponse with a "URL Not Found" message.

    Args:
        short_code (str): The short code associated with the shortened URL.

    Returns:
        - RedirectResponse: Redirects to the original URL.

    Raises:
        HTTPException: Raises a 404 HTTPException if the short code is not found.
    """
    url = Session().query(URL).filter(URL.short_code == short_code).first()
    if url is None:
        return JSONResponse({"message": "URL Not Found"}, status_code=404)
    return RedirectResponse(url.long_url)
