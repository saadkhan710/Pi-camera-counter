from datetime import datetime, date as Date
from typing import Dict
from pydantic import BaseModel, Field

class LatestCountResponse(BaseModel):
    """Response model containing the latest count data from Rasberry Pi device"""
    pi_id: str = Field(
        ...,
        examples=["cam-123"],
        description="Unique identifier of the Raspberry Pi device",
    )
    timestamp: datetime = Field(
        ...,
        examples=["2023-05-01T14:30:00Z"],
        description="Timestamp of the most recent count measurement in ISO 8601 format"
    )
    counts: Dict[str, int] = Field(
        ...,
        examples=[{"person": 5, "car": 3}],
        description="Dictionary mapping object types to their latest counts"
    )

class HourlyCountResponse(BaseModel):
    """Response model containing the Hourly count data from Rasberry Pi device"""
    pi_id: str = Field(
        ...,
        examples=["cam-123"],
        description="Unique identifier of the Raspberry Pi device"
    )
    date: Date = Field(
        ...,
        examples=["2023-05-01"],
        description="Date of the aggregated counts in YYYY-MM-DD format"
    )
    hourly_counts: Dict[int, Dict[str, int]] = Field(
        ...,
        examples=[{
            10: {"person": 15, "car": 7},
            11: {"person": 20, "car": 5}
        }],
        description="Nested dictionary mapping hours (0-23) to count dictionaries"
    )

class DailyCountResponse(BaseModel):
    """Response model containing the Daily count data from Rasberry Pi device"""
    pi_id: str = Field(
        ...,
        examples=["cam-123"],
        description="Unique identifier of the Raspberry Pi device"
    )
    date: Date = Field(
        ...,
        examples=["2023-05-01"],
        description="Date of the aggregated counts in YYYY-MM-DD format"
    )
    total_counts: Dict[str, int] = Field(
        ...,
        examples=[{"person": 120, "car": 45}],
        description="Dictionary mapping object types to their total daily counts"
    )