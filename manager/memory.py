"""
AI-COMPANY
manager/memory.py

Memory Manager
"""

from datetime import datetime


class Memory:

    def __init__(self):

        self.short_term = []

        self.long_term = []

    def remember(self, item):

        self.short_term.append({

            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "data": item

        })

        print(f"[MEMORY] Remember -> {item}")

    def save_long_term(self, item):

        self.long_term.append({

            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "data": item

        })

        print(f"[MEMORY] Saved -> {item}")

    def get_short_term(self):

        return self.short_term

    def get_long_term(self):

        return self.long_term

    def search(self, keyword):

        results = []

        for memory in self.short_term:

            if keyword.lower() in str(memory["data"]).lower():

                results.append(memory)

        for memory in self.long_term:

            if keyword.lower() in str(memory["data"]).lower():

                results.append(memory)

        return results

    def clear_short_term(self):

        self.short_term.clear()

    def clear_long_term(self):

        self.long_term.clear()

    def stats(self):

        return {

            "short_term": len(self.short_term),

            "long_term": len(self.long_term),

            "total": len(self.short_term) + len(self.long_term)

        }
