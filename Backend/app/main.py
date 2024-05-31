from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from sys import platform

app = FastAPI()
# Добавление обработки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники (лучше указать конкретные домены в продакшене)
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все методы
    allow_headers=["*"],  # Разрешить все заголовки
    expose_headers=["*"],  # Разрешить все заголовки
)

static_dir = ""
generated_images_dir = ""
template_dir = ""

if platform == "linux" or platform == "linux2":
    static_dir = "Backend/app/static"
    generated_images_dir = "Backend/app/generated_images"
    template_dir = "Backend/app/templates"
elif platform == "win32":
    static_dir = "Backend/app/static"
    generated_images_dir = "Backend/app/generated_images"
    template_dir = "Backend/app/templates"

app.mount("/static", StaticFiles(directory=static_dir), name="static")
app.mount("/generated_images", StaticFiles(directory=generated_images_dir), name="generated_images")

templates = Jinja2Templates(directory=template_dir)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
