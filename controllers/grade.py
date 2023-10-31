from fastapi import APIRouter
from services.grade import GradeService
from prisma.partials import GradleRequest, GradleResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from fastapi import status

router = APIRouter(prefix="/grades", tags=['Grades'])
gradeService = GradeService()

@router.get("/all")
async def list_grades() -> List[GradleResponse]:
    response = await gradeService.get_all()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.get("/{id}/details")
async def get_grade(id: str) -> List[GradleResponse]:
    response = await gradeService.get_by_id(id)
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado notas com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
async def insert_grade(request: GradleRequest) -> GradleResponse:
    body: GradleRequest = request
    response = await gradeService.create(body.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.put("/{id}/modify")
async def change_grade(id: str, request: GradleRequest) -> GradleResponse:
    response = await gradeService.change(id ,request.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
async def remove_grade(id: str) -> None:
    response = await gradeService.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado notas com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
		
    return JSONResponse(content=None, status_code=status.HTTP_204_NO_CONTENT)