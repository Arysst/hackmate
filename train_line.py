import json

file_path_trams_metro = 'trams_linia_metro.json'

with open(file_path_trams_metro, 'r', encoding='utf-8') as file:
    trams_metro_data = json.load(file)

print(trams_metro_data)
