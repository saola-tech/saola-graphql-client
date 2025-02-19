# Generated by ariadne-codegen
# Source: graphql

from typing import Optional

from .base_model import BaseModel
from .fragments import CrmRecord


class GetCrmRecord(BaseModel):
    crm_records_by_pk: Optional["GetCrmRecordCrmRecordsByPk"]


class GetCrmRecordCrmRecordsByPk(CrmRecord):
    pass
