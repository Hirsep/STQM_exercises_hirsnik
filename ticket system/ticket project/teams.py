from tickets import Ticket


class Team:
    def __init__(self, name: str, *members: str):
        self.name = name
        self.members = members

    def __str__(self):
        return f"{self.name} {self.members}:"

    def as_dict(self):
        return {
            'name': self.name,
            'members': list(self.members)
        }


class Assignments(dict[Team, list[Ticket]]):
    def __init__(self):
        super().__init__()

    def add(self, team, ticket):
        if team not in self:
            self[team] = [ticket]
        else:
            self[team].append(ticket)

    def __str__(self):
        result = ""
        for team, tickets in self.items():
            result += f"{team.name}: "
            result += ", ".join(team.members) + "\n"
            for ticket in tickets:
                result += str(ticket) + "\n"
            result += "\n"
        return result

    def as_dict(self):
        assignments_dict = {}
        for team, tickets in self.items():
            assignments_dict[team.name] = {
                'members': list(team.members),
                'tickets': [ticket.as_dict() for ticket in tickets]
            }
        return assignments_dict
