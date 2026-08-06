from fastapi import FastAPI



app = FastAPI()


@app.api_route(methods=["QUERY"])
def hello_world():
    return "Hello, World!"

