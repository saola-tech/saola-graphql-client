# Generated by ariadne-codegen
# Source: graphql

from typing import Any

from pydantic import Field

from .base_model import BaseModel


class RefreshAccessToken(BaseModel):
    refresh_access_token: Any = Field(alias="refreshAccessToken")
