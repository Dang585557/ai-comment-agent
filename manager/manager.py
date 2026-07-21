"""Main AI Manager for AI-COMPANY."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
import json
import logging

from manager.dispatcher import Dispatcher
from manager.planner import Planner
from manager.report_generator import ReportGenerator
from manager.scheduler import Scheduler
from manager.task_queue import TaskQueue
from memory.memory_manager import MemoryManager


class AIManager:
    def __init__(self) -> None:
        self.planner = Planner()
        self.dispatcher = Dispatcher()
        self.scheduler = Scheduler()
        self.queue = TaskQueue()
        self.report = ReportGenerator()
        self.memory = MemoryManager()
        self.activities: list[dict[str, Any]] = []
        self.logger = self._build_logger()

    def receive_command(self, command: str) -> dict[str, Any]:
        plan = self.planner.create_plan(command)
        task = self.queue.add(plan)
        self.queue.start_task(task.id)
        self._activity(task.team, "Task started", task.title, 25)

        result = self.dispatcher.dispatch(task.to_dict())
        if result["success"]:
            self.queue.complete_task(task.id, result["output"])
            self._activity(task.team, result["assigned_agent"], result["output"].get("summary", task.title), 100)
        else:
            self.queue.fail_task(task.id, result.get("error", "Unknown error"))
            self._activity(task.team, result["assigned_agent"], result.get("error", "Task failed"), 0)

        record = {
            "task": self.queue.get(task.id).to_dict() if self.queue.get(task.id) else task.to_dict(),
            "dispatch": result,
        }
        self.memory.write("short_term", task.id, record)
        self.memory.conversation_log(command, result["output"].get("summary", result.get("error", "")))
        self._log_event("INFO" if result["success"] else "ERROR", f"{task.team} task {result['status']}: {task.title}")

        return {
            "success": result["success"],
            "task_id": task.id,
            "team": task.team,
            "agent": result["assigned_agent"],
            "status": result["status"],
            "output": result["output"],
            "error": result.get("error"),
            "created_at": task.created_at,
        }

    def dispatch(self, task: dict[str, Any]) -> dict[str, Any]:
        return self.dispatcher.dispatch(task)

    def schedule(self, task: dict[str, Any]) -> dict[str, Any]:
        return self.scheduler.schedule(task)

    def system_status(self) -> dict[str, Any]:
        summary = self.queue.summary()
        return {
            "status": "ONLINE",
            "health": 98 if summary["failed"] == 0 else 82,
            "agents": len(self.dispatcher.available()),
            "queue": summary,
            "memory": self.memory.list_memory(),
            "time": datetime.now().isoformat(timespec="seconds"),
        }

    def daily_report(self) -> dict[str, Any]:
        return self.report.generate(
            {
                "tasks": self.queue.summary(),
                "activities": self.activities[-10:],
                "memory": self.memory.list_memory(),
            }
        )

    def dashboard_cards(self) -> dict[str, Any]:
        summary = self.queue.summary()
        return {
            "total_agents": 56,
            "active_tasks": summary["running"] + summary["pending"],
            "completed_today": summary["completed"],
            "system_health": 98 if summary["failed"] == 0 else 82,
            "storage_used": "2.4 TB",
            "api_calls_today": 18567,
        }

    def list_tasks(self) -> list[dict[str, Any]]:
        return [task.to_dict() for task in reversed(self.queue.get_all())]

    def list_activities(self) -> list[dict[str, Any]]:
        if self.activities:
            return list(reversed(self.activities[-8:]))
        return [
            {"agent": "TikTok Content Agent", "message": "Generating a new short video", "team": "tiktok", "progress": 75, "time": "2 min ago"},
            {"agent": "Video Editor Agent", "message": "Rendering video timeline", "team": "video", "progress": 60, "time": "4 min ago"},
            {"agent": "Developer Agent", "message": "Building Dashboard Module", "team": "developer", "progress": 30, "time": "10 min ago"},
            {"agent": "Research Agent", "message": "Analyzing competitor content", "team": "research", "progress": 95, "time": "6 min ago"},
            {"agent": "Website Agent", "message": "Deploying website updates", "team": "website", "progress": 100, "time": "8 min ago"},
        ]

    def list_logs(self) -> list[dict[str, Any]]:
        log_file = Path("logs/system/system.log")
        if not log_file.exists():
            return [{"level": "INFO", "message": "System ready", "time": datetime.now().strftime("%H:%M:%S")}]
        lines = log_file.read_text(encoding="utf-8").splitlines()[-20:]
        return [{"level": self._level_from_line(line), "message": line, "time": line[:8] if len(line) > 8 else ""} for line in lines]

    def _activity(self, team: str, agent: str, message: str, progress: int) -> None:
        self.activities.append(
            {
                "agent": agent,
                "message": message,
                "team": team,
                "progress": progress,
                "time": datetime.now().strftime("%H:%M:%S"),
            }
        )

    def _build_logger(self) -> logging.Logger:
        Path("logs/system").mkdir(parents=True, exist_ok=True)
        logger = logging.getLogger("ai_company")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            handler = logging.FileHandler("logs/system/system.log", encoding="utf-8")
            handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%H:%M:%S"))
            logger.addHandler(handler)
        return logger

    def _log_event(self, level: str, message: str) -> None:
        getattr(self.logger, level.lower(), self.logger.info)(message)

    def _level_from_line(self, line: str) -> str:
        for level in ["ERROR", "WARNING", "SUCCESS", "INFO"]:
            if level in line:
                return level
        return "INFO"


Manager = AIManager


if __name__ == "__main__":
    manager = AIManager()
    print(json.dumps(manager.receive_command("สร้างคลิป TikTok 10 คลิป"), indent=2, ensure_ascii=False))
    print(json.dumps(manager.system_status(), indent=2, ensure_ascii=False))
