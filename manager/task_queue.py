"""In-memory task queue used by the manager and dashboard API."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any
import uuid


@dataclass
class Task:
    id: str
    title: str
    team: str
    task_type: str = "general"
    status: str = "PENDING"
    priority: str = "NORMAL"
    progress: int = 0
    output: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class TaskQueue:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add(self, task: dict[str, Any]) -> Task:
        new_task = Task(
            id=str(uuid.uuid4()),
            title=task.get("title", "Untitled Task"),
            team=task.get("team", "general"),
            task_type=task.get("task_type", "general"),
            priority=task.get("priority", "NORMAL"),
            status=task.get("status", "PENDING"),
        )
        self.tasks.append(new_task)
        return new_task

    def get(self, task_id: str) -> Task | None:
        return next((task for task in self.tasks if task.id == task_id), None)

    def get_all(self) -> list[Task]:
        return list(self.tasks)

    def get_pending(self) -> list[Task]:
        return [task for task in self.tasks if task.status == "PENDING"]

    def get_running(self) -> list[Task]:
        return [task for task in self.tasks if task.status == "RUNNING"]

    def get_completed(self) -> list[Task]:
        return [task for task in self.tasks if task.status == "COMPLETED"]

    def start_task(self, task_id: str) -> Task | None:
        task = self.get(task_id)
        if task:
            task.status = "RUNNING"
            task.progress = max(task.progress, 10)
            task.updated_at = datetime.now().isoformat(timespec="seconds")
        return task

    def complete_task(self, task_id: str, output: dict[str, Any]) -> Task | None:
        task = self.get(task_id)
        if task:
            task.status = "COMPLETED"
            task.progress = 100
            task.output = output
            task.updated_at = datetime.now().isoformat(timespec="seconds")
        return task

    def fail_task(self, task_id: str, error: str) -> Task | None:
        task = self.get(task_id)
        if task:
            task.status = "FAILED"
            task.error = error
            task.updated_at = datetime.now().isoformat(timespec="seconds")
        return task

    def update_progress(self, task_id: str, progress: int) -> Task | None:
        task = self.get(task_id)
        if task:
            task.progress = max(0, min(100, progress))
            task.status = "COMPLETED" if task.progress == 100 else "RUNNING"
            task.updated_at = datetime.now().isoformat(timespec="seconds")
        return task

    def remove(self, task_id: str) -> bool:
        before = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        return len(self.tasks) != before

    def total_tasks(self) -> int:
        return len(self.tasks)

    def summary(self) -> dict[str, int]:
        return {
            "total": len(self.tasks),
            "pending": len(self.get_pending()),
            "running": len(self.get_running()),
            "completed": len(self.get_completed()),
            "failed": len([task for task in self.tasks if task.status == "FAILED"]),
        }
