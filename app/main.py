from fastapi import FastAPI
from loguru import logger
from v1.services.routes import router as router_v1

import os
import uvicorn


api = FastAPI()
api.include_router(router_v1, prefix="/v1")


@api.get("/")
async def healthcheck():
    return {
        "project": "STORI accounts API",
        "version": "0.1.0",
        "status": "OK",
    }


if __name__ == "__main__":
    log_format = "%(asctime)s | %(levelname)s | %(message)s"
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = log_format
    log_config["formatters"]["default"]["fmt"] = log_format

    logger.info("Starting API server...")
    uvicorn.run(
        api,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 3000)),
        log_config=log_config
    )
