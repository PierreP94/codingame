import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
temp = list()
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temp.append(t)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
t_min = 10001
t_min_a = 10001
indice = list()
for i in range(n):
    if t_min_a >= abs(temp[i]) :
        t_min_a = abs(temp[i])
        t_min = temp[i]
        
n_result = 0
for i in range(n) :
    if t_min_a == abs(temp[i]) :
        n_result += 1
        indice.append(i)

if n_result >=2 :
    for i in indice :
        if t_min < temp[i] :
            t_min = temp[i]
elif t_min != t_min_a :
    t_min = -t_min_a
if n==0 :
    t_min = 0


print(t_min)

