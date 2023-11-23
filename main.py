from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory='templates')

class LoginBody(BaseModel):
   username: str
   password: str

@app.get("/")
async def root(request: Request):
   return templates.TemplateResponse('index.html', {'request': request})


@app.post("/login")
async def login(login_data: LoginBody):
   print(f"username: {login_data.username}, password: {login_data.password}")
   return {"ok": True}
