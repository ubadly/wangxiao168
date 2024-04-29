import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return Response(
        "Hello World",

    )


if __name__ == '__main__':
    uvicorn.run("app:app", host='0.0.0.0', port=46631, reload=True)
