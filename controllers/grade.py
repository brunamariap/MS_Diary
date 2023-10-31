from fastapi import APIRouter
from services.grade import GradeService
from prisma.models import Gradle
from prisma.partials import GradleRequest, GradleResponse
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter(prefix="/grades", tags=['Grades'])
gradeService = GradeService()


@router.get("/all")
async def insert_grade() -> List[GradleResponse]:
    response = await gradeService.list_all_grades()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=200)

@router.post("/create")
async def insert_grade(request: GradleRequest) -> GradleResponse:
    body: GradleRequest = request
    response = await gradeService.create_grade(body.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=200)