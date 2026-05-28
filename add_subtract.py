"""
Requirements:
-- API user specifies either addition or subtraction
-- provides num1 and num2
-- perform the operation num1 + num2 or num1 - num2
-- handle bad inputs too, return error code

general possible inputs it should handle
-- always a url
-- always to /addsub endpoint
-- always need two numbers, otherwise error
-- specify add, sub, or no action (last one defaults to add)

edge cases
-- lots of them... just defualt to error code
-- do want to handle decimals too

other thoughts


"""

# todo: what does the input string look like
# todo: get it up on Render, auto update with github actions or something
from fastapi import FastAPI

# Initialize the application
app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "Microservice is online and listening."}

# 1. The Client sends an HTTP request to this URL endpoint
# The {user_input} part extracts info from the URL as a parameter
@app.get("/process/{user_input}")
def process_data(user_input: str):
    # 2. The microservice uses the parameter to inform its execution
    processed_string = user_input.upper()
    character_count = len(user_input)

    # 3. The microservice sends back the output
    # FastAPI automatically converts this Python dictionary into JSON format
    return {
        "original": user_input,
        "processed": processed_string,
        "length": character_count,
        "status": "success"
    }