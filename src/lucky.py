# https://codeforces.com/problemset/problem/1676/A
# Python3

t = int(input())

for _ in range(t):
    ticket = input()
    
    sumaPrimeros = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sumaUltimos = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sumaPrimeros == sumaUltimos:
        print("YES")
    else:
        print("NO")
