from fastapi import FastAPI

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from api import chainlink
from utils.logger.logger import logger

app = FastAPI(
    title="API Project",
    description="Work in progress",
    version='0.1',
    swagger_ui_parameters={"docExpansion": "none"},
)

routers = [
    chainlink.router,
]

for router in routers:  # routers_test
    app.include_router(router)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
                   allow_credentials=True)


@app.on_event("startup")
async def startup_event():
    logger.info("API STARTED, docs at /docs#")


if __name__ == "__main__":
    """
    https://github.com/tiangolo/fastapi/issues/1508
    """
    import uvicorn
    from os import getenv

    load_dotenv()
    host = getenv("HOST", "0.0.0.0")
    port = int(getenv("PORT", "8080"))  # Default port is 8080 if not specified
    uvicorn.run(app, host=host, port=port)
