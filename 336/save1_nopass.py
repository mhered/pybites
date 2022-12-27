from fastapi import FastAPI # 1) import FastAPI

my_app = FastAPI()  # 2) create a FastAPI instance in the variable my_app

@my_app.get("/")  # 3) define a path operation decorator for GET requests to the URL "/"
async def root():  # 4) write the path operation function
    return {"message": "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"}  # 5) return the content