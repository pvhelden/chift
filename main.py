from fastapi import FastAPI

from routers import router

chift = FastAPI()

chift.include_router(router)
