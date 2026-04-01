from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse
from app.db.database import Base,engine 
from app.models import user,record
from app.routes import user_routes, record_routes, dashboard_routes,auth_routes
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Dashboard API")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)
@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request:Request,exc : RateLimitExceeded):
    return JSONResponse(
        status_code=429,content={"details":"Rate limiyt exceeded.Try again later."}
    )
app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(auth_routes.router)
@app.get("/")
def root():
    return {"message":"API is running"}
