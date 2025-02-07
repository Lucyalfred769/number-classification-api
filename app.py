from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    sum_powers = sum(int(digit) ** power for digit in num_str)
    return sum_powers == n

def get_digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def get_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    return properties

def get_fun_fact(n):
    try:
        response = requests.get(f"http://numbersapi.com/{n}/math")
        if response.status_code == 200:
            return response.text
        return f"{n} is {'even' if n % 2 == 0 else 'odd'}"
    except:
        return f"{n} is {'even' if n % 2 == 0 else 'odd'}"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    try:
        # Get number parameter and validate
        number = request.args.get('number', type=str)
        if not number or not number.lstrip('-').isdigit():
            return jsonify({
                "number": number,
                "error": True
            }), 400
        
        # Convert to integer
        num = int(number)
        
        # Calculate properties
        properties = get_properties(abs(num))
        
        # Get fun fact
        fun_fact = get_fun_fact(num)
        
        # Prepare response
        response = {
            "number": num,
            "is_prime": is_prime(abs(num)),
            "is_perfect": is_perfect(abs(num)),
            "properties": properties,
            "digit_sum": get_digit_sum(num),
            "fun_fact": fun_fact
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({
            "number": number if 'number' in locals() else None,
            "error": True
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
