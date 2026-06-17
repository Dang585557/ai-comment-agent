"""
AI-COMPANY
ceo/permissions.py
"""
class Permissions:

    def __init__(self):

        self.admins = set()

    def add_admin(self, user_id):

        self.admins.add(str(user_id))

    def remove_admin(self, user_id):

        self.admins.discard(str(user_id))

    def is_admin(self, user_id):

        return str(user_id) in self.admins

    def get_admins(self):

        return list(self.admins)
