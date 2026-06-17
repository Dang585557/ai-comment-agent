"""
AI-COMPANY
ceo/command_center.py

CEO Command Center
"""

from manager.manager import AIManager


class CommandCenter:

    def __init__(self):

        self.manager = AIManager()

        self.command_history = []

    def execute(self, command: str):

        self.command_history.append(command)

        print("=" * 60)
        print("[CEO COMMAND]")
        print(command)
        print("=" * 60)

        result = self.manager.receive_command(command)

        return result

    def history(self):

        return self.command_history

    def last_command(self):

        if not self.command_history:

            return None

        return self.command_history[-1]

    def clear_history(self):

        self.command_history.clear()

    def system_status(self):

        return self.manager.system_status()

    def daily_report(self):

        return self.manager.daily_report()
