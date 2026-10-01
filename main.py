from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    # title is required - must be a text string
    title: str
    # description is optional - defaults to nothing
    description: str | None = None
    # status defaults to "pending" if not provided
    status: str = "pending"

# Store tasks in a list (acts as our database)
tasks = []
# Give each task a unique ID number
task_id_counter = 0



@app.post("/tasks", status_code=201)
def create_task(task: Task):
    # Use the counter from outside this function
    global task_id_counter
    # Give this task a unique ID
    task_id_counter += 1
    # Convert the task object to a dictionary
    task_data = task.model_dump()
    # Add the ID to the dictionary
    task_data["id"] = task_id_counter
    # Store the task in our list
    tasks.append(task_data)
    # Send the created task back
    return task_data

@app.get("/tasks")
def get_tasks():
    return tasks
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    # Loop through tasks with their position numbers
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            # Convert updated task to dictionary
            task_data = updated_task.model_dump()
            # Keep the same ID
            task_data["id"] = task_id
            # Replace the old task at this position
            tasks[index] = task_data
            return task_data
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # Loop through tasks with their position numbers
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            # Remove the task at this position
            tasks.pop(index)
            return {"message": "Task deleted"}
    return {"error": "Task not found"}