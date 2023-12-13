from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

from database import Base, engine
from models import user, organization, source
from routers import user, organization, source

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.on_event("startup")
def startup_event():
    # Move the create_all call to the startup event
    Base.metadata.create_all(bind=engine, tables=[
        user.User.__table__,
        organization.Organization.__table__,
        source.Source.__table__
    ])


app.include_router(user.router)
app.include_router(organization.router)
app.include_router(source.router)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
