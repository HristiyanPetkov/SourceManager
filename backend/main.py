from fastapi import FastAPI, Request

from database import Base, engine
from models import user, organization, source
from routers import sources, users, organizations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost",
    "http://localhost:3000",  # Replace with your React app's URL
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


@app.get("/")
def read_root():
    return {"Hello": "World"}
