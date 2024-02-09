import uuid
from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from app import User
from app.internal.auth import auth_backend
from app.managers.user import get_user_manager
from app.schemas.user import UserRead, UserUpdate, UserCreate

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
