from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from prisma.partials import DiaryRequest
from .test_base import TestBase
from main import app
from prisma.models import Diary
import datetime

client = TestClient(app)
prefix = "/diaries"


class TestApp(TestBase):

    def test_get_all_diaries(self, setUp):
        response = client.get(f"{prefix}/all")

        assert response

    def test_create_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }
        request = DiaryRequest(**diary)

        response = Diary.prisma().create(diary)
        # print(response)
        assert response
        # assert response.json() == diary

    def test_edit_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }

        edited_diary = {
            "referencePeriod": 1,
            "referenceYear": 2024,
            "startDate": day,
            "endDate": day
        }

        response_create_diary = Diary.prisma().create(diary)
        diary_id = response_create_diary.id

        response = Diary.prisma().update(data=edited_diary, where={
            "id": diary_id
        })
        
        assert response

    def test_delete_diary(self, setUp):
        day = datetime.datetime.utcnow().isoformat() + 'Z'
        diary = {
            "referencePeriod": 2,
            "referenceYear": 2023,
            "startDate": day,
            "endDate": day
        }
        
        response_create_diary = Diary.prisma().create(diary)
        diary_id = response_create_diary.id

        response = Diary.prisma().delete(where={"id": diary_id})
        
        assert response
