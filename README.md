# Number Classification API

## Project Description

This FastAPI application classifies numbers based on various mathematical properties. It checks whether a given number is prime, perfect,
or an Armstrong number, and provides additional details such as its parity (odd/even), digit sum, and a fun fact retrieved from an external API.

## Setup Instructions

**Prerequisites:**

- Python 3.6+
- pip

**Installation:**

1. Clone the repository:

   ```
   git clone https://github.com/Inifinitech/my_ess_hng2.gitgit
   ```

2. Install dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## API Documentation

### **Endpoint:**

GET `/api/classify-number?number=<num>`

### **Request Parameters:**

| Parameter | Type | Description            |
| --------- | ---- | ---------------------- |
| number    | int  | The number to classify |

### **Response Format:**

- **Request Example:** `/api/classify-number?number=90`

- **Response:** JSON
  ```json
  {
  "number": 90,
  "is_prime": false,
  "is_perfect": false,
  "properties": [
    "even"
  ],
  "digit_sum": 9,
  "fun_fact": "90 is the latitude of the North Pole and the South Pole."
  }
  ```

### Example Usage: Using CURL:

```
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=90"
```

## Backlink

https://hng.tech/hire/python-developers

### Deployment

The API is deployed at [EndPoint URL](https://your-deployment-url.com/api/classify-number)