from fastapi import APIRouter
from services.diary import DiaryService
from prisma.partials import DiaryRequest, DiaryResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from fastapi import status

router = APIRouter(prefix="/diaries", tags=['Diário'])
diaryService = DiaryService()

@router.get("/all")
async def list_diaries() -> List[DiaryResponse]:
    response = diaryService.get_all()
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.post("/create")
def insert_diary(request: DiaryRequest) -> DiaryResponse:
    response = diaryService.create(request.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.put("/{id}/modify")
async def change_diary(id: str, request: DiaryRequest) -> DiaryResponse:
    response = await diaryService.change(id, request.dict())
		
    return JSONResponse(content=jsonable_encoder(response), status_code=status.HTTP_200_OK)

@router.delete("/remove")
async def remove_diary(id: str) -> DiaryResponse:
    response = await diaryService.remove(id)
    
    if not response:
        return JSONResponse(content={"details": "Não foi encontrado um diário com o id especificado"}, status_code=status.HTTP_404_NOT_FOUND)
    
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)