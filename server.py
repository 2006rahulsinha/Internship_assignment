from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory data storage
tasks = [
    {
        "id": 1,
        "title": "Complete project proposal",
        "description": "Finish the Q1 project proposal and submit to management",
        "status": "In Progress",
        "priority": "High",
        "dueDate": "2026-02-15"
    },
    {
        "id": 2,
        "title": "Review code changes",
        "description": "Review pull requests from the development team",
        "status": "Pending",
        "priority": "Medium",
        "dueDate": "2026-02-10"
    },
    {
        "id": 3,
        "title": "Update documentation",
        "description": "Update API documentation with new endpoints",
        "status": "Completed",
        "priority": "Low",
        "dueDate": "2026-01-30"
    },
    {
        "id": 4,
        "title": "Team meeting preparation",
        "description": "Prepare slides and agenda for weekly team sync",
        "status": "Pending",
        "priority": "Medium",
        "dueDate": "2026-02-05"
    },
    {
        "id": 5,
        "title": "Bug fix deployment",
        "description": "Deploy critical bug fixes to production environment",
        "status": "In Progress",
        "priority": "High",
        "dueDate": "2026-02-02"
    }
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(tasks)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    task = next((t for t in tasks if t['id'] == item_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Item not found"}), 404

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    return jsonify({
        "message": "Item received successfully!",
        "received": data
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
