# Task Manager REST API

A lightweight RESTful API built with **Python** and **FastAPI** to manage tasks with full CRUD capabilities and auto-generated interactive Swagger documentation.

---

## 🛠️ Tech Stack & Tools

- **Language:** Python 3.14+
- **Framework:** FastAPI
- **Data Validation:** Pydantic
- **Development Server:** Uvicorn

---

## ✨ Features

- **Create Task (`POST /tasks`):** Add new tasks with title, optional description, and automatic ID assignment.
- **Read All Tasks (`GET /tasks`):** Fetch the entire list of tasks.
- **Read Single Task (`GET /tasks/{task_id}`):** Retrieve details of a specific task by its ID.
- **Update Task (`PUT /tasks/{task_id}`):** Modify existing task details or status.
- **Delete Task (`DELETE /tasks/{task_id}`):** Remove a task from the list.
- **Auto Docs:** Interactive Swagger UI for live testing.

---

## 🚀 How to Run Locally

### 1. Repository Clone Karein
```bash
git clone [https://github.com/UmangBheda/task-api.git](https://github.com/UmangBheda/task-api.git)
cd task-api
