from datetime import date, datetime
from typing import Dict
from pydantic import BaseModel

class LatestCountResponse(BaseModel):
    pi_id: str
    timestamp: datetime
    counts: Dict[str, int]                    # {object_type: count}
    
class HourlyCountResponse(BaseModel):
    pi_id: str
    date: date
    hourly_counts: Dict[int, Dict[str, int]]  # {hour: {object_type: count}}
    
class DailyCountResponse(BaseModel):
    pi_id: str
    date: date
    total_counts: Dict[str, int]              # {object_type: total_count}