from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import UploadFile
from fastapi import File

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

import shutil
import os

from app.database.database import get_db

from app.models.schemas import AlumniCreate
from app.models.schemas import AlumniResponse
from app.models.response_models import AlumniListResponse

from app.services.database_service import DatabaseService

from app.security.jwt_handler import get_current_active_user


router = APIRouter(
    prefix="/alumni",
    tags=["Alumni"]
)

# ===================================================
# CREATE
# ===================================================

@router.post(
    "/",
    response_model=AlumniResponse,
    status_code=201
)
def create_alumni(
    alumni: AlumniCreate,
    current_user=Depends(get_current_active_user),
    db: Session = Depends(get_db)
):

    service = DatabaseService(db)

    return service.create_alumni(alumni)


# ===================================================
# GET ALL
# Pagination + Sorting
# ===================================================

@router.get(
    "/",
    response_model=AlumniListResponse
)
def get_all_alumni(

    page: int = Query(
        1,
        ge=1,
        description="Page number"
    ),

    size: int = Query(
        10,
        ge=1,
        le=100,
        description="Records per page"
    ),

    sort_by: str = Query(
        "id",
        description="Sort by column"
    ),

    order: str = Query(
        "asc",
        pattern="^(asc|desc)$",
        description="Sort order"
    ),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    return service.get_all_alumni(
        page,
        size,
        sort_by,
        order
    )

# ===================================================
# SEARCH
# ===================================================

@router.get(
    "/search",
    response_model=AlumniListResponse
)
def search_alumni(

    name: str | None = Query(
        default=None,
        description="Search by alumni name"
    ),

    company: str | None = Query(
        default=None,
        description="Search by company"
    ),

    city: str | None = Query(
        default=None,
        description="Search by city"
    ),

    designation: str | None = Query(
        default=None,
        description="Search by designation"
    ),

    page: int = Query(
        1,
        ge=1
    ),

    size: int = Query(
        10,
        ge=1,
        le=100
    ),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    return service.search_alumni(

        name=name,

        company=company,

        city=city,

        designation=designation,

        page=page,

        size=size

    )



# ===================================================
# DASHBOARD STATISTICS
# ===================================================

@router.get("/stats")
def statistics(

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    return service.get_statistics()


@router.get("/stats/companies")
def company_statistics(

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    return service.company_statistics()


@router.get("/stats/cities")
def city_statistics(

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    return service.city_statistics()


# ===================================================
# EXPORT CSV
# ===================================================

@router.get("/export/csv")
def export_csv(

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    file_path = service.export_csv()

    return FileResponse(

        path=file_path,

        filename="alumni.csv",

        media_type="text/csv"

    )


# ===================================================
# EXPORT EXCEL
# ===================================================

@router.get("/export/excel")
def export_excel(

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    file_path = service.export_excel()

    return FileResponse(

        path=file_path,

        filename="alumni.xlsx",

        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )


# ===================================================
# IMPORT CSV
# ===================================================

@router.post("/import/csv")
def import_csv(

    file: UploadFile = File(...),

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    uploads_folder = "uploads"

    os.makedirs(

        uploads_folder,

        exist_ok=True

    )

    filepath = os.path.join(

        uploads_folder,

        file.filename

    )

    with open(

        filepath,

        "wb"

    ) as buffer:

        shutil.copyfileobj(

            file.file,

            buffer

        )

    service = DatabaseService(db)

    return service.import_csv(filepath)

# ===================================================
# GET BY ID
# ===================================================

@router.get(
    "/{alumni_id}",
    response_model=AlumniResponse
)
def get_alumni(

    alumni_id: int,

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    alumni = service.get_alumni_by_id(alumni_id)

    if alumni is None:

        raise HTTPException(
            status_code=404,
            detail="Alumni not found"
        )

    return alumni


# ===================================================
# UPDATE
# ===================================================

@router.put(
    "/{alumni_id}",
    response_model=AlumniResponse
)
def update_alumni(

    alumni_id: int,

    alumni: AlumniCreate,

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    updated = service.update_alumni(

        alumni_id,

        alumni

    )

    if updated is None:

        raise HTTPException(

            status_code=404,

            detail="Alumni not found"

        )

    return updated


# ===================================================
# DELETE
# ===================================================

@router.delete(
    "/{alumni_id}"
)
def delete_alumni(

    alumni_id: int,

    current_user=Depends(get_current_active_user),

    db: Session = Depends(get_db)

):

    service = DatabaseService(db)

    deleted = service.delete_alumni(

        alumni_id

    )

    if not deleted:

        raise HTTPException(

            status_code=404,

            detail="Alumni not found"

        )

    return {

        "success": True,

        "message": "Alumni deleted successfully"

    }
