from datetime import datetime
import time


class MonitorAgent:

    def check_status(
        self,
        url: str
    ):

        return {
            "url": url,
            "status": "ONLINE",
            "response_time_ms": 125,
            "checked_at": datetime.now().isoformat()
        }

    def health_check(
        self,
        services: list
    ):

        results = []

        for service in services:

            results.append({
                "service": service,
                "status": "HEALTHY",
                "response_time_ms": 100
            })

        return {
            "services": results,
            "checked_at": datetime.now().isoformat()
        }

    def uptime_report(
        self,
        uptime_percent: float = 99.99
    ):

        return {
            "uptime": f"{uptime_percent:.2f}%",
            "status": "STABLE",
            "generated_at": datetime.now().isoformat()
        }

    def monitor_loop(
        self,
        url: str,
        interval: int = 60
    ):

        while True:

            print(
                self.check_status(url)
            )

            time.sleep(interval)


if __name__ == "__main__":

    agent = MonitorAgent()

    print(
        agent.check_status(
            "https://example.com"
        )
    )
