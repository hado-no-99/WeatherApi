from time import time
from fastapi import HTTPException, Request

session_time = 0
session_ip = 0
hit_counter = 0

def ratelimit(request: Request, max_counter: int = 5, max_session_time: int = 20):
	global session_time, session_ip, hit_counter
	current_ip = request.client.host
	current_time = time()
	if current_ip == session_ip and current_time <= session_time:
		if hit_counter < max_counter:
			hit_counter += 1
			print(f"Hit counter increased --> ")
			print(f"Session :{session_time}, IP: {session_ip}, hit_counter: {hit_counter}")
			return True
		print(f"Hit counter reached its maximum --> {hit_counter}")
		print(f"Session :{session_time}, IP: {session_ip}, hit_counter: {hit_counter}")
		raise HTTPException(status_code=429, detail="Too many requests")
	else:
		session_time = time() + max_session_time
		hit_counter = 1
		session_ip = current_ip
		print(f"Time exceeded or a new request. Time: {session_time}, IP: {current_ip}")
		print(f"Session :{session_time}, IP: {session_ip}, hit_counter: {hit_counter}")
		return True
