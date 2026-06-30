class Database:
    def __enter__(self):
        print("Conected to database...!!!")
        return self

    def __exit__(self, exc_type, exc, tb):
        
        if exc:
            print(f"Error: {exc}")

        print("Disconnected from database...!!!")
        return True  # Suppress the exception

with Database():
    print("Processing data...!!!")   
    raise Exception("Oops!!!")      