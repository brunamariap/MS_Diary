from repository.grade import GradeRepository
from prisma.partials import GradleRequest
from fastapi import Depends
from prisma.models import Gradle

class GradeService:
		
		def __init__(self):
				self.gradeRepository = GradeRepository()
				
    
		def create_grade(self, request: GradleRequest) -> Gradle:
				return self.gradeRepository.create(request)
		
		def list_all_grades(self):
			return self.gradeRepository.get_all()
