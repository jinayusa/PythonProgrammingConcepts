from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database
users = {
    1: {'name': 'Jinay', 'age': 25},
    2: {'name': 'Shah', 'age': 30}
}

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    user_id = len(users) + 1
    users[user_id] = new_user
    return jsonify({'id': user_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
