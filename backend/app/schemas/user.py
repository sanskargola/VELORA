from pydantic import BaseModel, ConfigDict


class UserProfileOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    role: str
    is_verified: bool


class UserProfileUpdate(BaseModel):
    email: str | None = None
