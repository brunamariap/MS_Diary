from fastapi import FastAPI
from prisma import Prisma
from controllers import grade, diary

app = FastAPI()
app.include_router(grade.router)
app.include_router(diary.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
def startup():
    prisma.connect()

@app.on_event("shutdown")
def shutdown():
    prisma.disconnect()