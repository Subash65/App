from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants for user information
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    # GET request does not take any input and returns a hardcoded response
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Get JSON data from the request
        data = request.json.get("data", [])
        
        # Validate input
        if not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid input format"}), 400

        # Initialize lists for numbers and alphabets
        numbers = []
        alphabets = []
        highest_lowercase_alphabet = []

        # Process the data
        for item in data:
            if item.isdigit():
                numbers.append(item)
            elif item.isalpha():
                alphabets.append(item)
        
        # Find the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        if lowercase_alphabets:
            highest_lowercase_alphabet.append(max(lowercase_alphabets))
        
        # Prepare the response
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }

        return jsonify(response), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
