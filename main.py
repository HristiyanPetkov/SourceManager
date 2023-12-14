from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

from database import Base, engine
from models import user, organization, source
from routers import users, organizations, sources

templates = Jinja2Templates(directory="templates")

app = FastAPI()


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


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
