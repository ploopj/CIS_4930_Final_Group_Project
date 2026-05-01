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

## Screenshots
### Jenkins Home Page
![Jenkins Home Page](Screenshots/jenkins-home.png)
Jenkins home page that lists our project.


### Jenkins Build Page
![Jenkins Build Page](Screenshots/jenkins-build.png)
Our Jenkins configuration is successfully running with our Jenkinsfile setup.

### Skeleton Page
![Pretty Print](Screenshots/pretty-print.png)
This was our skeleton website that ran with all of our files. We will build off of this

### Task Tracker Project
![Pretty Print](Screenshots/task-tracker.png)
This is our finalized project. It is a simple task tracker that lets you create a list of 
tasks to stay organized. Jenkins automates the process of running our code with the help of 
Docker.
