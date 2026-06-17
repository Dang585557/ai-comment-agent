"""
AI-COMPANY
manager/manager.py
Main AI Manager"""
from planner import Planner
from dispatcher import Dispatcher
from scheduler import Scheduler
from task_queue import TaskQueue
from report_generator import ReportGenerator
class AIManager:
def __init__(self):

 self.planner = Planner()
 self.dispatcher = Dispatcher()
 self.scheduler = Scheduler()
 self.queue = TaskQueue()
 self.report = ReportGenerator()

 def receive_command(self, command):
  print(f"[CEO] {command}")
   task = self.planner.create_plan(command)
   self.queue.add(task)
    self.dispatcher.dispatch(task)
    return True
    def system_status(self):
    return {
    "status": "ONLINE",
   "agents": "Running",
  "queue": self.queue.total_tasks()
    }
    def daily_report(self):
    return self.report.generate()
    if __name__ == "__main__":
    manager = AIManager()
    manager.receive_command(
   "สร้างคลิป TikTok 10 คลิป"
    )
    print(manager.system_status())
