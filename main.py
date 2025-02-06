from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import math

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def get_homepage():
    return ORJSONResponse({"message": "Welcome"}, status_code=200)

@app.get('/api/classify-number')
def get_funfact(number: str = None):
    try:
        if number is None or not number.lstrip('-').isdigit():
            return ORJSONResponse(
                {   "number": f"{number}",
                    "error": True
                    }, status_code=400)

        number = int(number)

        result = {
            "number": number,
            "is_prime": False,
            "is_perfect": False, 
            "properties": [],
            "digit_sum": sum(int(digit) for digit in str(abs(number))),
            "fun_fact": None
        }

        if number > 1:
            if number == 2 or number == 3:
                result["is_prime"] = True
            elif number % 2 == 0 or number % 3 == 0:
                result["is_prime"] = False
            else:
                for i in range(5, int(math.sqrt(number)) + 1, 2):
                    if number % i == 0:
                        result["is_prime"] = False
                        break
                else:
                    result["is_prime"] = True

        if number % 2 == 0:
            result["properties"].append("even")
        else:
            result["properties"].append("odd")

        num_digits = len(str(abs(number)))
        sum_of_powers = sum(int(digit) ** num_digits for digit in str(abs(number)))
        if sum_of_powers == abs(number):
            result["properties"].append("armstrong")

        if number > 1:
            perfect_sum = 1
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    perfect_sum += i
                    if i != number // i:
                        perfect_sum += number // i
            result["is_perfect"] = (perfect_sum == number)


        if number >= 0:
            response = requests.get(f"http://numbersapi.com/{number}")
            result["fun_fact"] = response.text if response.status_code == 200 else "No fun fact available."
        else:
            result["fun_fact"] = "Fun facts are only available for positive numbers."

        return ORJSONResponse(result)

    except Exception as err:
        return ORJSONResponse({"error": f"An error occurred: {str(err)}"}, status_code=500)
