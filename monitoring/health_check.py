import socket
from datetime import datetime
import requests
import psutil


class HealthCheck:

    def __init__(self):
        self.results = {}

    def internet(self):

        try:

            requests.get(
                "https://www.google.com",
                timeout=5
            )

            return True

        except Exception:

            return False

    def disk(self):

        disk = psutil.disk_usage("/")

        return {

            "healthy": disk.percent < 90,

            "usage": disk.percent

        }

    def memory(self):

        memory = psutil.virtual_memory()

        return {

            "healthy": memory.percent < 90,

            "usage": memory.percent

        }

    def cpu(self):

        cpu = psutil.cpu_percent(interval=1)

        return {

            "healthy": cpu < 90,

            "usage": cpu

        }

    def hostname(self):

        return socket.gethostname()

    def run(self):

        self.results = {

            "time": datetime.now().isoformat(),

            "hostname": self.hostname(),

            "internet": self.internet(),

            "cpu": self.cpu(),

            "memory": self.memory(),

            "disk": self.disk(),

            "overall": "HEALTHY"

        }

        if (
            not self.results["internet"]
            or not self.results["cpu"]["healthy"]
            or not self.results["memory"]["healthy"]
            or not self.results["disk"]["healthy"]
        ):
            self.results["overall"] = "WARNING"

        return self.results


if __name__ == "__main__":

    checker = HealthCheck()

    print(checker.run())
