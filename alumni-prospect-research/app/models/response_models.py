"""
Response models used by paginated API endpoints.
"""

from typing import List

from pydantic import BaseModel
from pydantic import Field

from app.models.schemas import AlumniResponse


class AlumniListResponse(BaseModel):
    """
    Standard paginated response for alumni records.
    """

    page: int = Field(
        description="Current page number"
    )

    size: int = Field(
        description="Number of records per page"
    )

    total_records: int = Field(
        description="Total number of alumni records"
    )

    total_pages: int = Field(
        description="Total number of available pages"
    )

    items: List[AlumniResponse] = Field(
        description="List of alumni records"
    )


class AlumniSearchResponse(AlumniListResponse):
    """
    Response returned for search endpoints.

    Uses the same pagination structure as AlumniListResponse.
    """
    pass