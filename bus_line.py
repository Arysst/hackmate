import json

file_path_recorreguts = 'recorreguts_consolidats.json'

with open(file_path_recorreguts, 'r', encoding='utf-8') as file:
    bus_line = json.load(file)


print(bus_line)
