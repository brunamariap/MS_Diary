from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from prisma.models import Gradle
from prisma.partials import GradleRequest
from typing import Coroutine, Any

class GradeRepository:
    
		def create(self, request: GradleRequest) -> Coroutine[Any, Any, Gradle]:
			return Gradle.prisma().create(request)
		
		def get_all(self) -> Coroutine[Any, Any, Gradle]:
			return Gradle.prisma().find_many()