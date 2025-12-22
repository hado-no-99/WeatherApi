from time import time
from fastapi import HTTPException, Request

window_time = 0
window_IPs = {}


def ratelimit(request: Request, max_counter: int = 5, max_session_time: int = 20):
	global window_time, window_IPs
	current_ip = request.client.host
	check_current_window(max_session_time)
	if not current_ip in window_IPs:
		window_IPs[current_ip] = 1
		print(f"hit registered --> {window_IPs[current_ip]}  IP_Pool : {current_ip} Time_Window: {window_time} Current time: {time()}")
	else:
		hit_counter = window_IPs[current_ip]
		if hit_counter >= 5:
			print(f"Max HIT Reached --> {hit_counter} IP_Pool: {window_IPs} Time_Window: {window_time} Current_Time: {time()}")
			raise HTTPException(status_code=429, detail=f"Too many requests\nBlocking IP : {current_ip}\nRetry After : {int(window_time - time())} seconds")
		window_IPs[current_ip] += 1
		print(f"hit registered --> {window_IPs[current_ip]}  IP_Pool: {window_IPs} Time_Window: {window_time} Current time: {time()}")

	# current_time = time()
	# if current_ip == session_ip and current_time <= session_time:
	# 	if hit_counter < max_counter:
	# 		hit_counter += 1
	# 		print(f"Hit counter increased --> ")
	# 		print(f"Session :{session_time}, IP: {session_ip}, hit_counter: {hit_counter}")
	# 		return True
	# 	print(f"Hit counter reached its maximum --> {hit_counter}")
	# 	print(f"Session :{session_time}, IP: {session_ip}, hit_counter: {hit_counter}")
	# 	raise HTTPException(status_code=429, detail="Too many requests")
	# else:
	# 	session_time = time() + max_session_time
	# 	hit_counter = 1
	# 	session_ip = current_ip
	# 	print(f"Time exceeded or a new request. Time: {session_time}, IP: {current_ip}")
	# 	print(f"Session :{session_time}, IP: {session_ip}, hit_counter: {hit_counter}")
	# 	return True


def check_current_window(max_session_time):
	global window_time, window_IPs
	current_time = time()
	print(current_time)
	if window_time == 0 or current_time > window_time:
		print("time resetted")
		window_time = current_time + max_session_time
		window_IPs = {}