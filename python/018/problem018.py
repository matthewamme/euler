"""
Project Euler Problem #017

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


#Import the text lazily
text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

#split into array
rows = text.split('\n')
#flip upside down and start from the bottom
rows.reverse()

#split nested arrays into arrays and convert to int
for row, value in enumerate(rows):
    rows[row] = value.split(" ")
    for col,colvalue in enumerate(value.split(" ")):
        rows[row][col] = int(colvalue)

depth = 0
for row, value in enumerate(rows):
    if depth + 1 == len(rows):
        #print final answer (last rows value)
        print value[0]
    else:
        for col, entry in enumerate(value):
            if (col + 1 ) == len(value):
                #look at this value and next, so skip last column
                exit
            else:
                #replace next rows value with max of this and next value
                rows[depth+1][col]= rows[depth+1][col] + max(entry,value[col+1])
        depth = depth + 1
              



