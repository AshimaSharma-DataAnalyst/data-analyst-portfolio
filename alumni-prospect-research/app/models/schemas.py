"""
Pydantic schemas for request validation and API responses.

These schemas validate incoming data, serialize outgoing data,
and generate Swagger documentation.
"""

from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import HttpUrl


class AlumniCreate(BaseModel):
    """
    Schema used when creating or updating an alumni record.
    """

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Full name of the alumni"
    )

    company: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Company where the alumni works"
    )

    designation: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Current job title"
    )

    city: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Current city"
    )

    linkedin_url: Optional[HttpUrl] = Field(
        default=None,
        description="LinkedIn profile URL"
    )

    source: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Information source"
    )

    summary: str = Field(
        ...,
        min_length=5,
        description="Brief alumni summary"
    )


class AlumniResponse(AlumniCreate):
    """
    Schema returned to the client.
    """

    id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class AlumniSearch(BaseModel):
    """
    Schema used for searching alumni.
    """

    name: Optional[str] = None

    company: Optional[str] = None

    city: Optional[str] = None

    designation: Optional[str] = None