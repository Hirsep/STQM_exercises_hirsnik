import json


def write_json(assignments, file="ticket-log.json"):

    with open(file, "w") as f:
        json.dump(assignments.as_dict(), f, indent=4)


def read_json(file_name="ticket-log.json"):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data
