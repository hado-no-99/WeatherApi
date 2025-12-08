
from fastapi import Depends, FastAPI, Request
from models.endpoint_models import weatherReqParams
from visualCrossingApi.api_request import fetch_weather

app = FastAPI()

@app.get('/{location}')
def get_weather_by_location(request: Request, location: str):
    print(fetch_weather(request.url))
    return {"msg": f"{location} weather", "URL" : f"{request.url}"}


@app.get('/{location}/{datetime1}')
def get_weather_by_location_datetime1(params: weatherReqParams = Depends(weatherReqParams)):
        return {"location": params.location, "datetime1": params.datetime1}

@app.get('/{location}/{datetime1}/{datetime2}')
def get_weather_by_location_datetime1_datetime2(request: Request, params: weatherReqParams = Depends(weatherReqParams)):
    return {"location": params.location, "datetime1": params.datetime1, "datetime2": params.datetime2}


def main():
    print("Hello from weatherapi!")


if __name__ == "__main__":
    main()
