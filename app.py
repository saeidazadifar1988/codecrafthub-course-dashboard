"""CodeCraftHub Learning Management Platform - Backend API

In-memory course storage (no database). Run with: python app.py
Serves the dashboard at / and exposes /api/courses CRUD endpoints.
"""
from datetime import datetime
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

# In-memory storage
_courses = []
_next_id = 1

VALID_STATUSES = {"Not Started", "In Progress", "Completed"}


def _serialize(course):
    return {
        "id": course["id"],
        "name": course["name"],
        "description": course["description"],
        "target_date": course["target_date"],
        "status": course["status"],
        "created_at": course["created_at"],
    }


def _validate_body(body, partial=False):
    """Return (cleaned_data, error_message)."""
    errors = []
    if not isinstance(body, dict):
        return None, "Request body must be a JSON object."

    cleaned = {}

    # name
    if "name" in body:
        name = body["name"]
        if not isinstance(name, str) or not name.strip():
            errors.append("name is required.")
        else:
            cleaned["name"] = name.strip()
    elif not partial:
        errors.append("name is required.")

    # description
    if "description" in body:
        desc = body["description"]
        if not isinstance(desc, str) or not desc.strip():
            errors.append("description is required.")
        else:
            cleaned["description"] = desc.strip()
    elif not partial:
        errors.append("description is required.")

    # target_date
    if "target_date" in body:
        td = body["target_date"]
        if not isinstance(td, str) or not td.strip():
            errors.append("target_date is required.")
        else:
            try:
                datetime.strptime(td.strip(), "%Y-%m-%d")
                cleaned["target_date"] = td.strip()
            except ValueError:
                errors.append("target_date must be in YYYY-MM-DD format.")
    elif not partial:
        errors.append("target_date is required.")

    # status
    if "status" in body:
        st = body["status"]
        if not isinstance(st, str) or st.strip() not in VALID_STATUSES:
            errors.append(
                f"status must be one of: {', '.join(sorted(VALID_STATUSES))}."
            )
        else:
            cleaned["status"] = st.strip()
    elif not partial:
        errors.append("status is required.")

    if errors:
        return None, " ".join(errors)
    return cleaned, None


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/courses", methods=["GET"])
def list_courses():
    return jsonify([_serialize(c) for c in _courses]), 200


@app.route("/api/courses", methods=["POST"])
def create_course():
    global _next_id
    cleaned, err = _validate_body(request.get_json(silent=True) or {})
    if err:
        return jsonify({"error": err}), 400

    course = {
        "id": _next_id,
        "name": cleaned["name"],
        "description": cleaned["description"],
        "target_date": cleaned["target_date"],
        "status": cleaned["status"],
        "created_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    }
    _next_id += 1
    _courses.append(course)
    return jsonify(_serialize(course)), 201


@app.route("/api/courses/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    cleaned, err = _validate_body(request.get_json(silent=True) or {}, partial=True)
    if err:
        return jsonify({"error": err}), 400

    for course in _courses:
        if course["id"] == course_id:
            course.update(cleaned)
            return jsonify(_serialize(course)), 200
    return jsonify({"error": f"Course with id {course_id} not found."}), 404


@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    for i, course in enumerate(_courses):
        if course["id"] == course_id:
            _courses.pop(i)
            return jsonify({"message": f"Course {course_id} deleted."}), 200
    return jsonify({"error": f"Course with id {course_id} not found."}), 404


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found."}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
