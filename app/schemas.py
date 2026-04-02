from datetime import datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    password_hash: str


class UserResponse(BaseModel):
    id: UUID
    email: str
    password_hash: str
    created_at: datetime


class CreateListRequest(BaseModel):
    owner_id: UUID
    name: str
    max_budget: Decimal = Decimal("0")


class UpdateListRequest(BaseModel):
    owner_id: UUID
    name: str | None = None
    max_budget: Decimal | None = None


class DeleteListRequest(BaseModel):
    owner_id: UUID


class ListResponse(BaseModel):
    id: UUID
    owner_id: UUID
    name: str
    max_budget: Decimal
    created_at: datetime


class DeleteListResponse(BaseModel):
    message: str


class ShareListRequest(BaseModel):
    list_id: UUID
    owner_id: UUID
    user_id: UUID
    user_email: str
    role: Literal["owner", "editor", "viewer"] = "editor"


class ShareListResponse(BaseModel):
    list_id: UUID
    shared_with: str
    role: Literal["owner", "editor", "viewer"]


class ListMemberResponse(BaseModel):
    user_id: UUID
    email: str
    role: Literal["owner", "editor", "viewer"]
    created_at: datetime
