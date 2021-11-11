from fastapi import FastAPI

import uvicorn
from routers import items

app = FastAPI()


app.include_router(
    items.router,
    prefix="/item",
    tags=["Item"],
    responses={418: {"description": "I'm a teapot"}},
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)