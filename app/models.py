from datetime import datetime
from typing import List, Dict
from pydantic import BaseModel, Field, field_validator

class CountData(BaseModel):
    object_type: str = Field(..., examples=["person"], description="Type of object counted")
    count: int = Field(..., examples=[5], description="Number of objects detected")

class LogEntry(BaseModel):
    timestamp: datetime = Field(..., description="Time of count measurement")
    counts: List[CountData] = Field(..., description="List of object counts")

class PiUploadRequest(BaseModel):
    pi_id: str = Field(..., examples=["cam-123"], description="Unique identifier of Raspberry Pi")
    logs: List[LogEntry] = Field(..., description="List of log entries to upload")

    @field_validator('logs')
    def logs_not_empty(cls, v):
        if not v:
            raise ValueError("No logs from Rasberry:PI")
        return v