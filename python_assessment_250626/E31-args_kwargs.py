#log_event("User Login", "admin", "dashboard", timestamp="10:00 AM", status="Success")
#Expected Output:
#Event: User 
#Login Details: ('admin', 'dashboard') 
#Metadata: {'timestamp': '10:00 AM', 'status': 'Success'}


def log_event(message,*args,**kwargs):
    print(f"Event:{message}")
    print(f"Login Details:{args}")
    print(f"Metadata:{kwargs}")

log_event(
    "User Login",
    "admin", 
    "dashboard",
    timestamp="10:00 AM",
    status="Success"
)    