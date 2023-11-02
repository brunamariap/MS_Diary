from prisma.models import Grade
from prisma.partials import GradeRequest


class GradeRepository:
    def create(self, request: GradeRequest):
        return Grade.prisma().create(request)

    def get_all(self):
        return Grade.prisma().find_many(include={'diary': True})

    def get_by_id(self, id):
        return Grade.prisma().find_unique({'id': id})

    def change(self, id: str, request: GradeRequest):
        return Grade.prisma().update(data=request, where={'id': id})

    def remove(self, id: str):
        return Grade.prisma().delete({'id': id})
