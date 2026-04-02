from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.internal_list_members import router as internal_list_members_router
from app.routes.internal_lists import router as internal_lists_router
from app.routes.internal_users import router as internal_users_router

app = FastAPI(title="IO Service")

app.include_router(health_router)
app.include_router(internal_list_members_router)
app.include_router(internal_lists_router)
app.include_router(internal_users_router)
