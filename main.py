# print("hello baby")
from fastapi import FastAPI
from src.module import func

app = FastAPI()

@app.get('/')
def first_page():
    return func()

# if __name__ == "__main__":
#     app.

#uvicorn main:app

