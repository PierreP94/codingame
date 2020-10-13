import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line_1 = input()
line_2 = input()
line_3 = input()
N1={}
N2={}
N3={}
segments1 = {}
segments2 = {}
segments3 = {}
segmentchiffre = {}
chiffre = {}
answer = ""
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
N = line_1 + "\n" + line_2 + "\n" + line_3
for i in range(0, len(line_1), 3):
    j = i//3
    N1[j] = line_1[i:i+3]
    N2[j] = line_2[i:i+3]
    N3[j] = line_3[i:i+3]
for i in range (0, len(N1)):
    segments1[i] = len(N1[i].strip())
    segments2[i] = len(N2[i].strip())
    segments3[i] = len(N3[i].strip())
    segmentchiffre[i] =+ segments1[i] + segments2[i] + segments3[i]

for i in range(len(line_1)//3) :

    if segmentchiffre[i] == 2 : chiffre[i] = "1"
    elif segmentchiffre[i] == 4 : chiffre[i] = "4"
    elif segmentchiffre[i] == 3 : chiffre[i] = "7"
    elif segmentchiffre[i] == 6 : 
        if segments3[i] == 2 : chiffre[i] = "9"
        elif  N2[i][1] == "_" : chiffre[i] = "6"
    elif segmentchiffre[i] == 7 :
        if N2[i][1] == "_": chiffre[i] = "8"
        else : chiffre[i] = "0"
    elif segmentchiffre[i] == 5 : 
        if N3[i][0] == "|" : chiffre[i] = "2"
        elif N2[i][0] == "|" : chiffre[i] = "5"
        else : chiffre[i] = "3"

for i in range(len(chiffre)) :
    answer += str(chiffre[i])


print(answer)

