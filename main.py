from fastapi import FastAPI
from prisma import Prisma
from controllers import grade, diary
from contextlib import asynccontextmanager, contextmanager

app = FastAPI()
app.include_router(grade.router)
app.include_router(diary.router)

prisma = Prisma(auto_register=True)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Load the ML model
#     # ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
#     await prisma.connect()
#     yield
#     await prisma.disconnect()
#     # Clean up the ML models and release the resources
#     # ml_models.clear()


@app.on_event("startup")
def startup():
    prisma.connect()

@app.on_event("shutdown")
def shutdown():
    prisma.disconnect()