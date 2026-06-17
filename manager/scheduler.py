"""
AI-COMPANY
manager/scheduler.py

Task Scheduler
"""

from datetime import datetime
import time


class Scheduler:

    def __init__(self):

        self.running = False

        self.interval = 5

        self.jobs = []

    def add_job(self, name, callback):

        self.jobs.append({

            "name": name,

            "callback": callback,

            "enabled": True

        })

        print(f"[SCHEDULER] Added Job -> {name}")

    def remove_job(self, name):

        self.jobs = [

            job for job in self.jobs

            if job["name"] != name

        ]

    def enable_job(self, name):

        for job in self.jobs:

            if job["name"] == name:

                job["enabled"] = True

    def disable_job(self, name):

        for job in self.jobs:

            if job["name"] == name:

                job["enabled"] = False

    def run_once(self):

        print(f"[SCHEDULER] {datetime.now()}")

        for job in self.jobs:

            if not job["enabled"]:

                continue

            try:

                job["callback"]()

            except Exception as e:

                print(f"[ERROR] {job['name']} -> {e}")

    def start(self):

        self.running = True

        print("[SCHEDULER] Started")

        while self.running:

            self.run_once()

            time.sleep(self.interval)

    def stop(self):

        self.running = False

        print("[SCHEDULER] Stopped")

    def status(self):

        return {

            "running": self.running,

            "interval": self.interval,

            "jobs": len(self.jobs)

        }

    def set_interval(self, seconds):

        self.interval = seconds
