from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Login Page
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "user" and password == "12345678":
        return RedirectResponse("/home", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

# Main Option Page
@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Redirect APIs
@app.get("/api/text-translation")
async def text_translation_redirect():
    return RedirectResponse("https://c5d160a8c2941867ca.gradio.live")

@app.get("/api/video-transcript")
async def video_transcript_redirect():
    return RedirectResponse("https://9c43f415a3639a4076.gradio.live/")
