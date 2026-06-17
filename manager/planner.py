"""
AI-COMPANY
manager/planner.py
Task Planner"""
from datetime
import datetime
class Planner:
def __init__(self):self.supported_teams = ["tiktok","video","developer","research","website"]
def create_plan(self, command: str):team = self.detect_team(command)priority = self.detect_priority(command)plan = {
   "title": command,
   "team": team,
    "priority": priority,
    "status": "PENDING",
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}
print(f"[PLANNER] New Plan -> {plan}")
 return plan
 def detect_team(self, command: str):text = command.lower()
 if "tiktok" in text:
 return "tiktok"
 if "video" in text:
 return "video"
 if "website" in text:
 return "website"
 if "code" in text:
 return "developer"
 if "developer" in text:
 return "developer"
 if "research" in text:
 return "research"return "
