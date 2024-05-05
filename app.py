import uvicorn
from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from spider.common.enums import School
from spider.core.wangxiao import WangXiao168

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/frontend/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return Response(
        "Hello World",

    )


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    with open("web/frontend/templates/login.html", "r") as f:
        html_content = f.read()

    return HTMLResponse(html_content)


@app.post("/login", response_class=JSONResponse)
def post_login(request: Request, username: str = Form(...), password: str = Form(...)):
    wx = WangXiao168(school=School.xatu)
    login_data = wx.do_login(username=username, password=password)

    return JSONResponse(content=login_data)


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=46631, reload=True)
