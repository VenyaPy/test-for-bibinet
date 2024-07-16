from fastapi import FastAPI
import uvicorn

from models.search.router import router_search

app = FastAPI()


app.include_router(router_search)


if __name__ == "__main__":
    uvicorn.run("FastAPI.app.main:app", reload=True)