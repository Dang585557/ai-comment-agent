"""Task planning for AI-COMPANY."""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Any


@dataclass
class Plan:
    title: str
    team: str
    priority: str
    task_type: str
    status: str = "PENDING"
    created_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        if not data["created_at"]:
            data["created_at"] = datetime.now().isoformat(timespec="seconds")
        return data


class Planner:
    """Turns CEO commands into structured tasks."""

    def __init__(self) -> None:
        self.supported_teams = ["tiktok", "video", "developer", "research", "website"]

    def create_plan(self, command: str) -> dict[str, Any]:
        clean_command = " ".join(command.strip().split())
        if not clean_command:
            raise ValueError("Command cannot be empty")

        plan = Plan(
            title=clean_command,
            team=self.detect_team(clean_command),
            priority=self.detect_priority(clean_command),
            task_type=self.detect_task_type(clean_command),
        )
        return plan.to_dict()

    def detect_team(self, command: str) -> str:
        text = command.lower()
        if any(word in text for word in ["tiktok", "short", "clip", "คลิป"]):
            return "tiktok"
        if any(word in text for word in ["video", "render", "edit", "subtitle"]):
            return "video"
        if any(word in text for word in ["code", "developer", "dashboard", "api", "website module"]):
            return "developer"
        if any(word in text for word in ["research", "competitor", "trend", "วิเคราะห์"]):
            return "research"
        if any(word in text for word in ["website", "deploy", "seo", "landing"]):
            return "website"
        return "general"

    def detect_priority(self, command: str) -> str:
        text = command.lower()
        if any(word in text for word in ["urgent", "ด่วน", "critical", "asap"]):
            return "HIGH"
        if any(word in text for word in ["low", "later", "ภายหลัง"]):
            return "LOW"
        return "NORMAL"

    def detect_task_type(self, command: str) -> str:
        text = command.lower()
        if any(word in text for word in ["report", "รายงาน"]):
            return "report"
        if any(word in text for word in ["create", "generate", "สร้าง"]):
            return "create"
        if any(word in text for word in ["fix", "แก้", "repair"]):
            return "fix"
        if any(word in text for word in ["deploy", "publish"]):
            return "deploy"
        return "general"
