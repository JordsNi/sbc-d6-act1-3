#square (Activity 2)

rows = int(input("Row: "))
cols = int(input("Column: "))
i = 0
while(i < rows):
    j = 0
    while(j < cols):
        if(i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
            print('*', end = '')
        else:
            print(' ', end = '')
        j = j + 1
    i = i + 1
    print()
