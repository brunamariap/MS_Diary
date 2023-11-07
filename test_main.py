from fastapi.testclient import TestClient
from main import app
import pytest
from prisma import Prisma


client = TestClient(app)

prisma = Prisma()

# @pytest.fixture(scope="function")
# async def swtup():
#     await prisma.connect()
#     yield prisma
#     await prisma.disconnect()

# @app.on_event("startup")
# async def startup_event():
#     await prisma.connect()

# @app.on_event("shutdown")
# async def shutdown_event():
#     await prisma.disconnect()

# pytest_plugins = ('pytest_asyncio',)


def test_simple():
    # await asyncio.sleep(0.5)
    prisma.connect()
    print('connect', prisma.is_connected())
    response = client.get("/diaries/all")
    print(response)
    prisma.disconnect()
    assert True

# @pytest.mark.asyncio
# async def test_read_all_diaries():
#     # prisma.connect()
#     response = client.get("/diaries/all")
#     assert response.status_code == 200
#     await prisma.disconnect()
#     # assert True

# def test_read_all_grades():
#     # await prisma.connect()
#     # response = client.get("/grades/all")
#     # assert response.status_code == 200
#     # await prisma.disconnect()
#     assert True