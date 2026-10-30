from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100 # Default chunk size is 100
    overlap: Optional[int] = 20 # Default overlap is 20  
    do_reset: Optional[int] = 0
