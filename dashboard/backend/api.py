"""FastAPI backend for the AI-COMPANY dashboard."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ceo.command_center import CommandCenter


app = FastAPI(title="AI-COMPANY Dashboard API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

command_center = CommandCenter()


class CommandRequest(BaseModel):
    command: str


@app.get("/")
def root() -> dict[str, Any]:
    return {
        "project": "AI-COMPANY",
        "status": "ONLINE",
        "time": datetime.now().isoformat(timespec="seconds"),
    }


@app.post("/command")
def execute_command(payload: CommandRequest) -> dict[str, Any]:
    return command_center.execute(payload.command)


@app.get("/system/status")
def system_status() -> dict[str, Any]:
    return command_center.system_status()


@app.get("/dashboard/cards")
def dashboard_cards() -> dict[str, Any]:
    return command_center.manager.dashboard_cards()


@app.get("/tasks")
def tasks() -> list[dict[str, Any]]:
    return command_center.manager.list_tasks()


@app.get("/activities")
def activities() -> list[dict[str, Any]]:
    return command_center.manager.list_activities()


@app.get("/logs")
def logs() -> list[dict[str, Any]]:
    return command_center.manager.list_logs()


@app.get("/memory/search")
def memory_search(q: str = "", bucket: str | None = None) -> list[dict[str, Any]]:
    return command_center.manager.memory.search(q, bucket=bucket)


@app.get("/teams")
def teams() -> list[dict[str, Any]]:
    return [
        {"name": "TikTok Team", "team": "tiktok", "status": "ONLINE", "agents": 8, "performance": 75},
        {"name": "Video Team", "team": "video", "status": "ONLINE", "agents": 6, "performance": 60},
        {"name": "Developer Team", "team": "developer", "status": "ONLINE", "agents": 10, "performance": 90},
        {"name": "Research Team", "team": "research", "status": "ONLINE", "agents": 6, "performance": 85},
        {"name": "Website Team", "team": "website", "status": "ONLINE", "agents": 4, "performance": 80},
    ]


@app.get("/devices")
def devices() -> list[dict[str, Any]]:
    return [
        {"name": "Cloud PC #1", "type": "Windows 11", "status": "ONLINE"},
        {"name": "Cloud PC #2", "type": "Windows 11", "status": "OFFLINE"},
        {"name": "Android Device #1", "type": "Android", "status": "ONLINE"},
        {"name": "Android Device #2", "type": "Android", "status": "ONLINE"},
        {"name": "iOS Device #1", "type": "iOS", "status": "ONLINE"},
    ]


@app.get("/reports/daily")
def daily_report() -> dict[str, Any]:
    return command_center.daily_report()
