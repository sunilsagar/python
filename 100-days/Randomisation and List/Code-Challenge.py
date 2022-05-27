row1 = ["a","a","a"]
row2 = ["a","a","a"]
row3 = ["a","a","a"]

map = [row1, row2, row3] 
print(f"{row1}\n{row2}\n{row3}")
print(map)

position = input("Wehere do you want to put the tresure? ")

####
horizontal = int(position[0])
vertical = int(position[1])

#print(map[vertical -1])
selected_row = map[vertical -1]
selected_row[horizontal -1 ] = "x"

print(f"{row1}\n{row2}\n{row3}")