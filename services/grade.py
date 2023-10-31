from repository.grade import GradeRepository
from prisma.partials import GradleRequest
from fastapi import Depends
from prisma.models import Gradle

class GradeService:
		
		def __init__(self):
				self.service = GradeRepository()
		
		def create(self, request: GradleRequest):
				return self.service.create(request)
		
		def get_all(self):
			return self.service.get_all()
		
		def get_by_id(self, id: str):
			return self.service.get_by_id(id)

		def change(self, id: str, request: GradleRequest):
			return self.service.change(id, request)

		def remove(self, id: str):
			return self.service.remove(id)