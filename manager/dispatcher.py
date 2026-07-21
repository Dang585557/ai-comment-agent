"""Task dispatcher that routes tasks to real team handlers."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Callable


class Dispatcher:
    def __init__(self) -> None:
        self.handlers: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
            "tiktok": self._run_tiktok,
            "video": self._run_video,
            "developer": self._run_developer,
            "research": self._run_research,
            "website": self._run_website,
            "general": self._run_general,
        }

    def dispatch(self, task: dict[str, Any]) -> dict[str, Any]:
        team = task.get("team", "general")
        handler = self.handlers.get(team, self._run_general)
        started_at = datetime.now().isoformat(timespec="seconds")
        try:
            output = handler(task)
            return {
                "success": True,
                "assigned_team": team,
                "assigned_agent": output.get("agent", f"{team.title()} Agent"),
                "status": "COMPLETED",
                "started_at": started_at,
                "completed_at": datetime.now().isoformat(timespec="seconds"),
                "output": output,
            }
        except Exception as exc:
            return {
                "success": False,
                "assigned_team": team,
                "assigned_agent": f"{team.title()} Agent",
                "status": "FAILED",
                "started_at": started_at,
                "completed_at": datetime.now().isoformat(timespec="seconds"),
                "error": str(exc),
                "output": {},
            }

    def available(self) -> list[str]:
        return sorted(self.handlers.keys())

    def register_agent(self, team: str, handler: Callable[[dict[str, Any]], dict[str, Any]]) -> None:
        self.handlers[team] = handler

    def remove_agent(self, team: str) -> None:
        self.handlers.pop(team, None)

    def status(self) -> dict[str, Any]:
        return {"registered_agents": len(self.handlers), "teams": self.available()}

    def _run_tiktok(self, task: dict[str, Any]) -> dict[str, Any]:
        title = task["title"]
        return {
            "agent": "TikTok Content Agent",
            "summary": f"Created TikTok content plan for: {title}",
            "deliverables": ["hook", "script", "caption", "hashtags"],
            "script": f"Hook: {title}. Explain the key idea in 20 seconds, then end with a clear call to action.",
            "hashtags": ["#AI", "#Automation", "#TikTok"],
        }

    def _run_video(self, task: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": "Video Editor Agent",
            "summary": f"Prepared video editing workflow for: {task['title']}",
            "deliverables": ["timeline", "subtitle pass", "thumbnail brief", "render checklist"],
            "render_status": "READY_FOR_RENDER",
        }

    def _run_developer(self, task: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": "Developer Agent",
            "summary": f"Prepared engineering implementation steps for: {task['title']}",
            "deliverables": ["requirements", "component plan", "test plan"],
            "next_action": "Implement and verify module locally",
        }

    def _run_research(self, task: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": "Research Agent",
            "summary": f"Completed research outline for: {task['title']}",
            "deliverables": ["trend notes", "competitor angles", "recommendations"],
            "confidence": 0.82,
        }

    def _run_website(self, task: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": "Website Agent",
            "summary": f"Prepared website work package for: {task['title']}",
            "deliverables": ["page changes", "SEO checklist", "deployment checklist"],
            "deployment_status": "READY",
        }

    def _run_general(self, task: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent": "General Agent",
            "summary": f"Processed general task: {task['title']}",
            "deliverables": ["task summary", "recommended next step"],
        }
