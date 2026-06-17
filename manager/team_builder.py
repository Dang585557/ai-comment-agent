"""
AI-COMPANY
manager/team_builder.py

Team Builder
"""

from datetime import datetime


class TeamBuilder:

    def __init__(self):

        self.teams = {

            "tiktok": [],

            "video": [],

            "developer": [],

            "research": [],

            "website": []

        }

    def create_team(self, name):

        if name not in self.teams:

            self.teams[name] = []

            print(f"[TEAM] Created -> {name}")

    def add_agent(self, team, agent_name):

        if team not in self.teams:

            self.create_team(team)

        self.teams[team].append({

            "name": agent_name,

            "status": "ONLINE",

            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        })

        print(f"[TEAM] Added {agent_name} -> {team}")

    def remove_agent(self, team, agent_name):

        if team not in self.teams:

            return

        self.teams[team] = [

            agent

            for agent in self.teams[team]

            if agent["name"] != agent_name

        ]

    def get_team(self, team):

        return self.teams.get(team, [])

    def get_all(self):

        return self.teams

    def total_teams(self):

        return len(self.teams)

    def total_agents(self):

        total = 0

        for team in self.teams.values():

            total += len(team)

        return total

    def summary(self):

        result = {}

        for name, members in self.teams.items():

            result[name] = {

                "agents": len(members)

            }

        return result
