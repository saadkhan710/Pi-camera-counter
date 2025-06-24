from typing import Dict, List, Any
from datetime import datetime

class DataStore:
    def __init__(self):
        self.counts: Dict[str, List[Dict[str, Any]]] = {}  # {pi_id: [{timestamp, counts}, ...]}
        self.last_upload: Dict[str, datetime] = {}  # {pi_id: timestamp}
        
    def add_logs(self, pi_id: str, logs: List[Dict[str, Any]]):
        if pi_id not in self.counts:
            self.counts[pi_id] = []
        self.counts[pi_id].extend(logs)                  # Used append here as it adds multiple item to an existing list
        self.last_upload[pi_id] = datetime.now()
        
    def get_counts_for_pi(self, pi_id: str) -> List[Dict[str, Any]]:
        return self.counts.get(pi_id, [])                # Used get method because if pi_id doesn't exist it returns empty list [] ,systems won't crash
      
# Initialize the data store
data_store = DataStore()