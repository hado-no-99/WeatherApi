from fastapi import Request


def req_validation_error_handler(request: Request, exc: Exception):
	return type(exc)