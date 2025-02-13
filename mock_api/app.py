from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI()


# Load data from a JSON file at the start
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)


# Endpoint that reads data from the JSON file and returns it
@app.get("/data")
async def get_data():
    data = load_data()
    return JSONResponse(content=data)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
