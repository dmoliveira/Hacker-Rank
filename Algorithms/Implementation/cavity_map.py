cavity_map = []

for _ in range(int(input())):
    cavity_map.append(input())
    
for row, row_map in enumerate(cavity_map):
    output = ''
    row_map = list(row_map)
    for column, number in enumerate(row_map):
        output += number
        if column > 0 and column < len(row_map)-1\
            and row_map[column-1] < number\
            and row_map[column+1] < number\
            and row > 0 and row < len(cavity_map)-1\
            and list(cavity_map[row-1])[column] < number\
            and list(cavity_map[row+1])[column] < number:
                output = output[:-1] + 'X'
    print(output)             