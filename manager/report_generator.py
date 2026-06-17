"""
AI-COMPANY
manager/report_generator.py

Report Generator
"""

from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.reports = []

    def generate(self, summary=None):

        report = {

            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "system": "AI-COMPANY",

            "status": "ONLINE",

            "summary": summary if summary else {

                "agents": "Running",

                "tasks": "Processing",

                "health": "Healthy"

            }

        }

        self.reports.append(report)

        print("[REPORT] Report Generated")

        return report

    def get_reports(self):

        return self.reports

    def latest(self):

        if not self.reports:

            return None

        return self.reports[-1]

    def clear(self):

        self.reports.clear()

    def export(self):

        return {

            "total_reports": len(self.reports),

            "reports": self.reports

        }

    def stats(self):

        return {

            "generated": len(self.reports),

            "last_generated": self.reports[-1]["generated_at"] if self.reports else None

        }
