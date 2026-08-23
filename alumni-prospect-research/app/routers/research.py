from fastapi import APIRouter
from pydantic import BaseModel

from app.services.research_service import ResearchService

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)


class ResearchRequest(BaseModel):
    name: str
    company: str
    designation: str
    education: str | None = ""
    city: str | None = ""


@router.post("/profile")
def generate_profile(request: ResearchRequest):

    service = ResearchService()

    return service.build_profile(
        request.model_dump()
    )
