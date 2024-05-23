from fastapi import FastAPI
from starlette.middleware.exceptions import ExceptionMiddleware
from db.base_db import engine
from models import post, user

app = FastAPI(debug=True)


user.Base.metadata.create_all(bind=engine)
post.Base.metadata.create_all(bind=engine)


app = ExceptionMiddleware(app)
