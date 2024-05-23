from fastapi import FastAPI
from starlette.middleware.exceptions import ExceptionMiddleware

app = FastAPI(debug=True)

app = ExceptionMiddleware(app)