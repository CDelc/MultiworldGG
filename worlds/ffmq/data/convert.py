import yaml

with open("entrances.yaml", "r") as file:
    ent = yaml.safe_load(file)
with open("rooms.yaml", "r") as file:
    rooms = yaml.safe_load(file)

with open("rooms.py", "w") as file:
    file.write("rooms = " + str(rooms) + "\n" + "entrances = " + str(ent))