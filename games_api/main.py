from fastapi import FastAPI

from games_api.configs.settings import settings
from games_api.routers import api_router

app = FastAPI(title='Games API')
app.include_router(api_router, prefix=settings.API_VERSION)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main:app', host='0.0.0.0', port=8000, log_level='info', reload=True
    )
