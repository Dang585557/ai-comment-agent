"""
AI-COMPANY
manager/task_queue.py
Task Queue Manager"""
from dataclasses
import dataclass, field
from datetime 
import datetime
from typing 
import List, Dict
import uuid@dataclass
class Task:
    id: str
    title: str
    team: str
    status: str = "PENDING"
    priority: str = "NORMAL"
    progress: int = 0
    created_at: str = field(
    default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
class TaskQueue:
def __init__(self):self.tasks: List[Task] = []
def add(self, task: Dict): new_task = Task(

            id=str(uuid.uuid4()),
            title=task.get("title", "Untitled Task"),
            team=task.get("team", "General"),
            priority=task.get("priority", "NORMAL")
        )
        self.tasks.append(new_task)
        print(f"[QUEUE] Added -> {new_task.title}")
    return new_task
    def get_all(self):
    return self.tasks
    def get_pending(self):
    return [t for t in self.tasks if t.status == "PENDING"]
    def get_running(self):
    return [t for t in self.tasks if t.status == "RUNNING"]
    def get_completed(self):
    return [t for t in self.tasks if t.status == "COMPLETED"]
    def start_task(self, task_id):
    for task in self.tasks:
    if task.id == task_id:   task.status = "RUNNING"
    return task
    return None
    def update_progress(self, task_id, progress):
    for task in self.tasks:
    if task.id == task_id:task.progress = progress
    if progress >= 100:  task.progress = 100 task.status = "COMPLETED"
    return task
    return None
    def remove(self, task_id):self.tasks = [ t for t in self.tasks if t.id != task_id
 ]
    def total_tasks(self):
    return len(self.tasks)
    def summary(self):
    return 
  {
    "total": len(self.tasks),
    "pending": len(self.get_pending()),
    "running": len(self.get_running()),
    "completed": len(self.get_completed())  
  }
