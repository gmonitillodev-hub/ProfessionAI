from enum import Enum
from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, model_validator

from utils.file_handler import check_folder


class OperationEnum(str, Enum):
    CLASSIFY = "classify"
    SUMMARIZE = "summarize"
    KEYWORD_EXTRACTION = "keyword-extraction"
    FULL_OPERATION = "full-operation"


class Request(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    file_path: str = Field(..., min_length=1)
    operation_type: OperationEnum | None = Field(None)

    @model_validator(mode="after")
    def validate(self: Self) -> Self:
        """ Here we validate the exitance of the file / folder """
        """if self.file_path == "/.":
            raise ValueError("Invalid file path")"""

        try:
            check_result = check_folder(self.file_path)
            print(f"Check result -> {check_result}")
        except Exception as e:
            print(f"Check error -> {e}")
        return self


