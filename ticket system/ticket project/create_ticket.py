import datetime


class Ticket:
    def __init__(self, ticket_id, ticket_status, ticket_priority, ticket_agent, ticket_title, ticket_date):
        self.ticket_id = ticket_id
        self.ticket_status = ticket_status
        self.ticket_priority = ticket_priority
        self.ticket_agent = ticket_agent
        self.ticket_title = ticket_title
        self.ticket_date = ticket_date

    def __str__(self):
        return f"ID: {self.ticket_id}\n" \
               f"Title: {self.ticket_title}\n" \
               f"Status: {self.ticket_status}\n" \
               f"Agent: {self.ticket_agent}\n" \
               f"Priority: {self.ticket_priority}\n" \
               f"Date: {self.ticket_date}"


class CreateTicket:

    def __init__(self):
        self.ticket_id = 99999
        self.ticket_status = "open"
        self.ticket_priority = None
        self.ticket_title = None
        self.ticket_agent = None
        self.ticket_date = datetime.datetime.now().strftime("%d/%m/%Y")

    def give_ticket_id(self):
        self.ticket_id += 1
        return self.ticket_id

    def set_ticket_status(self, status):
        self.ticket_status = status

    def set_ticket_priority(self):
        print("Set Priority: \n 1 - High \n 2 - Medium \n 3 - Low")
        choice = int(input("Your Input >>: "))
        while choice not in [1, 2, 3]:
            choice = int(input('ERROR: Wrong Input. ☺'))

        priority_names = ['High', 'Medium', 'Low']
        self.ticket_priority = priority_names[choice - 1]

    def set_ticket_agent(self):
        ticket_agents = ["Peter Hirsnik", "Georg Mansky-Kummert", "STQM-Class"]
        print("Who is working on this ticket?")
        for idx, agent in enumerate(ticket_agents, start=1):
            print(f"{idx} - {agent}")

        choice = int(input("Your input >>: "))
        while choice > len(ticket_agents) or choice < 1:
            choice = int(input('ERROR: Wrong Input. ☺'))

        agent_name = ticket_agents[choice - 1]
        return agent_name

    def set_ticket_title(self, title):
        self.ticket_title = title

    def create_ticket(self):
        self.give_ticket_id()
        self.ticket_agent = None
        self.ticket_title = None
        self.ticket_priority = None

        if self.ticket_priority is None:
            self.set_ticket_priority()

        if self.ticket_title is None:
            self.set_ticket_title(input("Enter ticket title >>: "))

        agent = self.set_ticket_agent()
        ticket = Ticket(self.ticket_id, self.ticket_status, self.ticket_priority, agent, self.ticket_title, self.ticket_date)
        return ticket
