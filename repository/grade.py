from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from prisma.models import Gradle
from prisma.partials import CreateGradleBody
from typing import Coroutine, Any

class GradeRepository:
    
		async def create(self, request: CreateGradleBody) -> Coroutine[Any, Any, Gradle]:
			return await Gradle.prisma().create(request)