from fastapi import FastAPI, Depends
from prisma import Prisma
from controllers import grade

app = FastAPI()
app.include_router(grade.router)

prisma = Prisma(auto_register=True)

@app.on_event("startup")
async def startup():
    await prisma.connect()

@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()