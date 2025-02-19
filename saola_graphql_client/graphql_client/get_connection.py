# Generated by ariadne-codegen
# Source: graphql

from typing import Optional

from .base_model import BaseModel
from .fragments import Connection


class GetConnection(BaseModel):
    connections_by_pk: Optional["GetConnectionConnectionsByPk"]


class GetConnectionConnectionsByPk(Connection):
    pass
