from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', method=['GET'])
def health():
	return jsonify({"status": "healthy"}), 200

@app.route('validate_age',methods=['POST'])
def validate_age():
	data = request.get_json()
	if not data or 'age' not in data:
	return jsonify({"error": "Missing age field"}), 400
	age = data['age']
	if not isinstance(age, int) or age > 150:
	return jsonify({"error": "Age must be an integer between 0 and 150"}), 400
	return jsonify({"valid": True, "message": "Age is valid"}), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
