from fastapi import FastAPI, Request

from database import Base, engine
from models import user, organization, source
from routers import sources, users, organizations, login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "http://localhost:3004",
    "http://localhost:3005",
    "http://localhost:3006",
    "http://localhost:3007",
    "http://localhost:3008",
    "http://localhost:3009",
    "http://localhost:3010",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine, tables=[
        user.User.__table__,
        organization.Organization.__table__,
        source.Source.__table__
    ])


app.include_router(users.router)
app.include_router(organizations.router)
app.include_router(sources.router)
app.include_router(login.router)
