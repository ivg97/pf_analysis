import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core import config
from core.config import app_settings
from api.v1 import base


app = FastAPI(
    title=app_settings.PROJECT_NAME,
    description='Example run fastAPI project',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

# ROUTERS
app.include_router(base.router, prefix='/api/v1')


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=app_settings.PROJECT_HOST,
        port=app_settings.PROJECT_PORT
    )
