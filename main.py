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

uniquenumber_api = {
    1: {
        "number": "",
        "is_prime": "",
        "is_perfect": "",
        "properties": "",
        "digit_sum": "",
        "fun_fact": ""
    }
}

@app.get('/')
def get_homepage():
    try:
        return ORJSONResponse(
            {"message": "Welcome"}, status_code=200
        )
    except Exception as err:
        return ORJSONResponse(
            {"error": f"{str(err)}"}, status_code=500
        )
    
@app.get('/api/classify-number')
def get_funfact(number: str=None):
    try:
        # return number
        uniquenumber_api[1]["number"] = int(number)

        # check for prime
        if int(number) % 2 == 0 or int(number) % 3 == 0:
            uniquenumber_api[1]["is_prime"] = False
        else: 
            uniquenumber_api[1]["is_prime"] = True 

        # check for properties
        properties = []
        num_digits = len(number)
        sum_of_powers = 0

        for i in number:
            sum_of_powers += int(i) ** num_digits

        is_armstrong = sum_of_powers == int(number)
        if is_armstrong:
            properties.append("armstrong")

        if int(number) % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        uniquenumber_api[1]["properties"] = properties

        # logic of digit_sum
        result = 0
        for i in number:   
            result += int(i)      
            uniquenumber_api[1]["digit_sum"] = result

        # check for perfect number
        if int(number) < 2:
            is_perfect = False
        else:
            perfect_result = 1
            for i in range(2, int(math.sqrt(int(number))) + 1):
                if int(number) % i == 0:
                    perfect_result += i
                    if i != int(number) // i:
                        perfect_result += int(number) // i

            is_perfect = perfect_result == int(number)

        uniquenumber_api[1]["is_perfect"] = is_perfect

        # logic to return fun_fact
        response = requests.get(f"http://numbersapi.com/{number}")
        fun_fact = response.text

        uniquenumber_api[1]["fun_fact"] = fun_fact
        

        return ORJSONResponse(uniquenumber_api[1])
    except:
        if not number or not number.lstrip('-').isdigit():
            return ORJSONResponse(
                {   "number": "alphabet",
                    "error": True
                    }
            )