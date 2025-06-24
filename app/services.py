from datetime import datetime, date
from collections import defaultdict
from typing import Dict, List, Any
from .database import data_store

def aggregate_hourly_counts(pi_id: str) -> Dict[int, Dict[str, int]]:      # {10: {"person": 5, "car": 3}, ....}
    """Aggregate counts by hour for the current day"""
    counts = data_store.get_counts_for_pi(pi_id)
    if not counts:
        return {}
    
    today = datetime.now().date()
    hourly_counts = defaultdict(lambda: defaultdict(int))                  # Each missing outer key (hour) automatically creates new defaultdict(int) and assigns default value
    
    for entry in counts:
        entry_date = entry["timestamp"].date()
        if entry_date == today:
            hour = entry["timestamp"].hour
            for count in entry["counts"]:
                hourly_counts[hour][count["object_type"]] += count["count"]
    
    return {hour: dict(counts) for hour, counts in hourly_counts.items()}  # Dictionary comprehension that converts the nested defaultdict into a regular dict.
  
def aggregate_daily_counts(pi_id: str, target_date: date) -> Dict[str, int]:
    """Aggregate counts by object type for a specific date"""
    counts = data_store.get_counts_for_pi(pi_id)
    if not counts:
        return {}
    
    daily_counts = defaultdict(int)
    
    for entry in counts:
        entry_date = entry["timestamp"].date()
        if entry_date == target_date:
            for count in entry["counts"]:
                daily_counts[count["object_type"]] += count["count"]
    
    return dict(daily_counts)                                             # Converts defaultdict into a regular dict.
  
def get_latest_entry(pi_id: str) -> Dict[str, Any]:
    """Get the most recent log entry for a pi"""
    counts = data_store.get_counts_for_pi(pi_id)
    if not counts:
        return {}
    return max(counts, key=lambda x: x["timestamp"])                      # Returns the dictionary with the latest timestamp