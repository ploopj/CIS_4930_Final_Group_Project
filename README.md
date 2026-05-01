# CIS 4930 — Final project

Flask app for tasks (name, start/end dates, notes). Tasks are stored in memory only, so they disappear when the server restarts.

**API**

- `GET /api/tasks` — list tasks as JSON
- `POST /api/tasks` — send JSON: `name`, `start_date`, `end_date`, optional `notes`. Server adds `id`.
- `GET /health` — returns `{"status":"ok"}`

Bad requests get status `400` and `{"error":"..."}`.

Dates are plain strings (ISO-style is fine, e.g. `2026-05-01`).

**Run (venv)**

```text
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --debug
```

**Run (Docker)**

```text
docker compose build
docker compose up -d
```

Stop: `docker compose down`.

If `docker compose` isn’t available, try `docker-compose`.

**Quick checks**

```text
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/api/tasks
```

Example POST:

```text
curl -X POST http://127.0.0.1:5000/api/tasks -H "Content-Type: application/json" -d "{\"name\":\"Demo\",\"start_date\":\"2026-05-01\",\"end_date\":\"2026-05-15\",\"notes\":\"hello\"}"
```
