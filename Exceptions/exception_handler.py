from fastapi import FastAPI, RequestValidationError

app = FastAPI()

@app.exception_handler(RequestValidationError)
def validation_error_handler(req, excep):
	return type(excep)