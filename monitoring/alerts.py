from datetime import datetime
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class AlertManager:

    def __init__(self):

        self.alerts = []

    def add(

        self,

        level: str,

        title: str,

        message: str

    ):

        alert = {

            "time": datetime.now().isoformat(),

            "level": level.upper(),

            "title": title,

            "message": message

        }

        self.alerts.append(alert)

        if level.upper() == "INFO":
            logging.info(message)

        elif level.upper() == "WARNING":
            logging.warning(message)

        elif level.upper() == "ERROR":
            logging.error(message)

        elif level.upper() == "CRITICAL":
            logging.critical(message)

        return alert

    def info(self, title, message):

        return self.add(
            "INFO",
            title,
            message
        )

    def warning(self, title, message):

        return self.add(
            "WARNING",
            title,
            message
        )

    def error(self, title, message):

        return self.add(
            "ERROR",
            title,
            message
        )

    def critical(self, title, message):

        return self.add(
            "CRITICAL",
            title,
            message
        )

    def history(self):

        return self.alerts

    def latest(self):

        if self.alerts:

            return self.alerts[-1]

        return None

    def clear(self):

        self.alerts.clear()

    def total(self):

        return len(self.alerts)


if __name__ == "__main__":

    alerts = AlertManager()

    alerts.info(
        "System",
        "AI-COMPANY started successfully."
    )

    print(alerts.latest())
