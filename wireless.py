import sqlite3

csvfile = 'awesome-01.csv'

with open (csvfile) as f:
    lines = f.readlines()
   

breaks = []
for i in range(len(lines)):
    tokens = [t.strip() for t in lines[i].split(",")]
    print(len(tokens[0]))
    if len(tokens) == 1:
        breaks.append(i)


ap_header = lines[breaks[0]+1]
ap_data = lines[breaks[0]+2:breaks[1]-1]

client_header = lines[breaks[1]+1]

client_data   = lines[breaks[1]+2:breaks[2]-1]


