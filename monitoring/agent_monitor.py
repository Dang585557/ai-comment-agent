from datetime import datetime


class AgentMonitor:

    def __init__(self):

        self.agents = {}

    def register(self, name: str):

        self.agents[name] = {

            "status": "ONLINE",

            "current_task": None,

            "last_update": datetime.now().isoformat(),

            "completed_tasks": 0,

            "failed_tasks": 0

        }

    def update_task(self, name: str, task: str):

        if name in self.agents:

            self.agents[name]["current_task"] = task
            self.agents[name]["last_update"] = datetime.now().isoformat()

    def complete_task(self, name: str):

        if name in self.agents:

            self.agents[name]["completed_tasks"] += 1
            self.agents[name]["current_task"] = None
            self.agents[name]["last_update"] = datetime.now().isoformat()

    def failed_task(self, name: str):

        if name in self.agents:

            self.agents[name]["failed_tasks"] += 1
            self.agents[name]["last_update"] = datetime.now().isoformat()

    def offline(self, name: str):

        if name in self.agents:

            self.agents[name]["status"] = "OFFLINE"
            self.agents[name]["last_update"] = datetime.now().isoformat()

    def online(self, name: str):

        if name in self.agents:

            self.agents[name]["status"] = "ONLINE"
            self.agents[name]["last_update"] = datetime.now().isoformat()

    def get(self, name: str):

        return self.agents.get(name)

    def all(self):

        return self.agents

    def summary(self):

        return {

            "total_agents": len(self.agents),

            "online": len(
                [
                    a
                    for a in self.agents.values()
                    if a["status"] == "ONLINE"
                ]
            ),

            "offline": len(
                [
                    a
                    for a in self.agents.values()
                    if a["status"] == "OFFLINE"
                ]
            ),

            "time": datetime.now().isoformat()

        }


if __name__ == "__main__":

    monitor = AgentMonitor()

    monitor.register("TikTok Team")
    monitor.register("Video Team")

    print(monitor.summary())
