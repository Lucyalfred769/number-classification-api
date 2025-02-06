from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)

def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        num = request.args.get('number', type=int)
        if num is None:
            raise ValueError

        armstrong = is_armstrong(num)
        prime = is_prime(num)
        perfect = is_perfect(num)
        digit_sum = sum(int(d) for d in str(num))

        properties = []
        if armstrong:
            properties.append("armstrong")
        properties.append("odd" if num % 2 else "even")

        fun_fact_url = f"http://numbersapi.com/{num}/math"
        fun_fact_response = requests.get(fun_fact_url)
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact found."

        return jsonify({
            "number": num,
            "is_prime": prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }), 200
    except ValueError:
        return jsonify({"number": "invalid", "error": True}), 400

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)  # Enable CORS

# Function to check if a number is Armstrong
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to check if a number is perfect
def is_perfect(num):
    return sum(i for i in range(1, num) if num % i == 0) == num

# API Route
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        num = request.args.get('number', type=int)  # Get the number from request
        if num is None:
            raise ValueError  # Handle missing number

        armstrong = is_armstrong(num)
        prime = is_prime(num)
        perfect = is_perfect(num)
        digit_sum = sum(int(d) for d in str(num))

        # Determine properties
        properties = []
        if armstrong:
            properties.append("armstrong")
        properties.append("odd" if num % 2 else "even")

        # Get Fun Fact from NumbersAPI
        fun_fact_url = f"http://numbersapi.com/{num}/math"
        fun_fact_response = requests.get(fun_fact_url)
        fun_fact = fun_fact_response.text if fun_fact_response.status_code == 200 else "No fun fact found."

        return jsonify({
            "number": num,
            "is_prime": prime,
            "is_perfect": perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }), 200
    except ValueError:
        return jsonify({"number": "invalid", "error": True}), 400

if __name__ == '__main__':
    app.run(debug=True)
