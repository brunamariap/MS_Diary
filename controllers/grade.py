from fastapi import APIRouter
from services.grade import GradeService
from prisma.models import Gradle
from prisma.partials import CreateGradleBody
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/grade", tags=['Grades'])
gradeService = GradeService()


@router.post("/")
async def insert_grade(request: CreateGradleBody) -> Gradle:
    body: CreateGradleBody = request
    response = await gradeService.create_grade(body.dict())
    
		
    return JSONResponse(content=jsonable_encoder(response), status_code=200)