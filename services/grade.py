from repository.grade import GradeRepository
from prisma.partials import CreateGradleBody
from fastapi import Depends
from prisma.models import Gradle

class GradeService:
		
		def __init__(self):
				self.gradeRepository = GradeRepository()
				
    
		async def create_grade(self, request: CreateGradleBody) -> Gradle:
				return await self.gradeRepository.create(request)
