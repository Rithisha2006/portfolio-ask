from pydantic import BaseModel
from typing import List


class SectorExposure(BaseModel):
    sector: str
    weight_pct: float


class ExposureResponse(BaseModel):
    exposures: List[SectorExposure]