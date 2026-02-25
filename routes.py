from fastapi import APIRouter, HTTPException
from app.models import Task
from app.database import collection
from bson import ObjectId

router = APIRouter()

# Create Task
@router.post("/tasks")
def create_task(task: Task):
    result = collection.insert_one(task.dict())
    return {"id": str(result.inserted_id)}

# Get All Tasks
@router.get("/tasks")
def get_tasks():
    tasks = []
    for task in collection.find():
        task["_id"] = str(task["_id"])
        tasks.append(task)
    return tasks

# Get Single Task
@router.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["_id"] = str(task["_id"])
    return task

# Update Task
@router.put("/tasks/{task_id}")
def update_task(task_id: str, task: Task):
    collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": task.dict()}
    )
    return {"message": "Updated successfully"}

# Delete Task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    collection.delete_one({"_id": ObjectId(task_id)})
    return {"message": "Deleted successfully"}