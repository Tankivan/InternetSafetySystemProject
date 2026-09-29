from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_main_page(request: Request):
    return templates.TemplateResponse({"request": request}, "index.html")


@app.get("/role_selection", response_class=HTMLResponse)
async def read_role_selection(request: Request):
    return templates.TemplateResponse({"request": request}, "role_selection.html")


@app.get("/choose_mode", response_class=HTMLResponse)
async def read_mode_selection(request: Request):
    return templates.TemplateResponse({"request": request}, "mode_selection.html")

@app.get("/questions", responce_class=HTMLResponse)
async def read_questions(request: Request)
    return templates.TemplateResponse({"request": request}, "questions.html")

@app.get("/answers", responce_class=HTMLResponse)
async def read_answers(request: Request)
    return templates.TemplateResponse({"request": request}, "answers.html")

