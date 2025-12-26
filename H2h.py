import json

with open('data.json', 'r') as file:
    data = json.load(file)

teams = sorted(data.keys())

H2H = []
for row_team in teams:
    row = []
    for col_team in teams:
        if row_team == col_team:
            row.append(0)
        else:
            row.append(data[row_team][col_team]["W"])
    H2H.append(row)






