"""
AI-COMPANY
manager/dispatcher.py

Task Dispatcher
"""
from datetime import datetime
class Dispatcher:
def __init__(self):
        self.available_agents = {
            "tiktok": "TikTok Manager",
            "video": "Video Manager",
            "developer": "Developer Manager",
            "research": "Research Manager",
            "website": "Website Manager",
            "general": "General Manager"
        }
    def dispatch(self, task):
        team = task.get("team", "general")

        agent = self.available_agents.get(
            team,
            "General Manager"
        )
        print("=" * 50)
        print("[DISPATCHER]")
        print(f"Time      : {datetime.now()}")
        print(f"Task      : {task['title']}")
        print(f"Team      : {team}")
        print(f"Priority  : {task['priority']}")
        print(f"Agent     : {agent}")
        print("=" * 50)
        return {
            "success": True,
            "assigned_team": team,
            "assigned_agent": agent,
            "status": "DISPATCHED"
        }
    def available(self):

        return list(self.available_agents.keys())

    def register_agent(self, team, manager_name):

        self.available_agents[team] = manager_name

        print(f"[Dispatcher] Registered {team}")

    def remove_agent(self, team):

        if team in self.available_agents:

            del self.available_agents[team]

            print(f"[Dispatcher] Removed {team}")

    def status(self):

        return {

            "registered_agents": len(self.available_agents),

            "teams": self.available_agents

        }
