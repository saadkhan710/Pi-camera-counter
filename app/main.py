from fastapi import FastAPI, HTTPException, status
from datetime import date, datetime
import logging
from .models import PiUploadRequest, CountData, LogEntry
from .schemas import LatestCountResponse, HourlyCountResponse, DailyCountResponse
from .services import aggregate_hourly_counts, aggregate_daily_counts, get_latest_entry
from .database import data_store

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
app = FastAPI(
    title="Raspberry Pi Object Counting API",
    description="API for receiving and querying object counts from Raspberry Pi cameras",
    version="1.0.0"
)

@app.post("/api/count/upload", status_code=status.HTTP_201_CREATED)
async def upload_counts(request: PiUploadRequest):
    """Endpoint for Raspberry Pi to upload new log entries"""
    try:
        # Convert Pydantic models to dicts for storage
        logs_to_store = [
            {
                "timestamp": log.timestamp,
                "counts": [count.model_dump() for count in log.counts]       # Used model_dump for Serialization: Converting a model to a dictionary

            }
            for log in request.logs
        ]
        
        data_store.add_logs(request.pi_id, logs_to_store)
        logger.info(f"Uploaded {len(logs_to_store)} logs for pi_id: {request.pi_id}")
        return {"message": "Logs uploaded successfully"}
    
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process log upload"
        )
        
@app.get("/api/count/latest", response_model=LatestCountResponse)
async def get_latest_count(pi_id: str):
    """Get the latest count for a specific Raspberry Pi"""
    latest_entry = get_latest_entry(pi_id)
    if not latest_entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"No count data available for {pi_id}"
        )
    
    counts_dict = {count["object_type"]: count["count"] for count in latest_entry["counts"]}
    return LatestCountResponse(
        pi_id=pi_id,
        timestamp=latest_entry["timestamp"],
        counts=counts_dict
    )
    
@app.get("/api/count/hourly", response_model=HourlyCountResponse)
async def get_hourly_counts(pi_id: str):
    """Get hourly aggregated counts"""
    hourly_counts = aggregate_hourly_counts(pi_id)
    if not hourly_counts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"No hourly count data available for {pi_id}"
        )
    
    return HourlyCountResponse(
        pi_id=pi_id,
        date=datetime.now().date(),
        hourly_counts=hourly_counts
    )
    
@app.get("/api/count/daily", response_model=DailyCountResponse)
async def get_daily_counts(pi_id: str, date: date):
    """Get daily aggregated counts"""
    daily_counts = aggregate_daily_counts(pi_id, date)
    if not daily_counts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= f"No daily count data available for {pi_id}"
        )
    
    return DailyCountResponse(
        pi_id=pi_id,
        date=date,
        total_counts=daily_counts
    )