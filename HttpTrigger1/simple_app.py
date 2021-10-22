from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware

async def homepage(request):
    return JSONResponse({"hello": "world"})


class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Custom"] = "Example"
        return response


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
    ],
    # Works with no middlewares defined
    #
    # Hangs with this line:
    # middleware=[Middleware(CustomHeaderMiddleware)]
    #
    # Works with this line:
    middleware = [Middleware(CORSMiddleware)]
)
