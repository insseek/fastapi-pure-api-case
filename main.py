from fastapi import FastAPI

app = FastAPI()

from routers import users, emails, blogs


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(users.router)
app.include_router(blogs.router)
app.include_router(emails.router)
