"""task tracker api."""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

_tasks: list[dict] = []
_next_id = 1

"""check the payload is valid"""
def _validate_payload(data: dict) -> tuple[bool, str]:
    if not isinstance(data, dict):
        return False, "JSON object required"
    name = data.get("name")
    if not name or not str(name).strip():
        return False, "name is required"
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    if not start_date or not str(start_date).strip():
        return False, "start_date is required"
    if not end_date or not str(end_date).strip():
        return False, "end_date is required"
    return True, ""

#serve the frontend
@app.get("/")
def index():
    return render_template("index.html")

#api info (was previously at /)
@app.get("/api")
def api_info():
    return jsonify(
        service="task-tracker",
        health="/health",
        tasks="/api/tasks",
    )

#list the tasks
@app.get("/api/tasks")
def list_tasks():
    return jsonify(_tasks)


#create a task
@app.post("/api/tasks")
def create_task():
    global _next_id
    data = request.get_json(silent=True) or {}
    ok, err = _validate_payload(data)
    if not ok:
        return jsonify({"error": err}), 400

    notes = data.get("notes") or ""
    task = {
        "id": _next_id,
        "name": str(data["name"]).strip(),
        "start_date": str(data["start_date"]).strip(),
        "end_date": str(data["end_date"]).strip(),
        "notes": str(notes).strip(),
    }
    _next_id += 1
    _tasks.append(task)
    return jsonify(task), 201

#check the health of the server
@app.get("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)