from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timedelta
from typing import Callable


class RateLimitingMiddleware(BaseHTTPMiddleware):
    # Rate limiting configurations: 100 requests per day
    RATE_LIMIT_DURATION = timedelta(days=1)
    RATE_LIMIT_REQUESTS = 100

    def __init__(self, app):
        super().__init__(app)
        self.request_counts = {}

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        client_ip = request.client.host

        request_count, last_request = self.request_counts.get(
            client_ip, (0, datetime.min)
        )

        elapsed_time = datetime.now() - last_request

        if elapsed_time > self.RATE_LIMIT_DURATION:
            request_count = 1
        else:
            if request_count >= self.RATE_LIMIT_REQUESTS:
                return JSONResponse(
                    status_code=429,
                    content={"message": "Rate limit exceeded. Please try again later."},
                )
            request_count += 1
        self.request_counts[client_ip] = (request_count, datetime.now())
        response = await call_next(request)
        return response
