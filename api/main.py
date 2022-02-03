from fastapi import FastAPI

from api.routers import submit, done
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app = FastAPI()
app.include_router(submit.router)
app.include_router(done.router)
app.add_middleware(
  CORSMiddleware,
  allow_origins = ["*"],
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ["*"]
)