from prisma.models import Gradle
from prisma.partials import GradleRequest

class GradeRepository:
		
		def create(self, request: GradleRequest):
			return Gradle.prisma().create(request)
		
		def get_all(self):
			return Gradle.prisma().find_many(include={ 'diary': True })
		
		def get_by_id(self):
			pass

		def change(self, id: str, request: GradleRequest):
			return Gradle.prisma().update(data=request, where={'id': id})

		def remove(self, id: str):
			return Gradle.prisma().delete({ 'id': id })