from fastapi import FastAPI
from fastapi_pagination import add_pagination

from games_api.configs.settings import settings
from games_api.routers import api_router

app = FastAPI(title='Games API')
app.include_router(api_router, prefix=settings.API_VERSION)
add_pagination(app)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'main:app', host='0.0.0.0', port=8000, log_level='info', reload=True
    )
