from typing import TYPE_CHECKING
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from database import Base, get_async_session


class UserModel(Base):
    __tablename__ = "user"

    if TYPE_CHECKING:  # pragma: no cover
        id: int
        email: str
        hashed_password: str
        is_active: bool
        is_superuser: bool
        is_verified: bool
    else:
        id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
        email: Mapped[str] = mapped_column(
            sa.String(length=320), unique=True, index=True, nullable=False
        )
        hashed_password: Mapped[str] = mapped_column(
            sa.String(length=1024), nullable=False
        )
        is_active: Mapped[bool] = mapped_column(sa.Boolean, default=True, nullable=False)
        is_superuser: Mapped[bool] = mapped_column(
            sa.Boolean, default=False, nullable=False
        )
        is_verified: Mapped[bool] = mapped_column(
            sa.Boolean, default=False, nullable=False
        )


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session=session, user_table=UserModel)
